"""
关卡数据：第一章「语法森林」
==========================
每个关卡是一个字典，字段说明：
    id            : 关卡编号（如 "1-1"）
    name          : 关卡名称
    scene         : 场景标题（带 emoji）
    story         : 剧情 NPC 对话
    knowledge     : 知识点列表（战斗前展示）
    monster       : 怪物名称
    monster_hp    : 怪物 HP
    reward_exp    : 奖励经验值（教学模式自动减半）
    reward_item   : 奖励物品
    is_boss       : 是否 BOSS 关
    modes         : 三档难度配置
        - teach      教学模式：照抄
        - fill       填空模式：补全 ___
        - challenge  挑战模式：从零写

每个 mode 包含：
    label        : 显示名
    instruction  : 任务说明
    template     : 代码模板（填空模式的初始内容）
    check_type   : 判定类型（见 core/battle.py）
    expected     : 期望值
    hint         : 提示文字
"""

CHAPTER1_LEVELS = [
    {
        "id": "1-1",
        "name": "变量之泉",
        "scene": "🌲 变量之泉",
        "story": "你来到一汪清泉前，老者说：「勇者，对泉水喊出你的宣言吧！用 print() 把你的话打印到屏幕上。」",
        "knowledge": [
            "print() 是 Python 的输出函数",
            "括号里的内容会被打印到屏幕上",
            '字符串需要用引号 " " 包起来',
        ],
        "monster": "🐍 泉水守卫蛇",
        "monster_hp": 50,
        "reward_exp": 50,
        "reward_item": "🗡️ 木剑",
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "请照抄下面的代码（熟悉手感）：",
                "template": 'print("我是AI勇者，踏上征途！")',
                "check_type": "exact",
                "expected": 'print("我是AI勇者，踏上征途！")',
                "hint": "一字不差地照抄即可",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "把 ___ 替换成你自己的宣言：",
                "template": 'print("___")',
                "check_type": "output_contains",
                "expected": "",
                "hint": '把 ___ 改成任意一句话，比如「我是勇者」',
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": "用 print() 输出任意一句话",
                "template": "",
                "check_type": "output_any",
                "expected": None,
                "hint": '格式：print("你的话")',
            },
        },
    },
    {
        "id": "1-2",
        "name": "数值祭坛",
        "scene": "⛩️ 数值祭坛",
        "story": "祭坛上刻着古老的符文：「勇者，把你的力量存入变量，方能被记住。」",
        "knowledge": [
            "变量就像一个盒子，用来存放数据",
            "赋值用等号：变量名 = 值",
            "变量名只能用字母、数字、下划线，不能数字开头",
        ],
        "monster": "🗿 符文石像",
        "monster_hp": 60,
        "reward_exp": 60,
        "reward_item": "🛡️ 木盾",
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "照抄代码，理解变量赋值：",
                "template": 'hero_name = "勇者"\nprint(hero_name)',
                "check_type": "output_exact",
                "expected": "勇者",
                "hint": "照抄即可",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "创建变量 hp 赋值为 100，并打印它（___ 处填数字）：",
                "template": "hp = ___\nprint(hp)",
                "check_type": "output_exact",
                "expected": "100",
                "hint": "把 ___ 改成 100",
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": "创建一个变量 attack = 10，再 print(attack) 输出它",
                "template": "",
                "check_type": "output_exact",
                "expected": "10",
                "hint": "两行：第一行赋值，第二行打印",
            },
        },
    },
    {
        "id": "1-3",
        "name": "拼接之桥",
        "scene": "🌉 拼接之桥",
        "story": "桥断了，需要用 + 号把两段字符串拼接起来才能通过。",
        "knowledge": [
            "字符串可以用 + 号拼接",
            '变量和字符串也能拼接："你好," + name',
            "数字不能直接和字符串拼接，需要转换",
        ],
        "monster": "🌉 断桥幽灵",
        "monster_hp": 70,
        "reward_exp": 70,
        "reward_item": "⚡ 加速靴",
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "照抄代码，观察字符串拼接：",
                "template": 'name = "勇者"\nprint("你好," + name)',
                "check_type": "output_exact",
                "expected": "你好,勇者",
                "hint": "照抄即可",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "把 ___ 填成变量名 name，完成拼接：",
                "template": 'name = "勇者"\nprint("你好," + ___)',
                "check_type": "output_exact",
                "expected": "你好,勇者",
                "hint": "___ 处填变量名 name（不要加引号）",
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": '创建变量 job = "法师"，用 + 拼接输出「我的职业是法师」',
                "template": "",
                "check_type": "output_exact",
                "expected": "我的职业是法师",
                "hint": 'print("我的职业是" + job)',
            },
        },
    },
    {
        "id": "1-4",
        "name": "条件岔路",
        "scene": "🚦 条件岔路",
        "story": "前方出现两条路，需要用 if-else 判断 HP 值，选择正确的方向。",
        "knowledge": [
            "if 判断条件：条件成立时执行",
            "else：条件不成立时执行",
            "注意冒号 : 和缩进（4 个空格）",
        ],
        "monster": "🚦 岔路守卫",
        "monster_hp": 80,
        "reward_exp": 80,
        "reward_item": "📜 判断卷轴",
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "照抄代码，理解 if-else：",
                "template": 'hp = 50\nif hp > 30:\n    print("存活")\nelse:\n    print("倒下")',
                "check_type": "output_exact",
                "expected": "存活",
                "hint": "注意冒号和 4 个空格缩进",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "把 ___ 填成 >，判断 hp 是否大于 30：",
                "template": 'hp = 50\nif hp ___ 30:\n    print("存活")\nelse:\n    print("倒下")',
                "check_type": "output_exact",
                "expected": "存活",
                "hint": "大于用 > 符号",
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": 'hp = 20，用 if-else 判断：hp > 0 输出「活着」，否则输出「死亡」',
                "template": "",
                "check_type": "output_exact",
                "expected": "活着",
                "hint": 'if hp > 0: print("活着") else: print("死亡")',
            },
        },
    },
    {
        "id": "1-5",
        "name": "循环迷阵",
        "scene": "🌀 循环迷阵",
        "story": "迷宫需要重复攻击 3 次才能打破结界，用 for 循环来实现吧！",
        "knowledge": [
            "for 循环用于重复执行代码",
            "range(3) 表示循环 3 次（0,1,2）",
            "循环体需要缩进 4 个空格",
        ],
        "monster": "🌀 迷阵核心",
        "monster_hp": 90,
        "reward_exp": 90,
        "reward_item": "🔮 法力水晶",
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "照抄代码，理解 for 循环：",
                "template": 'for i in range(3):\n    print("攻击!")',
                "check_type": "output_exact",
                "expected": "攻击!\n攻击!\n攻击!",
                "hint": "range(3) 循环 3 次",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "把 ___ 填成 5，循环攻击 5 次：",
                "template": 'for i in range(___):\n    print("攻击!")',
                "check_type": "output_exact",
                "expected": "攻击!\n攻击!\n攻击!\n攻击!\n攻击!",
                "hint": "循环 5 次用 range(5)",
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": "用 for 循环打印 1 到 5（提示：print(i)）",
                "template": "",
                "check_type": "output_exact",
                "expected": "1\n2\n3\n4\n5",
                "hint": "for i in range(1, 6): print(i)",
            },
        },
    },
    {
        "id": "1-6",
        "name": "BOSS：缩进蛇妖",
        "scene": "🐉 蛇妖巢穴",
        "story": "最终 BOSS 出现！它用乱码污染了勇者的代码，你需要修复这段程序让它正确运行。",
        "knowledge": [
            "综合运用 print、变量、if、for",
            "缩进错误是最常见的 bug",
            "注意中英文符号（冒号、引号）",
        ],
        "monster": "🐉 缩进蛇妖",
        "monster_hp": 150,
        "reward_exp": 200,
        "reward_item": "💎 语法晶石",
        "is_boss": True,
        "modes": {
            "teach": {
                "label": "教学模式",
                "instruction": "这段代码有 2 处错误（缩进 + 缺冒号），照抄正确版本：",
                "template": 'hp = 80\nif hp > 50\n    print("勇者强大")\nfor i in range(2)\n    print("攻击!")',
                "check_type": "boss_fix",
                "expected": 'hp = 80\nif hp > 50:\n    print("勇者强大")\nfor i in range(2):\n    print("攻击!")',
                "hint": "if 和 for 语句末尾都要加冒号 :",
            },
            "fill": {
                "label": "填空模式",
                "instruction": "修复这段代码（共 2 处错误，缺少冒号）：",
                "template": 'hp = 80\nif hp > 50___\n    print("勇者强大")\nfor i in range(2)___\n    print("攻击!")',
                "check_type": "boss_fix",
                "expected": 'hp = 80\nif hp > 50:\n    print("勇者强大")\nfor i in range(2):\n    print("攻击!")',
                "hint": "两个 ___ 处都填冒号 :",
            },
            "challenge": {
                "label": "挑战模式",
                "instruction": '从零写：hp=80，如果 hp>50 输出「强大」，再用 for 循环输出 2 次「攻击!」',
                "template": "",
                "check_type": "output_exact",
                "expected": "强大\n攻击!\n攻击!",
                "hint": "先 if 判断，再 for 循环",
            },
        },
    },
]


def get_all_chapters():
    """获取所有章节关卡数据（目前只有第一章，后续可扩展）"""
    return {
        1: {
            "title": "语法森林",
            "subtitle": "穿越六大关卡，击败 BOSS 缩进蛇妖，收集「语法晶石」",
            "levels": CHAPTER1_LEVELS,
        }
    }
