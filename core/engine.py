"""
游戏引擎：管理关卡数据、玩家进度、解锁逻辑
==========================================
负责把 data/chapters.py 里的关卡数据加载进来，
判断哪些关卡已解锁、是否全部通关等。
"""

from typing import List, Dict, Optional
from .player import Player


class GameEngine:
    """游戏引擎：协调玩家与关卡数据"""

    def __init__(self, levels: List[Dict]):
        """
        参数：
            levels: 关卡数据列表（来自 data/chapters.py）
        """
        self.levels = levels

    # ---------- 关卡查询 ----------
    def get_level(self, index: int) -> Optional[Dict]:
        """根据索引取关卡"""
        if 0 <= index < len(self.levels):
            return self.levels[index]
        return None

    def get_level_by_id(self, level_id: str) -> Optional[Dict]:
        """根据 id 取关卡"""
        for lv in self.levels:
            if lv["id"] == level_id:
                return lv
        return None

    def total_levels(self) -> int:
        return len(self.levels)

    # ---------- 解锁状态 ----------
    def is_locked(self, index: int, player: Player) -> bool:
        """
        关卡是否被锁定
        规则：第 0 关永远解锁；其他关需要前一关已通关
        """
        if index == 0:
            return False
        prev_level = self.get_level(index - 1)
        if prev_level is None:
            return True
        return not player.has_completed(prev_level["id"])

    def is_boss(self, level: Dict) -> bool:
        return level.get("is_boss", False)

    # ---------- 通关判定 ----------
    def is_chapter_completed(self, player: Player) -> bool:
        """当前章节是否全部通关"""
        return all(player.has_completed(lv["id"]) for lv in self.levels)

    def completed_count(self, player: Player) -> int:
        """已通关数量"""
        return sum(1 for lv in self.levels if player.has_completed(lv["id"]))

    # ---------- 奖励结算 ----------
    def settle_reward(self, level: Dict, mode_key: str, player: Player) -> int:
        """
        结算关卡奖励：经验 + 物品
        - 教学模式经验减半
        返回：实际获得的经验值
        """
        base_exp = level["reward_exp"]
        if mode_key == "teach":
            gained = base_exp // 2
        else:
            gained = base_exp

        player.gain_exp(gained)
        player.complete_level(level["id"], level.get("reward_item"))
        player.save()
        return gained

    # ---------- 获取下一关索引 ----------
    def next_level_index(self, current_index: int) -> Optional[int]:
        """获取下一关索引，没有则返回 None"""
        nxt = current_index + 1
        if nxt < len(self.levels):
            return nxt
        return None
