"""
便捷函数：关卡辅助生成器
========================
每章导入本文件即可快速生成题目配置
"""


def make_mode(instruction, template, check_type, expected, hint):
    """
    快速生成一个难度模式字典
    参数：
        instruction: 任务说明文字
        template:    代码模板（填空/教学的初始代码）
        check_type:  判定类型（exact / output_exact / output_contains
                     / output_any / boss_fix）
        expected:    期望输出（output_exact 时用；其他类型可传 ""）
        hint:        提示文字
    """
    return {
        "label": {"teach": "教学模式", "fill": "填空模式", "challenge": "挑战模式"}.get(
            _infer_mode(template, check_type, expected), "模式"
        ),
        "instruction": instruction,
        "template": template,
        "check_type": check_type,
        "expected": expected,
        "hint": hint,
    }


def _infer_mode(template, check_type, expected):
    """根据模板内容粗略推断模式名"""
    if "___" in template:
        return "fill"
    if check_type == "exact":
        return "teach"
    return "challenge"


# 章节元信息（总览用）
CHAPTER_META = {
    1: {"title": "🌲 语法森林",
        "subtitle": "穿越六大关卡，击败 BOSS 缩进蛇妖，收集「语法晶石」",
        "chinese": "第一章", "emoji": "🌲"},
    2: {"title": "🏔️ 数据矿脉",
        "subtitle": "NumPy/Pandas/Matplotlib 全流程，击败缺失值巨魔",
        "chinese": "第二章", "emoji": "🏔️"},
    3: {"title": "🏰 算法王城",
        "subtitle": "学习经典机器学习算法，击败过拟合之龙",
        "chinese": "第三章", "emoji": "🏰"},
    4: {"title": "🌋 神经网络深渊",
        "subtitle": "PyTorch 深度学习，击败梯度消失恶魔",
        "chinese": "第四章", "emoji": "🌋"},
    5: {"title": "🌌 大模型星界",
        "subtitle": "Transformers/RAG/LangChain/Agent，击败幻觉幽灵",
        "chinese": "第五章", "emoji": "🌌"},
    6: {"title": "🚀 云端天梯",
        "subtitle": "FastAPI/Docker/Gradio 部署，击败 Bugzor 本体",
        "chinese": "第六章", "emoji": "🚀"},
}

# 简写别名
M = make_mode
CHAPTER_M = CHAPTER_META
L = lambda *a, **k: None  # 占位符，未使用
