"""core 模块：游戏核心逻辑（不依赖 Streamlit 界面）"""

from .player import Player, load_player, save_player, default_player
from .battle import run_user_code, check_answer
from .engine import GameEngine

__all__ = [
    "Player",
    "load_player",
    "save_player",
    "default_player",
    "run_user_code",
    "check_answer",
    "GameEngine",
]
