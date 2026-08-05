"""
玩家系统：角色属性、存档、读档、升级逻辑
======================================
这里只用 Python 标准库，不依赖任何界面框架。
存档以 JSON 格式保存到 save/player.json
"""

import json
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List


# 存档路径（项目根目录 / save / player.json）
SAVE_PATH = Path(__file__).parent.parent / "save" / "player.json"

# 每多少经验升一级
EXP_PER_LEVEL = 100

# 每次升级的属性增量
LEVEL_UP_BONUS = {
    "max_hp": 20,
    "attack": 5,
    "defense": 2,
}


@dataclass
class Player:
    """玩家角色数据类"""

    name: str = "勇者"
    level: int = 1
    exp: int = 0
    hp: int = 100
    max_hp: int = 100
    attack: int = 10
    defense: int = 5
    inventory: List[str] = field(default_factory=list)
    completed_levels: List[str] = field(default_factory=list)
    current_chapter: int = 1

    # ---------- 经验与等级 ----------
    def gain_exp(self, amount: int) -> bool:
        """
        增加经验值，若升级则自动提升属性
        返回：是否升级
        """
        old_level = self.level
        self.exp += amount
        self.level = 1 + self.exp // EXP_PER_LEVEL

        if self.level > old_level:
            # 升级了：提升属性 + 满血
            diff = self.level - old_level
            self.max_hp += LEVEL_UP_BONUS["max_hp"] * diff
            self.attack += LEVEL_UP_BONUS["attack"] * diff
            self.defense += LEVEL_UP_BONUS["defense"] * diff
            self.hp = self.max_hp  # 升级回满血
            return True
        return False

    def exp_in_current_level(self) -> int:
        """当前等级内已积累的经验"""
        return self.exp % EXP_PER_LEVEL

    # ---------- 关卡进度 ----------
    def complete_level(self, level_id: str, item: str = None) -> None:
        """标记关卡为已完成，并加入背包"""
        if level_id not in self.completed_levels:
            self.completed_levels.append(level_id)
        if item and item not in self.inventory:
            self.inventory.append(item)

    def has_completed(self, level_id: str) -> bool:
        return level_id in self.completed_levels

    # ---------- 存档 ----------
    def save(self) -> None:
        """保存到 JSON 文件"""
        SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(SAVE_PATH, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=2)

    def to_dict(self) -> dict:
        return asdict(self)


# ---------- 模块级便捷函数 ----------
def default_player() -> Player:
    """新建一个默认玩家"""
    return Player()


def load_player() -> Player:
    """读取存档，不存在则返回新玩家"""
    if not SAVE_PATH.exists():
        return default_player()
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Player(**data)
    except Exception:
        # 存档损坏时返回新玩家
        return default_player()


def save_player(player: Player) -> None:
    """保存玩家存档"""
    player.save()
