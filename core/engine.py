"""
游戏引擎：管理多章节关卡数据、玩家进度、解锁逻辑
=================================================
负责：
  · 加载 data/chapters.py 的多章节数据
  · 章节切换（1~6章）
  · 关卡解锁（按章节内的顺序）
  · 奖励结算
"""

from typing import List, Dict, Optional
from .player import Player
from data.chapters import get_all_chapters, CHAPTER_META, get_chapter


class GameEngine:
    """游戏引擎（多章节版）"""

    def __init__(self, chapter_number: int = 1):
        """
        参数：
            chapter_number: 章节号 1~6
        """
        self.chapter_number = chapter_number
        chapter = get_chapter(chapter_number) or get_chapter(1)
        self.levels: List[Dict] = chapter["levels"]
        self.chapter_meta: Dict = chapter

    # ---------- 章节元信息 ----------
    def chapter_title(self) -> str:
        return self.chapter_meta.get("title", "")

    def chapter_subtitle(self) -> str:
        return self.chapter_meta.get("subtitle", "")

    def chapter_emoji(self) -> str:
        return self.chapter_meta.get("emoji", "")

    # ---------- 关卡查询 ----------
    def get_level(self, index: int) -> Optional[Dict]:
        if 0 <= index < len(self.levels):
            return self.levels[index]
        return None

    def get_level_by_id(self, level_id: str) -> Optional[Dict]:
        for lv in self.levels:
            if lv["id"] == level_id:
                return lv
        return None

    def total_levels(self) -> int:
        return len(self.levels)

    # ---------- 解锁状态（本章）----------
    def is_locked(self, index: int, player: Player) -> bool:
        if index == 0:
            return False
        prev = self.get_level(index - 1)
        if prev is None:
            return True
        return not player.has_completed(prev["id"])

    def is_boss(self, level: Dict) -> bool:
        return level.get("is_boss", False)

    def is_skeleton(self, level: Dict) -> bool:
        """是否为骨架关卡（三档题目后续补充）"""
        return level.get("_skeleton", False)

    # ---------- 章节通关判定 ----------
    def is_chapter_completed(self, player: Player) -> bool:
        return all(player.has_completed(lv["id"]) for lv in self.levels)

    def completed_count(self, player: Player) -> int:
        return sum(1 for lv in self.levels if player.has_completed(lv["id"]))

    # ---------- 跨章节进度 ----------
    def total_progress(self, player: Player) -> str:
        """所有章节总进度（X/Y 关）"""
        total = done = 0
        for ch in get_all_chapters().values():
            for lv in ch["levels"]:
                total += 1
                if player.has_completed(lv["id"]):
                    done += 1
        return f"{done}/{total}"

    def total_completed_ratio(self, player: Player) -> float:
        total = done = 0
        for ch in get_all_chapters().values():
            for lv in ch["levels"]:
                total += 1
                if player.has_completed(lv["id"]):
                    done += 1
        return done / total if total else 0.0

    def is_chapter_unlocked(self, chapter: int, player: Player) -> bool:
        """判定某章节是否解锁：第1章默认解锁；其他需通关上一章"""
        if chapter == 1:
            return True
        prev_data = get_chapter(chapter - 1)
        if prev_data is None:
            return False
        return all(player.has_completed(lv["id"]) for lv in prev_data["levels"])

    # ---------- 奖励结算 ----------
    def settle_reward(self, level: Dict, mode_key: str, player: Player) -> int:
        base_exp = level["reward_exp"]
        gained = base_exp // 2 if mode_key == "teach" else base_exp
        player.gain_exp(gained)
        player.complete_level(level["id"], level.get("reward_item"))
        player.save()
        return gained

    # ---------- 下一关 ----------
    def next_level_index(self, current_index: int) -> Optional[int]:
        nxt = current_index + 1
        return nxt if nxt < len(self.levels) else None

    # ---------- 找未通关的下一关 ----------
    def find_next_unlocked_uncompleted(self, player: Player) -> Optional[int]:
        """返回下一个已解锁但未通关的关卡索引"""
        for idx, lv in enumerate(self.levels):
            if (not player.has_completed(lv["id"])
                    and not self.is_locked(idx, player)):
                return idx
        return None


# ---------- 工具 ----------
ALL_CHAPTER_META = CHAPTER_META
TOTAL_CHAPTERS = 6
