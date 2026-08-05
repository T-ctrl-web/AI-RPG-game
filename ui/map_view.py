"""
地图视图：关卡列表与选择
"""

import streamlit as st


def render_map(engine):
    """渲染关卡地图"""
    p = st.session_state.player

    st.markdown(f"# 🗺️ {engine.chapter_title()} · {engine.chapter_meta.get('chinese','')}")
    st.markdown(f"> _{engine.chapter_subtitle()}_")

    # 顶部：进度概览 + 继续按钮
    done = engine.completed_count(p)
    total = engine.total_levels()
    st.progress(done / total, text=f"本章通关进度：{done}/{total}")

    # 继续冒险：跳到下一个未通关的已解锁关卡
    next_idx = engine.find_next_unlocked_uncompleted(p)
    if next_idx is not None:
        next_level = engine.get_level(next_idx)
        if st.button(
            f"▶ 继续冒险：{next_level['scene']}（{next_level['id']}）",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.current_level_idx = next_idx
            st.session_state.battle_result = None
            st.rerun()

    st.markdown("---")

    for idx, level in enumerate(engine.levels):
        _render_level_card(engine, level, idx, p)


def _render_level_card(engine, level, idx, player):
    """渲染单个关卡卡片"""
    is_completed = player.has_completed(level["id"])
    is_locked = engine.is_locked(idx, player)
    is_skel = engine.is_skeleton(level)

    col1, col2, col3 = st.columns([6, 2, 2])
    with col1:
        icon = "✅" if is_completed else ("🔒" if is_locked else "⚔️")
        boss_tag = " [BOSS]" if engine.is_boss(level) else ""
        skel_tag = " 🚧 待补充" if is_skel else ""
        st.markdown(f"### {icon} {level['scene']}{boss_tag}{skel_tag}")
        st.caption(f"关卡 {level['id']} · {level['name']}")
    with col2:
        st.markdown(f"**怪物**\n{level['monster']}")
        st.caption(f"HP: {level['monster_hp']}")
    with col3:
        st.markdown(f"**奖励**\n⭐ {level['reward_exp']}")
        st.caption(level["reward_item"])

    # 按状态显示按钮
    if is_locked:
        st.info("🔒 通关上一关后解锁")
    elif is_completed:
        st.success("✅ 已通关！可重玩刷经验")
        if st.button(f"重玩 {level['id']}", key=f"replay_{level['id']}"):
            st.session_state.current_level_idx = idx
            st.session_state.battle_result = None
            st.rerun()
    else:
        label = f"挑战 {level['id']} ▶"
        if is_skel:
            label = f"暂玩 {level['id']}（骨架） ▶"
            st.warning("🚧 本关三档题目后续补充，当前提供通用模板通关。")
        if st.button(label, key=f"play_{level['id']}", type="primary"):
            st.session_state.current_level_idx = idx
            st.session_state.battle_result = None
            st.rerun()

    st.markdown("---")

