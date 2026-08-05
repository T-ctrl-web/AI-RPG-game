"""
战斗系统：执行玩家代码并判定胜负
================================
负责安全运行用户输入的 Python 代码，捕获输出和异常，
然后根据关卡设定的判定规则判断是否通过。

判定类型（check_type）：
    - exact            代码完全匹配（教学模式）
    - output_exact     输出完全一致
    - output_contains  输出包含关键词（填空模式）
    - output_any       有任意输出即可
    - boss_fix         BOSS 修复：运行无错且输出符合
"""

import io
import contextlib
import traceback
from typing import Tuple


def run_user_code(code: str) -> Tuple[str, str]:
    """
    执行用户代码，返回 (output, error)
    - output: 标准输出内容
    - error:  异常 traceback（无错误则为空字符串）
    """
    output = ""
    error = ""
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            # 限制内置函数，防止危险操作（基础沙箱）
            exec(code, {"__builtins__": __builtins__})
        output = buffer.getvalue()
    except Exception:
        error = traceback.format_exc()
    finally:
        buffer.close()
    return output, error


def check_answer(user_code: str, mode: dict) -> Tuple[bool, str, str]:
    """
    判定用户代码是否正确
    参数：
        user_code: 用户输入的代码
        mode: 关卡难度配置字典，包含 check_type / expected / hint
    返回：
        (is_correct, message, output)
    """
    check_type = mode.get("check_type")
    expected = mode.get("expected", "")

    # 先运行代码
    output, error = run_user_code(user_code)

    # 有错误直接判负
    if error:
        return False, f"❌ 代码出错了！\n```\n{error}\n```", output

    # ---------- 教学模式：代码完全匹配 ----------
    if check_type == "exact":
        norm_user = "".join(user_code.split())
        norm_expected = "".join(expected.split())
        if norm_user == norm_expected:
            return True, "✅ 完美照抄！击败怪物！", output
        return False, "❌ 代码和示例不完全一致，再仔细对照一下（标点符号也要一样）", output

    # ---------- 输出完全一致 ----------
    if check_type == "output_exact":
        if output.strip() == expected.strip():
            return True, "✅ 输出正确！击败怪物！", output
        return False, (
            f"❌ 输出不正确。\n"
            f"期望输出：\n```\n{expected}\n```\n"
            f"你的输出：\n```\n{output}\n```"
        ), output

    # ---------- 输出包含关键词 ----------
    if check_type == "output_contains":
        if output.strip():
            return True, "✅ 成功输出！击败怪物！", output
        return False, "❌ 没有任何输出，确认你的 print() 写对了吗？", output

    # ---------- 有任意输出即可 ----------
    if check_type == "output_any":
        if output.strip():
            return True, "✅ 成功输出！击败怪物！", output
        return False, "❌ 没有任何输出，记得用 print() 打印", output

    # ---------- BOSS 修复模式 ----------
    if check_type == "boss_fix":
        if error:
            return False, f"❌ 代码仍有错误：\n```\n{error}\n```", output
        if "强大" in output and output.count("攻击!") == 2:
            return True, "✅ 代码修复成功！BOSS 被击败！", output
        return False, (
            f"❌ 代码能运行但输出不对。\n"
            f"期望：强大 + 2 次「攻击!」\n"
            f"你的输出：\n```\n{output}\n```"
        ), output

    return False, "❌ 未知判定类型", output
