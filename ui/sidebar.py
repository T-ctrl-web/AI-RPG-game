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

        # 进度
        st.markdown("---")
        st.markdown("### 📊 进度")
        total = engine.total_levels()
        done = engine.completed_count(p)
        st.progress(done / total, text=f"第一章 {done}/{total} 关")

        # 重置按钮
        st.markdown("---")
        if st.button("🔄 重新开始（清空存档）", use_container_width=True):
            from core.player import default_player

            st.session_state.player = default_player()
            st.session_state.player.save()
            st.session_state.current_level_idx = 0
            st.session_state.battle_result = None
            st.rerun()
