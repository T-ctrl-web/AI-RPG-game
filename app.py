"""
AI 勇者纪元 - Python 学习 RPG 游戏
==================================
启动方式：
    streamlit run app.py

项目结构：
    app.py              <- 本文件（入口）
    core/               核心逻辑层（player / battle / engine）
    data/               关卡数据层（chapters）
    ui/                 界面层（sidebar / map_view / battle_view）
    save/player.json    自动存档
"""

import streamlit as st

from data.chapters import CHAPTER1_LEVELS
from core.engine import GameEngine
from ui import render_sidebar, render_map, render_battle, init_session


def main():
    # 页面配置
    st.set_page_config(
        page_title="AI 勇者纪元",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # 初始化会话状态
    init_session()

    # 创建游戏引擎（加载第一章关卡）
    engine = GameEngine(CHAPTER1_LEVELS)

    # 顶部标题
    st.title("🎮 AI 勇者纪元")
    st.caption("用玩游戏的方式学 Python")

    # 侧边栏角色卡
    render_sidebar(engine)

    # 主区域：根据状态显示地图或战斗
    idx = st.session_state.current_level_idx
    if idx == -1:
        render_map(engine)
    elif 0 <= idx < engine.total_levels():
        render_battle(engine, idx)
    else:
        render_map(engine)


if __name__ == "__main__":
    main()
