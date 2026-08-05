"""
战斗界面：编程题挑战
===================
代码编辑器使用 streamlit-ace（VS Code 同款内核），
支持 Python 语法高亮、自动缩进、行号、圆润主题。
"""

import streamlit as st
from streamlit_ace import st_ace

from core.battle import check_answer


def init_session():
    """初始化会话状态"""
    if "player" not in st.session_state:
        from core.player import load_player
        st.session_state.player = load_player()
    if "current_level_idx" not in st.session_state:
        st.session_state.current_level_idx = 0
    if "battle_result" not in st.session_state:
        st.session_state.battle_result = None
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = "teach"


def render_battle(engine, level_idx):
    """渲染战斗界面"""
    level = engine.get_level(level_idx)
    if level is None:
        st.error("关卡不存在")
        return

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
                type="primary" if st.session_state.selected_mode == key else "secondary",
            ):
                st.session_state.selected_mode = key
                st.session_state.battle_result = None
                st.rerun()

    mode = level["modes"][st.session_state.selected_mode]
    st.markdown(f"**当前难度**：{mode_labels[st.session_state.selected_mode]}")
    st.markdown(f"**任务**：{mode['instruction']}")

    # ---------- 代码模板与输入（Ace Editor） ----------
    if st.session_state.selected_mode == "teach":
        st.info(f"📝 参考代码：\n```python\n{mode['template']}\n```")

    # 根据难度设置初始代码
    if st.session_state.selected_mode == "fill":
        default_code = mode.get("template", "")
    elif st.session_state.selected_mode == "teach":
        default_code = mode.get("template", "")
    else:
        default_code = ""

    # Ace Editor：专业代码编辑器（VS Code 内核）
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="dracula",
        keybinding="vscode",
        key=f"ace_{level['id']}_{st.session_state.selected_mode}",
        height=220,
        show_gutter=True,
        show_print_margin=False,
        wrap=True,
        font_size=14,
        tab_size=4,
        auto_update=True,
        readonly=False,
    )

    # ---------- 按钮区 ----------
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        if st.button("⚔️ 发起攻击（运行代码）", type="primary", use_container_width=True):
            if not user_code or not user_code.strip():
                st.warning("请先输入代码！")
            else:
                _handle_attack(engine, level, mode, user_code)
    with col2:
        if st.button("💡 查看提示"):
            st.info(f"💡 提示：{mode['hint']}")
    with col3:
        if st.button("👁️ 显示答案"):
            if st.session_state.selected_mode == "challenge":
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
                    st.rerun()
            else:
                st.balloons()
                st.success("🎉 恭喜！你已通关第一章「语法森林」！")
        with col_b:
            if st.button("🏠 返回地图", use_container_width=True):
                st.session_state.current_level_idx = -1
                st.session_state.battle_result = None
                st.rerun()
    else:
        st.error(result["message"])
        if result["output"]:
            st.markdown("**你的输出：**")
            st.code(result["output"], language="text")
        st.info("💪 别灰心，再试一次！可以点击「💡 查看提示」")
