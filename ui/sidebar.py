"""
侧边栏：角色卡 & 进度显示
"""

import streamlit as st

from core.player import EXP_PER_LEVEL


def render_sidebar(engine):
    """渲染侧边栏角色卡"""
    p = st.session_state.player

    with st.sidebar:
        st.markdown("## 🎮 角色卡")
        st.markdown(f"### 👤 {p.name}")

        # 等级与经验进度
        exp_in_level = p.exp_in_current_level()
        st.progress(
            exp_in_level / EXP_PER_LEVEL,
            text=f"Lv.{p.level}  经验 {exp_in_level}/{EXP_PER_LEVEL}",
        )

        # 属性
        col1, col2 = st.columns(2)
        col1.metric("❤️ HP", f"{p.hp}/{p.max_hp}")
        col2.metric("⚔️ 攻击", p.attack)
        col1.metric("🛡️ 防御", p.defense)
        col2.metric("⭐ 总经验", p.exp)

        # 背包
        st.markdown("### 🎒 背包")
        if p.inventory:
            for item in p.inventory:
                st.markdown(f"- {item}")
        else:
            st.markdown("_空空如也，去打怪吧！_")

        # 进度 + 关卡选择
        st.markdown("---")
        st.markdown("### 📊 进度 & 关卡跳转")
        total = engine.total_levels()
        done = engine.completed_count(p)
        st.progress(
            done / total,
            text=f"{engine.chapter_title()} {done}/{total} 关"
        )
        # 总进度
        st.caption(f"📊 总进度：{engine.total_progress(p)}")

        # 可点击的关卡列表
        st.markdown("**🗺️ 选择关卡：**")
        _render_level_selector(engine, p)

        # 返回地图
        if st.button("🏠 返回地图", use_container_width=True):
            st.session_state.current_level_idx = -1
            st.session_state.battle_result = None
            st.rerun()

        # 重置按钮
        st.markdown("---")
        if st.button("🔄 重新开始（清空存档）", use_container_width=True):
            from core.player import default_player

            st.session_state.player = default_player()
            st.session_state.player.save()
            st.session_state.current_chapter = 1
            st.session_state.current_level_idx = -1
            st.session_state.battle_result = None
            st.rerun()


def _render_level_selector(engine, player):
    """侧边栏关卡选择器：每关一行，可点击跳转"""
    for idx, level in enumerate(engine.levels):
        is_completed = player.has_completed(level["id"])
        is_locked = engine.is_locked(idx, player)
        is_current = st.session_state.current_level_idx == idx

        if is_completed:
            icon = "✅"
            label = f"{icon} {level['id']} {level['name']}"
            btn_type = "secondary"
        elif is_locked:
            icon = "🔒"
            label = f"{icon} {level['id']} 🔒 未解锁"
            btn_type = "secondary"
        else:
            icon = "⚔️"
            label = f"{icon} {level['id']} {level['name']}"
            btn_type = "primary" if is_current else "secondary"

        # 锁定关卡不可点击
        if is_locked:
            st.markdown(f"<div style='padding:4px 8px;opacity:0.5'>{label}</div>", unsafe_allow_html=True)
        else:
            if st.button(label, key=f"sidebar_level_{level['id']}", type=btn_type, use_container_width=True):
                st.session_state.current_level_idx = idx
                st.session_state.battle_result = None
                st.rerun()
