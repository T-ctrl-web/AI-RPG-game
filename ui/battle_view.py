"""
战斗界面：编程题挑战
===================
代码编辑器使用 Streamlit 原生 st.code_editor（1.41+ 官方组件），
支持 Python 语法高亮、行号、Tab 缩进、VS Code 键位，
不依赖任何第三方组件，从根本上避免 removeChild 爆红问题。
"""

import streamlit as st

from core.battle import check_answer

# 代码编辑器的全局唯一 key —— 永不变化
# 官方组件的销毁逻辑稳定，单实例全局复用，永远不会触发第三方组件的 DOM 时序 bug
ACE_KEY = "code_editor_main"


def init_session():
    """初始化会话状态"""
    if "player" not in st.session_state:
        from core.player import load_player
        st.session_state.player = load_player()
    if "current_chapter" not in st.session_state:
        st.session_state.current_chapter = 1
    if "current_level_idx" not in st.session_state:
        # 默认显示地图（-1），玩家可自由选择已解锁/已通关的关卡
        st.session_state.current_level_idx = -1
    if "battle_result" not in st.session_state:
        st.session_state.battle_result = None
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = "teach"
    if "code_draft" not in st.session_state:
        # 草稿缓存：key = f"{level_id}:{mode}"，每个模式独立保存用户写的代码
        # ⚠️ 只在用户明确动作（切模式/攻击/切关）时写入，不存模板默认值
        st.session_state.code_draft = {}
    if "_last_editor_ctx" not in st.session_state:
        # 上次显示编辑器时的上下文（level_id:mode），用于判断是否需要刷新编辑器内容
        st.session_state._last_editor_ctx = None


def render_battle(engine, level_idx):
    """渲染战斗界面"""
    level = engine.get_level(level_idx)
    if level is None:
        st.error("关卡不存在")
        return

    current_mode = st.session_state.selected_mode
    editor_key = ACE_KEY
    draft_key = f"{level['id']}:{current_mode}"
    ctx = f"{level['id']}:{current_mode}"   # 当前上下文：关卡 + 模式
    mode = level["modes"][current_mode]

    # ---------- 顶部：场景与怪物 ----------
    st.markdown(f"# {level['scene']}")
    if engine.is_boss(level):
        st.error(f"⚔️ BOSS 战：{level['monster']}（HP: {level['monster_hp']}）")
    else:
        st.warning(f"⚔️ 遭遇：{level['monster']}（HP: {level['monster_hp']}）")

    # 剧情 NPC 对话
    with st.chat_message("npc", avatar="🧙"):
        st.markdown(f"_{level['story']}_")

    # 知识小课堂
    with st.expander("📖 知识小课堂（点击展开）", expanded=True):
        for k in level["knowledge"]:
            st.markdown(f"- {k}")

    st.markdown("---")

    # ---------- 难度选择 ----------
    mode_labels = {"teach": "🟢 教学", "fill": "🟡 填空", "challenge": "🔴 挑战"}
    st.markdown("### 选择难度")
    cols = st.columns(3)
    for i, key in enumerate(["teach", "fill", "challenge"]):
        with cols[i]:
            if st.button(
                f"{mode_labels[key]}\n{level['modes'][key]['label']}",
                key=f"mode_{key}",
                use_container_width=True,
                type="primary" if current_mode == key else "secondary",
            ):
                # 切模式前：把当前编辑器代码存进「旧模式」的草稿（只存用户真实修改过的）
                if editor_key in st.session_state and st.session_state[editor_key] is not None:
                    old_draft = f"{level['id']}:{current_mode}"
                    code_now = st.session_state[editor_key]
                    old_mode_cfg = level["modes"][current_mode]
                    old_template = old_mode_cfg.get("template", "") if current_mode != "challenge" else ""
                    if code_now.strip() != "" and code_now != old_template:
                        st.session_state.code_draft[old_draft] = code_now
                # 切到新模式，清空 last_ctx → 编辑器会重算并显示新模式的代码
                st.session_state.selected_mode = key
                st.session_state.battle_result = None
                st.session_state._last_editor_ctx = None
                st.rerun()

    st.markdown(f"**当前难度**：{mode_labels[current_mode]}")
    st.markdown(f"**任务**：{mode['instruction']}")

    # ---------- 参考代码（教学模式） ----------
    if current_mode == "teach":
        st.info(f"📝 参考代码：\n```python\n{mode['template']}\n```")

    # Step 1：计算编辑器本应显示的「正确代码」（intended_code）
    # 优先级：用户在此模式下真实写过的草稿 > 模式自带模板（填空___ / 教学完整 / 挑战空）
    saved_draft = st.session_state.code_draft.get(draft_key)
    if saved_draft and saved_draft.strip():
        intended_code = saved_draft
        st.caption("💾 已恢复你上次在此模式写的代码。")
    else:
        if current_mode == "challenge":
            intended_code = ""                              # 挑战：空白，不给答案
        elif current_mode == "fill":
            intended_code = mode.get("template", "")        # 填空：含 ___ 的模板
        else:  # teach
            intended_code = mode.get("template", "")        # 教学：完整可运行代码

    # Step 2：上下文变化时，手动同步编辑器 session_state
    # Streamlit 有状态组件一旦 key 存在，widget 的 value= 只在首次渲染生效；
    # 之后无论传什么 value，组件显示都以 session_state[key] 为准。
    # 所以必须手动写 session_state[editor_key] = intended_code 才能切关卡/切模式时正确刷新内容。
    if st.session_state._last_editor_ctx != ctx:
        st.session_state[editor_key] = intended_code
        st.session_state._last_editor_ctx = ctx

    # ---------- 代码编辑器（Streamlit 1.41+ 原生，官方组件）----------
    # 不销毁实例（key 全局固定）→ 彻底避免第三方组件的 removeChild 爆红
    user_code = st.code_editor(
        value=intended_code,
        language="python",
        theme="dark",
        key=editor_key,
        height=260,
        line_numbers=True,
        show_copy_button=True,
        wrap=True,
        tab_size=4,
    )

    # ---------- 按钮区 ----------
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        if st.button("⚔️ 发起攻击（运行代码）", type="primary", use_container_width=True):
            if not user_code or not user_code.strip():
                st.warning("请先输入代码！")
            else:
                # 攻击前：草稿入库（只存用户真实修改过的内容，不存默认模板）
                if current_mode == "challenge":
                    should_save_draft = bool(user_code and user_code.strip())
                else:  # teach / fill
                    should_save_draft = user_code != mode.get("template", "")
                if should_save_draft:
                    st.session_state.code_draft[draft_key] = user_code
                _handle_attack(engine, level, mode, user_code)
    with col2:
        if st.button("💡 查看提示"):
            st.info(f"💡 提示：{mode['hint']}")
    with col3:
        if st.button("👁️ 显示答案"):
            if current_mode == "challenge":
                st.code(mode["hint"], language="text")
            else:
                st.code(mode["expected"], language="python")

    # ---------- 战斗结果 ----------
    _render_battle_result(engine, level, mode)


def _handle_attack(engine, level, mode, user_code):
    """处理攻击按钮：判定 + 奖励"""
    is_correct, msg, output = check_answer(user_code, mode)
    st.session_state.battle_result = {
        "is_correct": is_correct,
        "message": msg,
        "output": output,
        "mode": st.session_state.selected_mode,
    }

    if is_correct:
        gained = engine.settle_reward(level, st.session_state.selected_mode, st.session_state.player)
        st.session_state.last_gained_exp = gained
        # 通关：本关卡所有模式的草稿全部清理，下次进本关时从新鲜模板开始
        for k in list(st.session_state.code_draft.keys()):
            if k.startswith(f"{level['id']}:"):
                del st.session_state.code_draft[k]
        # 重置编辑器上下文：下次进入新关卡/新模式时强制刷新模板
        st.session_state._last_editor_ctx = None
    st.rerun()


def _render_battle_result(engine, level, mode):
    """渲染战斗结果区域"""
    if not st.session_state.battle_result:
        return

    result = st.session_state.battle_result
    if result["is_correct"]:
        st.balloons()
        st.success(result["message"])

        gained = st.session_state.get("last_gained_exp", level["reward_exp"])
        st.markdown(f"🎁 获得经验 +{gained}，获得 {level['reward_item']}")

        col_a, col_b = st.columns(2)
        with col_a:
            next_idx = engine.next_level_index(st.session_state.current_level_idx)
            if next_idx is not None:
                if st.button("▶ 下一关", type="primary", use_container_width=True):
                    st.session_state.current_level_idx = next_idx
                    st.session_state.battle_result = None
                    st.session_state.selected_mode = "teach"
                    # 切下一关：重置编辑器上下文，保证编辑器显示下一关的正确模板
                    st.session_state._last_editor_ctx = None
                    st.rerun()
            else:
                st.balloons()
                # 动态读取章节名（适配全部 6 章，不硬编码）
                chapter_meta = {}
                try:
                    from data.helpers import CHAPTER_META
                    chapter_meta = CHAPTER_META.get(st.session_state.get("current_chapter", 1), {})
                except Exception:
                    chapter_meta = {"title": "本章", "chinese": "当前章节"}
                st.success(f"🎉 恭喜！你已通关{chapter_meta.get('chinese', '本章')}「{chapter_meta.get('title', '')}」！")
        with col_b:
            if st.button("🏠 返回地图", use_container_width=True):
                st.session_state.current_level_idx = -1
                st.session_state.battle_result = None
                # 返回地图：不清草稿，但下次再进关/切关时会按 ctx 刷新
                st.session_state._last_editor_ctx = None
                st.rerun()
    else:
        st.error(result["message"])
        if result["output"]:
            st.markdown("**你的输出：**")
            st.code(result["output"], language="text")
        st.info("💪 别灰心，再试一次！可以点击「💡 查看提示」")
