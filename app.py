"""
AI 勇者纪元 - Python 学习 RPG 游戏
==================================
启动：streamlit run app.py
"""

import streamlit as st

from data.chapters import CHAPTER_META
from core.engine import GameEngine, TOTAL_CHAPTERS
from ui import render_sidebar, render_map, render_battle, init_session


def main():
    st.set_page_config(
        page_title="AI 勇者纪元",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    init_session()

    # 加载当前章节引擎
    engine = GameEngine(st.session_state.current_chapter)

    # 顶部标题 + 章节切换
    _render_header(engine)

    # 侧边栏
    render_sidebar(engine)

    # 主区域
    idx = st.session_state.current_level_idx
    if idx == -1:
        render_map(engine)
    elif 0 <= idx < engine.total_levels():
        render_battle(engine, idx)
    else:
        render_map(engine)


def _render_header(engine: GameEngine):
    p = st.session_state.player
    total_pct = engine.total_completed_ratio(p)

    st.title(f"🎮 AI 勇者纪元 · {engine.chapter_title()}")
    st.caption(engine.chapter_subtitle())

    # 章节切换条
    tabs = []
    for n in range(1, TOTAL_CHAPTERS + 1):
        meta = CHAPTER_META[n]
        unlocked = engine.is_chapter_unlocked(n, p)
        label = f"{meta['emoji']} {n}. {meta['title']}"
        if not unlocked:
            label = f"🔒 {label}（通关上一章解锁）"
        tabs.append(label)

    selected = st.radio(
        "选择章节：",
        tabs,
        index=min(engine.chapter_number - 1, TOTAL_CHAPTERS - 1),
        horizontal=True,
        label_visibility="collapsed",
    )
    # 根据选中的 label 解析章节号
    for n in range(1, TOTAL_CHAPTERS + 1):
        if CHAPTER_META[n]["title"] in selected:
            if engine.is_chapter_unlocked(n, p) and st.session_state.current_chapter != n:
                st.session_state.current_chapter = n
                st.session_state.current_level_idx = -1
                st.session_state.battle_result = None
                st.rerun()
            break

    st.progress(total_pct, text=f"📊 总进度：{engine.total_progress(p)}")


if __name__ == "__main__":
    main()
