"""
地图视图：关卡列表与选择
"""

import streamlit as st


def render_map(engine):
    """渲染关卡地图"""
    p = st.session_state.player

    st.markdown("# 🗺️ 语法森林 · 第一章")
    st.markdown("> _穿越六大关卡，击败 BOSS 缩进蛇妖，收集「语法晶石」_")
    st.markdown("---")

    for idx, level in enumerate(engine.levels):
        _render_level_card(engine, level, idx, p)


def _render_level_card(engine, level, idx, player):
    """渲染单个关卡卡片"""
    is_completed = player.has_completed(level["id"])
    is_locked = engine.is_locked(idx, player)

    col1, col2, col3 = st.columns([6, 2, 2])
    with col1:
        icon = "✅" if is_completed else ("🔒" if is_locked else "⚔️")
        boss_tag = " [BOSS]" if engine.is_boss(level) else ""
        st.markdown(f"### {icon} {level['scene']}{boss_tag}")
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
        if st.button(
            f"挑战 {level['id']} ▶",
            key=f"play_{level['id']}",
            type="primary",
        ):
            st.session_state.current_level_idx = idx
            st.session_state.battle_result = None
            st.rerun()

    st.markdown("---")
