"""
关卡数据：AI 勇者纪元全部 6 章
=================================
说明：本文件包含 6 章完整数据结构（含章节标题、剧情、每关三档难度）。
由于关卡量巨大（113 关），本章以「可执行的模板+数据结构」为主：
  · 第一章：完整可玩（6 关已写全三档判定）
  · 第二章：完整可玩（18 关已写全三档判定）
  · 第三~六章：关卡骨架齐全（场景/怪物/奖励/知识点已写），后续可
    逐步补充每关三档题目代码。
"""

from .helpers import make_mode as _m, CHAPTER_META


# ==============================================================================
# 第一章：语法森林（完整可玩）
# ==============================================================================
CHAPTER1_LEVELS = [
    {
        "id": "1-1", "name": "变量之泉", "scene": "🌲 变量之泉",
        "story": "你来到一汪清泉前，老者说：「勇者，对泉水喊出你的宣言吧！用 print() 把你的话打印到屏幕上。」",
        "knowledge": ["print() 是 Python 的输出函数", "括号里的内容会被打印到屏幕上",
                      '字符串需要用引号 " " 包起来'],
        "monster": "🐍 泉水守卫蛇", "monster_hp": 50, "reward_exp": 50, "reward_item": "🗡️ 木剑",
        "modes": {
            "teach": {"label": "教学模式", "instruction": "请照抄下面的代码（熟悉手感）：",
                      "template": 'print("我是AI勇者，踏上征途！")', "check_type": "exact",
                      "expected": 'print("我是AI勇者，踏上征途！")', "hint": "一字不差地照抄即可"},
            "fill": {"label": "填空模式", "instruction": "把 ___ 替换成你自己的宣言：",
                     "template": 'print("___")', "check_type": "output_any",
                     "expected": "", "hint": '把 ___ 改成任意一句话，比如「我是勇者」'},
            "challenge": {"label": "挑战模式", "instruction": "用 print() 输出任意一句话",
                          "template": "", "check_type": "output_any",
                          "expected": None, "hint": '格式：print("你的话")'},
        },
    },
    {
        "id": "1-2", "name": "数值祭坛", "scene": "⛩️ 数值祭坛",
        "story": "祭坛上刻着古老的符文：「勇者，把你的力量存入变量，方能被记住。」",
        "knowledge": ["变量就像一个盒子，用来存放数据", "赋值用等号：变量名 = 值",
                      "变量名只能用字母、数字、下划线，不能数字开头"],
        "monster": "🗿 符文石像", "monster_hp": 60, "reward_exp": 60, "reward_item": "🛡️ 木盾",
        "modes": {
            "teach": {"label": "教学模式", "instruction": "照抄代码，理解变量赋值：",
                      "template": 'hero_name = "勇者"\nprint(hero_name)', "check_type": "output_exact",
                      "expected": "勇者", "hint": "照抄即可"},
            "fill": {"label": "填空模式", "instruction": "创建变量 hp 赋值为 100，并打印它：",
                     "template": "hp = ___\nprint(hp)", "check_type": "output_exact",
                     "expected": "100", "hint": "把 ___ 改成 100"},
            "challenge": {"label": "挑战模式", "instruction": "创建变量 attack = 10，再 print(attack)",
                          "template": "", "check_type": "output_exact",
                          "expected": "10", "hint": "两行：第一行赋值，第二行打印"},
        },
    },
    {
        "id": "1-3", "name": "拼接之桥", "scene": "🌉 拼接之桥",
        "story": "桥断了，需要用 + 号把两段字符串拼接起来才能通过。",
        "knowledge": ["字符串可以用 + 号拼接",
                      '变量和字符串也能拼接："你好," + name',
                      "数字不能直接和字符串拼接，需要 str() 转换"],
        "monster": "🌉 断桥幽灵", "monster_hp": 70, "reward_exp": 70, "reward_item": "⚡ 加速靴",
        "modes": {
            "teach": {"label": "教学模式", "instruction": "照抄代码，观察字符串拼接：",
                      "template": 'name = "勇者"\nprint("你好," + name)', "check_type": "output_exact",
                      "expected": "你好,勇者", "hint": "照抄即可"},
            "fill": {"label": "填空模式", "instruction": "把 ___ 填成变量名 name：",
                     "template": 'name = "勇者"\nprint("你好," + ___)', "check_type": "output_exact",
                     "expected": "你好,勇者", "hint": "___ 填变量名 name"},
            "challenge": {"label": "挑战模式",
                          "instruction": '创建变量 job = "法师"，输出「我的职业是法师」',
                          "template": "", "check_type": "output_exact",
                          "expected": "我的职业是法师", "hint": 'print("我的职业是" + job)'},
        },
    },
    {
        "id": "1-4", "name": "条件岔路", "scene": "🚦 条件岔路",
        "story": "前方出现两条路，需要用 if-else 判断 HP 值，选择正确的方向。",
        "knowledge": ["if 判断条件：条件成立时执行", "else：条件不成立时执行",
                      "注意冒号 : 和缩进（4 个空格）"],
        "monster": "🚦 岔路守卫", "monster_hp": 80, "reward_exp": 80, "reward_item": "📜 判断卷轴",
        "modes": {
            "teach": {"label": "教学模式", "instruction": "照抄代码，理解 if-else：",
                      "template": 'hp = 50\nif hp > 30:\n    print("存活")\nelse:\n    print("倒下")',
                      "check_type": "output_exact", "expected": "存活",
                      "hint": "注意冒号和 4 空格缩进"},
            "fill": {"label": "填空模式", "instruction": "把 ___ 填成 >：",
                     "template": 'hp = 50\nif hp ___ 30:\n    print("存活")\nelse:\n    print("倒下")',
                     "check_type": "output_exact", "expected": "存活", "hint": "大于用 >"},
            "challenge": {"label": "挑战模式",
                          "instruction": 'hp = 20，用 if-else：hp>0 输出「活着」否则「死亡」',
                          "template": "", "check_type": "output_exact", "expected": "活着",
                          "hint": 'if hp > 0: print("活着") else: print("死亡")'},
        },
    },
    {
        "id": "1-5", "name": "循环迷阵", "scene": "🌀 循环迷阵",
        "story": "迷宫需要重复攻击 3 次才能打破结界，用 for 循环实现吧！",
        "knowledge": ["for 循环用于重复执行代码", "range(3) 表示循环 3 次",
                      "循环体需要缩进 4 个空格"],
        "monster": "🌀 迷阵核心", "monster_hp": 90, "reward_exp": 90, "reward_item": "🔮 法力水晶",
        "modes": {
            "teach": {"label": "教学模式", "instruction": "照抄代码，理解 for 循环：",
                      "template": 'for i in range(3):\n    print("攻击!")',
                      "check_type": "output_exact",
                      "expected": "攻击!\n攻击!\n攻击!", "hint": "range(3) 循环 3 次"},
            "fill": {"label": "填空模式", "instruction": "把 ___ 填成 5，循环 5 次：",
                     "template": 'for i in range(___):\n    print("攻击!")',
                     "check_type": "output_exact",
                     "expected": "攻击!\n攻击!\n攻击!\n攻击!\n攻击!",
                     "hint": "循环 5 次用 range(5)"},
            "challenge": {"label": "挑战模式", "instruction": "用 for 循环打印 1 到 5",
                          "template": "", "check_type": "output_exact",
                          "expected": "1\n2\n3\n4\n5",
                          "hint": "for i in range(1, 6): print(i)"},
        },
    },
    {
        "id": "1-6", "name": "BOSS：缩进蛇妖", "scene": "🐉 蛇妖巢穴",
        "story": "最终 BOSS！它用乱码污染了代码，你需要修复这段程序。",
        "knowledge": ["综合运用 print、变量、if、for", "缩进错误是最常见的 bug",
                      "注意中英文符号（冒号、引号）"],
        "monster": "🐉 缩进蛇妖", "monster_hp": 150, "reward_exp": 200, "reward_item": "💎 语法晶石",
        "is_boss": True,
        "modes": {
            "teach": {"label": "教学模式", "instruction": "照抄正确版本：",
                      "template": 'hp = 80\nif hp > 50:\n    print("勇者强大")\nfor i in range(2):\n    print("攻击!")',
                      "check_type": "boss_fix",
                      "expected": 'hp = 80\nif hp > 50:\n    print("勇者强大")\nfor i in range(2):\n    print("攻击!")',
                      "hint": "if 和 for 后面都加冒号 :"},
            "fill": {"label": "填空模式", "instruction": "两个 ___ 都填冒号：",
                     "template": 'hp = 80\nif hp > 50___\n    print("勇者强大")\nfor i in range(2)___\n    print("攻击!")',
                     "check_type": "boss_fix",
                     "expected": 'hp = 80\nif hp > 50:\n    print("勇者强大")\nfor i in range(2):\n    print("攻击!")',
                     "hint": "填冒号 :"},
            "challenge": {"label": "挑战模式",
                          "instruction": 'hp=80，hp>50 输出「强大」，for 循环输出 2 次「攻击!」',
                          "template": "", "check_type": "output_exact",
                          "expected": "强大\n攻击!\n攻击!",
                          "hint": "先 if 判断，再 for 循环"},
        },
    },
]


# ==============================================================================
# 第二章：数据矿脉（完整可玩，18 关）
# ==============================================================================
def _chapter2_levels():
    """第二关数据，调用返回列表"""
    lv = []
    add = lv.append

    def _(id, name, scene, story, know, mon, mh, exp, item,
          teach_c, teach_t, teach_expected,
          fill_c, fill_t, fill_expected,
          challenge_instruction, challenge_expected,
          is_boss=False):
        """批量构造关卡。
        teach_expected / fill_expected / challenge_expected:
            传字符串 => output_exact
            传 "output_any" => output_any
            传 "output_contains" => output_contains
        """
        def _mode(template, instruction, expected_str, hint):
            if expected_str == "output_any":
                ct, exp = "output_any", ""
            elif expected_str == "output_contains":
                ct, exp = "output_contains", ""
            else:
                ct, exp = "output_exact", expected_str
            return {"label": "", "instruction": instruction, "template": template,
                    "check_type": ct, "expected": exp, "hint": hint}
        modes = {
            "teach": _mode(teach_c, teach_t, teach_expected, "照抄即可"),
            "fill": _mode(fill_c, fill_t, fill_expected, "把 ___ 填好"),
            "challenge": _mode("", challenge_instruction, challenge_expected,
                               "参考教学模式的写法，自己写出来"),
        }
        modes["teach"]["label"] = "教学模式"
        modes["fill"]["label"] = "填空模式"
        modes["challenge"]["label"] = "挑战模式"
        add({"id": id, "name": name, "scene": scene, "story": story, "knowledge": know,
             "monster": mon, "monster_hp": mh, "reward_exp": exp, "reward_item": item,
             "is_boss": is_boss, "modes": modes})

    # 2-1
    _("2-1", "NumPy 采石场", "⛏️ NumPy 采石场",
      "矿工带你走进矿山入口，老矿工：「勇者，用 np.array() 开采第一块数据矿石吧！」",
      ["NumPy 是科学计算基础库", "np.array(列表) 创建数组", "数组运算比列表快"],
      "⛏️ 矿石哥布林", 100, 80, "🪨 NumPy 镐头",
      'import numpy as np\narr = np.array([1, 2, 3])\nprint(arr)', "照抄：创建数组并打印", "[1 2 3]",
      'import numpy as np\narr = ___([1, 2, 3])\nprint(arr)', "把 ___ 填成 np.array", "[1 2 3]",
      "用 NumPy 创建数组 [4,5,6] 并打印", "[4 5 6]")
    # 2-2
    _("2-2", "矩阵运算矿洞", "💠 矩阵运算矿洞",
      "矿洞深处闪烁着矩阵能量，需要 reshape 形状。",
      ["reshape(a,b) 改形状", "广播机制：不同形状可运算", "+-*/ 运算都支持"],
      "💠 矩阵幽灵", 110, 90, "📐 矩阵罗盘",
      'import numpy as np\narr = np.array([1,2,3,4]).reshape(2,2)\nprint(arr.sum())',
      "照抄：reshape 2x2 求和", "10",
      'import numpy as np\narr = np.array([1,2,3,4]).___\nprint(arr.sum())',
      "___ 填 reshape(2,2)", "10",
      "创建 [10,20,30,40] reshape 2x2 求和", "100")
    # 2-3
    _("2-3", "聚合神殿", "🏛️ 聚合神殿",
      "神殿里刻着聚合魔法：让一堆数变成一个数。",
      [".sum() 求和", ".mean() 平均", ".max() 最大"],
      "🏛️ 聚合神官", 120, 100, "🎯 聚合宝石",
      'import numpy as np\narr = np.array([2,4,6,8,10])\nprint(arr.mean())', "照抄：求均值", "6.0",
      'import numpy as np\narr = np.array([2,4,6,8,10])\nprint(arr.___)', "___ 填 mean()", "6.0",
      "数组 [3,7,2,9,5] 打印最大值", "9")
    # 2-4
    _("2-4", "索引迷宫", "🌀 索引迷宫",
      "迷宫里用索引找到宝藏数组的部分。",
      ["arr[0] 第一个", "arr[a:b] 切片", "布尔索引 arr[arr>3]"],
      "🌀 迷宫守门人", 130, 110, "🗺️ 索引地图",
      'import numpy as np\narr = np.array([10,20,30,40])\nprint(arr[1])',
      "照抄：取第 2 个元素", "20",
      'import numpy as np\narr = np.array([10,20,30])\nprint(arr[___])', "___ 填 :2 取前两个", "[10 20]",
      "数组 [5,15,25,35] 切片取后两个", "[25 35]")
    # 2-5
    _("2-5", "线性代数秘境", "📐 线性代数秘境",
      "秘境中藏着矩阵乘法。",
      ["np.dot() 点乘", "矩阵形状要匹配", "@ 也能点乘"],
      "📐 线代巫师", 140, 120, "🧮 线代算盘",
      'import numpy as np\na = np.array([1,2])\nb = np.array([3,4])\nprint(np.dot(a,b))',
      "照抄：向量点积", "11",
      'import numpy as np\na = np.array([1,2])\nb = np.array([3,4])\nprint(___(a,b))',
      "___ 填 np.dot", "11",
      "[1,2,3]·[4,5,6] 点积", "32")
    # 2-6
    _("2-6", "DataFrame 提炼厂", "🏭 DataFrame 提炼厂",
      "工厂把原始数据变成结构化表格。",
      ["pd.DataFrame(字典)", ".head() 看前几行", ".info() 信息"],
      "🏭 提炼厂守卫", 150, 130, "📊 Pandas 筛子",
      'import pandas as pd\ndf = pd.DataFrame({"n":["A","B"],"a":[20,25]})\nprint(df.shape)',
      "照抄：创建 DataFrame 打印形状", "(2, 2)",
      'import pandas as pd\ndf = pd.___({"n":["A","B"],"a":[20,25]})\nprint(df.shape)',
      "___ 填 DataFrame", "(2, 2)",
      "创建两列 DataFrame 打印行数", "2")
    # 2-7
    _("2-7", "列操作工坊", "🔨 列操作工坊",
      "工坊里加工某列或新增列。",
      ["df['列'] 取列", "df['新列']=新增", ".apply() 批量处理"],
      "🔨 列工匠", 160, 140, "🪜 列操作梯",
      'import pandas as pd\ndf = pd.DataFrame({"a":[1,2],"b":[3,4]})\ndf["c"]=df["a"]+df["b"]\nprint(df["c"].sum())',
      "照抄：新增 c=a+b，求和", "10",
      'import pandas as pd\ndf = pd.DataFrame({"a":[1,2],"b":[3,4]})\ndf[___]=df["a"]+df["b"]\nprint(df[___].sum())',
      "两处 ___ 都填 c", "10",
      "a=[1,2], b=[3,4]，新增 c=a+b 打印 c 的和", "10")
    # 2-8
    _("2-8", "筛选之门", "🚪 筛选之门",
      "门神只让符合条件的行通过。",
      ["df[df['列']>X]", ".query() 字符串条件", ".loc/.iloc 定位"],
      "🚪 筛选门神", 170, 150, "🔍 筛选放大镜",
      'import pandas as pd\ndf = pd.DataFrame({"age":[20,25,30]})\nprint(len(df[df["age"]>22]))',
      "照抄：筛选年龄>22 行数", "2",
      'import pandas as pd\ndf = pd.DataFrame({"age":[20,25]})\nprint(len(df[df["age"]___22]))',
      "___ 填 >", "1",
      "age=[18,22,30]，筛 age>=22 打印行数", "2")
    # 2-9
    _("2-9", "分组竞技场", "⚔️ 分组竞技场",
      "竞技场内按类别分组再统计。",
      [".groupby() 分组", ".agg() 聚合", "pd.pivot_table 透视表"],
      "⚔️ 分组骑士", 180, 160, "🏆 分组奖杯",
      'import pandas as pd\ndf = pd.DataFrame({"t":["X","X","Y"],"s":[80,90,70]})\nprint(int(df.groupby("t").sum().loc["X"]))',
      "照抄：按 t 分组求 X 队总分", "170",
      'import pandas as pd\ndf = pd.DataFrame({"t":["X","Y"],"s":[80,90]})\nprint(int(df.___("t").sum().loc["Y"]))',
      "___ 填 groupby", "90",
      "t=[A,B,A], s=[60,80,90]，按 t 分组求 s 最大值打印 A 组", "90")
    # 2-10
    _("2-10", "合并之桥", "🌉 合并之桥",
      "两座表格要合并成一张。",
      ["pd.merge(df1, df2, on='键')", "pd.concat 堆叠", "内连接 inner"],
      "🌉 合并守桥人", 190, 170, "🔗 合并锁链",
      'import pandas as pd\na = pd.DataFrame({"id":[1,2],"n":["A","B"]})\nb = pd.DataFrame({"id":[1,2],"a":[20,25]})\nprint(len(pd.merge(a,b,on="id")))',
      "照抄：merge 后行数", "2",
      'import pandas as pd\na = pd.DataFrame({"id":[1,2],"n":["A","B"]})\nb = pd.DataFrame({"id":[1,2],"a":[20,25]})\nprint(len(pd.___(a,b,on="id")))',
      "___ 填 merge", "2",
      "创建两个 df 共 id 列并 merge，打印合并后的行数", "2")
    # 2-11
    _("2-11", "清洗熔炉", "🔥 清洗熔炉",
      "熔炉清除缺失值和重复值。",
      [".dropna() 删除缺失", ".fillna(V) 填充", ".drop_duplicates() 去重"],
      "🔥 熔炉火元素", 200, 180, "🧹 清洗扫帚",
      'import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({"h":[100,None,80]})\nprint(int(df.fillna(0)["h"].sum()))',
      "照抄：NaN 填 0 后求和", "180",
      'import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({"h":[100,None,80]})\nprint(int(df.___(0)["h"].sum()))',
      "___ 填 fillna", "180",
      "列 [1,None,3]，删除 NaN 行，打印行数", "2")
    # 2-12
    _("2-12", "数据类型熔炉", "🏭 数据类型锻造",
      "工厂把错误的类型改成正确的。",
      [".astype() 转换", "pd.to_datetime 转日期", "astype('category')"],
      "🏭 类型工匠", 210, 190, "🔧 类型扳手",
      'import pandas as pd\ndf = pd.DataFrame({"age":["20","25"]})\ndf["age"]=df["age"].astype(int)\nprint(df["age"].sum())',
      "照抄：字符串数字转 int 求和", "45",
      'import pandas as pd\ndf = pd.DataFrame({"age":["20","25"]})\ndf["age"]=df["age"].___(int)\nprint(df["age"].sum())',
      "___ 填 astype", "45",
      "列 ['1','2','3'] 转 int 求和", "6")
    # 2-13
    _("2-13", "Matplotlib 瞭望塔", "🗼 Matplotlib 瞭望塔",
      "塔上画折线图看清走势。",
      ["plt.plot() 折线", "plt.bar() 柱状", "plt.savefig() 存图"],
      "🗼 瞭望塔守护者", 220, 200, "🔭 可视化望远镜",
      'import matplotlib;matplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nplt.plot([1,2,3],[1,4,9])\nplt.savefig("c.png")\nprint("OK")',
      "照抄：画折线图保存", "OK",
      'import matplotlib;matplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nplt.___([1,2,3],[1,4,9])\nplt.savefig("c.png")\nprint("OK")',
      "___ 填 plot", "OK",
      "画任意折线图保存后打印 OK", "OK")
    # 2-14
    _("2-14", "Seaborn 花园", "🌸 Seaborn 花园",
      "花园里用 Seaborn 画漂亮图。",
      ["sns.heatmap() 热力图", "sns.histplot() 分布", "基于 matplotlib"],
      "🌸 花园精灵", 230, 210, "🎨 Seaborn 画笔",
      'import matplotlib,seaborn as sns;matplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nsns.histplot([1,1,2,2,3,3,3])\nplt.savefig("s.png")\nprint("OK")',
      "照抄：画分布图保存", "OK",
      'import matplotlib,seaborn as sns;matplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nsns.___([1,2,2,3,3])\nplt.savefig("s.png")\nprint("OK")',
      "___ 填 histplot", "OK",
      "画分布图保存后打印 OK", "OK")
    # 2-15
    _("2-15", "时间序列遗迹", "⏰ 时间序列遗迹",
      "遗迹里处理日期时间。",
      ["pd.to_datetime()", ".resample() 重采样", ".rolling() 移动窗口"],
      "⏰ 时间守护", 240, 220, "⌛ 时间沙漏",
      'import pandas as pd\ndf = pd.DataFrame({"d":["2024-01-01","2024-01-02"]})\ndf["d"]=pd.to_datetime(df["d"])\nprint(str(df["d"].dtype)[:7])',
      "照抄：字符串转日期", "datetime",
      'import pandas as pd\ndf = pd.DataFrame({"d":["2024-01-01"]})\ndf["d"]=pd.___(df["d"])\nprint(str(df["d"].dtype)[:7])',
      "___ 填 to_datetime", "datetime",
      "把字符串日期列转 datetime，打印 dtype 前 8 个字符", "datetime")
    # 2-16
    _("2-16", "数据管道工坊", "🔧 数据管道工坊",
      "大师用链式操作处理数据。",
      [".pipe(函数) 链式", ".query() 字符串", ".isin() 筛选"],
      "🔧 管道大师", 250, 230, "🚰 管道阀门",
      'import pandas as pd\ndef f(x): return x+1\ndf = pd.DataFrame({"a":[1,2,3]})\nprint(int(df.pipe(f)["a"].sum()))',
      "照抄：pipe 加一求和", "9",
      'import pandas as pd\ndef f(x): return x+1\ndf = pd.DataFrame({"a":[1,2,3]})\nprint(int(df.___(f)["a"].sum()))',
      "___ 填 pipe", "9",
      "定义加一函数，df pipe 后求和", "9")
    # 2-17
    _("2-17", "Jupyter 秘境（隐藏关）", "📓 Jupyter 法典",
      "秘境里藏着 Jupyter 的使用秘籍。",
      ["%timeit 测速", "Shift+Enter 运行", "?函数 查文档"],
      "📓 Jupyter 精灵", 260, 250, "🌌 Jupyter 法典",
      'import time\ns=time.time();sum(range(1000));print("OK")',
      "照抄：模拟测速后打印 OK", "OK",
      'import time\ns=___;sum(range(1000));print("OK")',
      "___ 填 time.time()", "OK",
      "time 模块运行一段循环，打印 OK", "OK")
    # 2-18 BOSS
    _("2-18", "BOSS：缺失值巨魔", "👹 缺失值巨魔巢穴",
      "巨魔污染了交易数据，清洗后再做汇总分析！",
      ["综合清洗+聚合", "缺失值填充", "分组汇总"],
      "👹 缺失值巨魔", 400, 500, "💎 数据晶石",
      'import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({"s":[100,None,200,300,None]})\nprint(int(df.fillna(0)["s"].sum()))',
      "照抄：填 0 求和", "600",
      'import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({"s":[100,None,200,300,None]})\nprint(int(df.___(0)["s"].sum()))',
      "___ 填 fillna", "600",
      'sale 列 [50,None,150,100]，填 0 后打印总和', "300",
      is_boss=True)
    return lv


# ==============================================================================
# 第三~六章：关卡骨架齐全（场景/怪物/奖励/知识点已完整；三档题目后续补充）
# ==============================================================================
def _chapter3_levels():
    """第三章：算法王城（20 关）—— 关卡骨架"""
    levels = [
        ("3-1", "线性回归骑士", "📈 线性回归骑士",
         "骑士教你用直线预测房价。",
         ["LinearRegression.fit/predict", "MSE/R2 评估", "train_test_split"],
         "⚔️ 回归骑士", 180, 140, "📈 回归长剑"),
        ("3-2", "评估竞技场", "🏟️ 评估竞技场",
         "评判模型优劣的竞技场。",
         ["MSE/MAE/R²", "训练/测试集划分", "过拟合概念"],
         "🏟️ 评估裁判", 190, 150, "📏 评估量尺"),
        ("3-3", "正则化神殿", "🛕 正则化神殿",
         "神殿内教你如何对抗过拟合。",
         ["Ridge 岭回归", "Lasso L1 正则", "超参数 α"],
         "🛕 正则神官", 200, 160, "⚖️ 正则天平"),
        ("3-4", "多项式回归秘境", "🎢 多项式滑道",
         "学习非线性拟合。",
         ["PolynomialFeatures", "欠拟合 vs 过拟合",
          "degree 调节复杂度"],
         "🌀 多项式巫师", 210, 170, "🎢 多项式滑道"),
        ("3-5", "逻辑回归法师", "🔮 逻辑回归法师",
         "法师画出决策边界。",
         ["LogisticRegression", "predict_proba 概率", "决策边界"],
         "🔮 逻辑法师", 220, 180, "🎴 概率卡牌"),
        ("3-6", "KNN 游侠", "🏹 KNN 游侠",
         "游侠靠邻居判断种类。",
         ["KNeighborsClassifier", "距离度量", "K 值选择"],
         "🏹 KNN 游侠", 230, 190, "🎯 KNN 飞镖"),
        ("3-7", "决策树游侠", "🌳 决策树精",
         "精怪用分支问答判断。",
         ["DecisionTreeClassifier", "熵/基尼系数", "max_depth 参数"],
         "🌳 决策树精", 240, 200, "🌿 决策树叶"),
        ("3-8", "随机森林军团", "🌲 森林领主",
         "军团投票决策：多棵树组合。",
         ["RandomForest", "bagging", "feature_importances_"],
         "🌲 森林领主", 250, 210, "🍂 森林之心"),
        ("3-9", "SVM 剑圣", "⚡ SVM 剑圣",
         "剑圣画出最优分界线。",
         ["SVC/SVR", "核函数 rbf", "C 与 gamma"],
         "⚡ SVM 剑圣", 260, 220, "🗡️ 向量之刃"),
        ("3-10", "K-Means 谜题", "🔵 聚类核心",
         "给怪物自动分类，不需要标签。",
         ["KMeans 聚类", "肘部法则选 K", "轮廓系数"],
         "🔵 聚类核心", 270, 230, "🎯 聚类宝石"),
        ("3-11", "层次聚类之树", "🌳 层次树精",
         "树形聚类，一步一步合并。",
         ["AgglomerativeClustering", "树状图", "Ward/Complete"],
         "🌳 层次树精", 280, 240, "🌿 层次之叶"),
        ("3-12", "降维秘境", "🌀 降维巫师",
         "把高维数据压缩到 2D 可视化。",
         ["PCA 主成分", "t-SNE 可视化", "方差解释率"],
         "🌀 降维巫师", 290, 250, "📐 降维罗盘"),
        ("3-13", "异常检测哨所", "🛰️ 哨所指挥官",
         "哨所专门抓异常数据。",
         ["IsolationForest", "LOF 离群因子", "异常分数"],
         "🛰️ 哨所指挥官", 300, 260, "🚨 异常雷达"),
        ("3-14", "特征工程熔炉", "🔥 特征大师",
         "大师把原始数据炼成好特征。",
         ["OneHot/Label 编码", "StandardScaler 标准化", "Polynomial 特征"],
         "🔥 特征大师", 310, 270, "⚒️ 特征锤"),
        ("3-15", "数据预处理工坊", "🔧 预处理工匠",
         "Pipeline 把所有步骤串起来。",
         ["Pipeline 管道", "ColumnTransformer",
          "SimpleImputer 填补"],
         "🔧 预处理工匠", 320, 280, "🏗️ 管道蓝图"),
        ("3-16", "交叉验证圣坛", "⛪ 圣坛祭司",
         "更可靠的评估方法。",
         ["KFold", "cross_val_score", "stratified 分层"],
         "⛪ 圣坛祭司", 330, 290, "🎰 调参骰子"),
        ("3-17", "评估矩阵宝库", "💎 矩阵守护",
         "全指标评估分类模型。",
         ["混淆矩阵", "ROC/AUC", "Precision/Recall/F1"],
         "💎 矩阵守护", 340, 300, "📊 评估宝典"),
        ("3-18", "超参调优圣坛", "🎰 调优神官",
         "自动搜索最优超参数。",
         ["GridSearchCV", "RandomizedSearchCV",
          "贝叶斯优化"],
         "🎰 调优神官", 350, 310, "🎲 调优骰盅"),
        ("3-19", "推荐系统秘境（隐藏关）", "🤖 推荐大师",
         "学习怎么给用户推荐物品。",
         ["协同过滤 CF", "内容推荐", "混合推荐"],
         "🤖 推荐大师", 360, 320, "🎁 推荐引擎"),
        ("3-20", "BOSS：过拟合之龙", "🐉 过拟合之龙巢穴",
         "恶龙训练集无敌，测试集却一败涂地！",
         ["端到端 ML 项目", "解决过拟合", "多个模型对比"],
         "🐉 过拟合之龙", 600, 600, "💎 算法晶石", True),
    ]
    return [_skeleton(l) for l in levels]


def _chapter4_levels():
    """第四章：神经网络深渊（18 关）"""
    levels = [
        ("4-1", "张量之泉", "💧 张量水灵",
         "PyTorch 的最基本单位：张量。",
         ["torch.Tensor", "dtype/shape", ".to(device)"],
         "💧 张量水灵", 200, 180, "⚙️ 张量齿轮"),
        ("4-2", "自动微分秘境", "🔄 梯度精灵",
         "反向传播的核心：自动微分。",
         ["requires_grad", "loss.backward()", "计算图"],
         "🔄 梯度精灵", 210, 190, "🪡 微分针"),
        ("4-3", "全连接地层", "🧱 地基石人",
         "最简单的网络：线性层+激活。",
         ["nn.Linear", "nn.ReLU", "forward()"],
         "🧱 地基石人", 220, 200, "🏗️ 网络蓝图"),
        ("4-4", "损失函数神殿", "🛕 损失神官",
         "选对损失函数才能训练。",
         ["MSELoss", "CrossEntropyLoss", "损失曲线"],
         "🛕 损失神官", 230, 210, "⚖️ 损失天平"),
        ("4-5", "训练循环工坊", "🔨 训练工匠",
         "固定套路：前向→损失→反向→更新。",
         ["optimizer.zero_grad()", "loss.backward()", "step()"],
         "🔨 训练工匠", 240, 220, "🔁 训练齿轮"),
        ("4-6", "优化器神殿", "⚡ 优化神官",
         "好的优化器让网络学得更快。",
         ["SGD/Momentum", "Adam", "学习率调度"],
         "⚡ 优化神官", 250, 230, "🎯 优化箭矢"),
        ("4-7", "正则化圣坛", "⛪ 正则祭司",
         "深层网络防过拟合。",
         ["Dropout", "BatchNorm", "权重衰减"],
         "⛪ 正则祭司", 260, 240, "🛡️ 正则盾牌"),
        ("4-8", "数据加载驿站", "🐎 驿站骑士",
         "数据怎么高效率喂给网络。",
         ["Dataset/ __getitem__", "DataLoader/batch",
          "transforms 数据增强"],
         "🐎 驿站骑士", 270, 250, "📦 数据马鞍"),
        ("4-9", "CNN 视觉之眼", "👁️ 视觉守卫",
         "赋予模型识别图片的能力。",
         ["nn.Conv2d", "MaxPool2d", "感受野"],
         "👁️ 视觉守卫", 280, 260, "🔍 视觉之眼"),
        ("4-10", "ResNet 神殿", "🛕 残差神官",
         "让深层网络训练不再难：残差连接。",
         ["ResBlock", "skip connection", "深层训练稳定"],
         "🛕 残差神官", 290, 270, "🌟 残差星徽"),
        ("4-11", "RNN 记忆长河", "🌊 记忆水妖",
         "处理序列数据的记忆网络。",
         ["nn.RNN/LSTM/GRU", "hidden state",
          "seq2seq 思想"],
         "🌊 记忆水妖", 300, 280, "🌀 记忆水晶"),
        ("4-12", "Transformer 神殿", "🛕 注意力神像",
         "当今大模型的基石。",
         ["Self-Attention", "MultiheadAttention",
          "Positional Encoding"],
         "🛕 注意力神像", 310, 290, "🌟 注意力权杖"),
        ("4-13", "迁移学习工坊", "🔄 迁移大师",
         "拿别人预训练好的模型改一改就用。",
         ["pretrained=True", "freeze/解冻", "微调全连接层"],
         "🔄 迁移大师", 320, 300, "🦋 迁移翅膀"),
        ("4-14", "生成对抗秘境", "🎭 GAN 双子",
         "互相博弈的生成器和判别器。",
         ["Generator/Discriminator", "对抗训练", "WGAN/StyleGAN"],
         "🎭 GAN 双子", 330, 310, "🎨 生成画笔"),
        ("4-15", "目标检测竞技场", "🎯 检测猎手",
         "找出图中物体的位置和类别。",
         ["bounding box", "IoU", "mAP/YOLO"],
         "🎯 检测猎手", 340, 320, "📐 检测框尺"),
        ("4-16", "模型可解释性（隐藏关）", "🔮 解释先知",
         "让网络告诉你它为什么这么判。",
         ["Grad-CAM", "SHAP 值", "注意力可视化"],
         "🔮 解释先知", 350, 330, "💡 解释明灯"),
        ("4-17", "论文复现秘境（隐藏关）", "📜 论文贤者",
         "读经典论文，复现核心代码。",
         ["AlexNet/VGG/ViT", "代码结构设计",
          "训练稳定性技巧"],
         "📜 论文贤者", 360, 340, "📚 复现宝典"),
        ("4-18", "BOSS：梯度消失恶魔", "😈 梯度消失恶魔巢穴",
         "深层网络的梯度越来越小，无法学习！",
         ["自定义深层架构", "BatchNorm/残差",
          "梯度裁剪"],
         "😈 梯度消失恶魔", 700, 700, "💎 深度晶石", True),
    ]
    return [_skeleton(l) for l in levels]


def _chapter5_levels():
    """第五章：大模型星界（22 关）"""
    levels = [
        ("5-1", "Prompt 咒语学院", "📖 咒语教授",
         "教你怎么写提示词让 AI 听懂。",
         ["Zero-shot 零样本", "角色设定 System Prompt", "清晰指令"],
         "📖 咒语教授", 240, 240, "📜 咒语书"),
        ("5-2", "Few-shot 竞技场", "🏟️ 竞技斗士",
         "给几个例子让 AI 照葫芦画瓢。",
         ["Few-shot 示例", "CoT 思维链", "自一致性"],
         "🏟️ 竞技斗士", 250, 250, "🎴 样本卡牌"),
        ("5-3", "Prompt 模板工坊", "🔧 模板工匠",
         "把提示词做成模板，变量替换。",
         ["模板变量占位符", "输出 JSON 格式", "结构化输出"],
         "🔧 模板工匠", 260, 260, "📋 模板印章"),
        ("5-4", "Transformers 神殿", "🛕 模型神官",
         "HuggingFace 生态入门。",
         ["pipeline() 一键调用", "AutoModel/AutoTokenizer",
          "from_pretrained 加载模型"],
         "🛕 模型神官", 270, 270, "🤗 HF 徽章"),
        ("5-5", "Embedding 向量星座", "⭐ 星座守卫",
         "把文字变成向量，就能算相似性。",
         ["SentenceTransformer", "余弦相似度",
          "向量空间语义近邻"],
         "⭐ 星座守卫", 280, 280, "✨ 向量星图"),
        ("5-6", "开源模型动物园", "🦁 模型驯兽师",
         "认识常见开源大模型。",
         ["Qwen/Llama/ChatGLM", "本地推理",
          "int4/8 量化推理"],
         "🦁 模型驯兽师", 290, 290, "🏞️ 模型图鉴"),
        ("5-7", "文档加载驿站", "📄 文档守卫",
         "怎么把 PDF/Markdown 导入系统。",
         ["PDF 解析", "文本分块 chunking",
          "Markdown/HTML 加载"],
         "📄 文档守卫", 300, 300, "📚 文档背包"),
        ("5-8", "Chroma 图书馆", "📚 图书馆长",
         "轻量级向量数据库：Chroma。",
         ["chromadb Collection", "add() 存储",
          "query() 相似度检索"],
         "📚 图书馆长", 310, 310, "🗄️ Chroma 书架"),
        ("5-9", "FAISS 向量矩阵", "🔢 FAISS 守卫",
         "Facebook 的高性能向量库。",
         ["IndexFlatL2", "IndexIVFFlat 加速",
          "批量检索"],
         "🔢 FAISS 守卫", 320, 320, "🧮 FAISS 矩阵"),
        ("5-10", "Milvus 星界仓库（隐藏关）", "🌌 Milvus 守护",
         "分布式向量数据库，生产级。",
         ["pymilvus Collection", "索引类型 IVF/HNSW",
          "分布式存储"],
         "🌌 Milvus 守护", 330, 330, "🌠 Milvus 星舰"),
        ("5-11", "RAG 图书馆", "📖 知识守护",
         "检索+生成 = 让 LLM 回答你的私有文档。",
         ["Retrieve 检索 TopK", "上下文拼接",
          "来源引用 citation"],
         "📖 知识守护", 340, 340, "🔍 RAG 放大镜"),
        ("5-12", "LangChain 工坊", "🔨 工坊大师",
         "LangChain 把各种组件串起来。",
         ["LLMChain", "PromptTemplate",
          "OutputParser 解析结果"],
         "🔨 工坊大师", 350, 350, "⛓️ 链条核心"),
        ("5-13", "Memory 记忆神殿", "🧠 记忆神官",
         "让对话记得历史：短/长/摘要记忆。",
         ["BufferMemory", "ConversationSummaryMemory",
          "窗口记忆"],
         "🧠 记忆神官", 360, 360, "💭 记忆项链"),
        ("5-14", "LlamaIndex 神殿", "🦙 Llama 神官",
         "LlamaIndex 文档向量化+查询全栈。",
         ["ServiceContext", "VectorStoreIndex",
          "as_query_engine()"],
         "🦙 Llama 神官", 370, 370, "🌳 Llama 神树"),
        ("5-15", "高级 RAG 工坊", "🔧 RAG 大师",
         "优化 RAG 效果：重排序/改查/分块策略。",
         ["Reranker 重排序", "QueryTransform",
          "Parent-Child 分块"],
         "🔧 RAG 大师", 380, 380, "⚙️ RAG 引擎"),
        ("5-16", "Tool 工具集市", "🛒 工具商人",
         "给 Agent 装备各种工具函数。",
         ["@tool 装饰器", "结构化参数",
          "Function Calling"],
         "🛒 工具商人", 390, 390, "🧰 工具箱"),
        ("5-17", "Agent 召唤祭坛", "🤖 Agent 召唤师",
         "让模型自己思考用什么工具（ReAct）。",
         ["ReAct 思考-行动", "AgentExecutor",
          "Plan-and-Execute"],
         "🤖 Agent 召唤师", 400, 400, "🎭 Agent 面具"),
        ("5-18", "多 Agent 协作秘境（隐藏关）", "👥 协作大师",
         "多个 Agent 分工合作完成复杂任务。",
         ["Multi-Agent 编排", "Role 分工",
          "CrewAI/Autogen"],
         "👥 协作大师", 410, 410, "🎪 协作剧场"),
        ("5-19", "微调熔炉", "🔥 熔炉火神",
         "用自己的数据给大模型「上课」。",
         ["LoRA 低秩适应", "QLoRA 4bit 量化微调",
          "PEFT 库"],
         "🔥 熔炉火神", 420, 420, "⚒️ 微调锤"),
        ("5-20", "数据集锻造坊", "⚔️ 数据锻造师",
         "高质量数据才是好微调的关键。",
         ["Alpaca/ShareGPT 格式", "数据清洗去重",
          "数据增强合成"],
         "⚔️ 数据锻造师", 430, 430, "📊 数据模具"),
        ("5-21", "评估竞技场", "🏆 评估裁判",
         "大模型效果怎么测？",
         ["BLEU/ROUGE 指标", "LLM-as-Judge",
          "人工评估最佳实践"],
         "🏆 评估裁判", 440, 440, "📏 评估标尺"),
        ("5-22", "BOSS：幻觉幽灵", "👻 幻觉幽灵巢穴",
         "幽灵让大模型满嘴胡言，需要 RAG + 引用 + 验证！",
         ["完整 RAG 系统", "引用来源", "反幻觉 Chain-of-Verification"],
         "👻 幻觉幽灵", 800, 800, "💎 星界晶石", True),
    ]
    return [_skeleton(l) for l in levels]


def _chapter6_levels():
    """第六章：云端天梯（15 关）"""
    levels = [
        ("6-1", "Git 时光遗迹", "📜 时光守护",
         "代码的时光机：回到任意版本。",
         ["init/add/commit/log", "分支 branch",
          ".gitignore"],
         "📜 时光守护", 300, 300, "⏳ 时光沙漏"),
        ("6-2", "GitHub 协作港口", "⚓ 港口船长",
         "多人协作开发的最佳实践。",
         ["push/pull/PR", "Code Review",
          "Fork + Pull Request"],
         "⚓ 港口船长", 310, 310, "🚢 协作航船"),
        ("6-3", "FastAPI 神殿", "🏛️ API 守门人",
         "把模型能力封装成 HTTP 接口。",
         ["@app.get / @app.post", "Pydantic 数据模型",
          "path/query 参数"],
         "🏛️ API 守门人", 320, 320, "🔌 API 钥匙"),
        ("6-4", "异步竞技场", "⚡ 异步剑士",
         "高并发的秘诀：async/await。",
         ["async def / await", "BackgroundTasks",
          "Streaming 流式响应"],
         "⚡ 异步剑士", 330, 330, "🌀 异步披风"),
        ("6-5", "中间件迷宫", "🌀 中间件守门",
         "在请求前后统一处理。",
         ["CORSMiddleware", "JWT 认证中间件",
          "Depends 依赖注入"],
         "🌀 中间件守门", 340, 340, "🛡️ 中间件盾"),
        ("6-6", "Docker 方舟", "🚢 方舟舵手",
         "把整个环境打包带走，哪里都能跑。",
         ["Dockerfile FROM/COPY/CMD", "镜像/容器",
          "端口映射 -p"],
         "🚢 方舟舵手", 350, 350, "📦 容器宝箱"),
        ("6-7", "Docker Compose 港口", "⚓ 港口船长",
         "多个容器一起协作：API + 数据库 + 向量库。",
         ["docker-compose.yml", "services/networks/volumes",
          "up/down"],
         "⚓ 港口船长", 360, 360, "⛓️ 编排锁链"),
        ("6-8", "云端天梯", "☁️ 云端守卫",
         "把服务搬到公网：云服务器 + Nginx。",
         ["SSH 部署", "Nginx 反向代理",
          "HTTPS + 域名"],
         "☁️ 云端守卫", 370, 370, "🚀 云端火箭"),
        ("6-9", "Gradio 展台", "🎪 展台主持",
         "快速搭建演示界面给用户体验。",
         ["gr.Interface(fn, inputs, outputs)",
          "gr.Blocks 高级布局", "State 状态"],
         "🎪 展台主持", 380, 380, "🎨 展示画布"),
        ("6-10", "Streamlit 王座", "👑 王座守护",
         "用 Streamlit 打造复杂的数据+AI 工具。",
         ["session_state", "st.cache_data 缓存",
          "多页面 multipage"],
         "👑 王座守护", 390, 390, "🌟 王座权杖"),
        ("6-11", "前端桥梁（隐藏关）", "🌉 前端桥梁师",
         "让 AI API 和真·前端网页对接。",
         ["fetch API 调后端", "WebSocket 流式",
          "SSE 服务器推送"],
         "🌉 前端桥梁师", 400, 400, "🌈 前端彩虹"),
        ("6-12", "量化工坊", "⚖️ 量化大师",
         "让大模型跑得更快更省内存。",
         ["bitsandbytes int8/int4",
          "AWQ/GPTQ", "推理 benchmark"],
         "⚖️ 量化大师", 410, 410, "⚡ 闪电护符"),
        ("6-13", "监控哨所", "📡 哨所指挥官",
         "在线上随时监控系统健康。",
         ["logging 日志", "Prometheus/metrics",
          "/health 健康检查"],
         "📡 哨所指挥官", 420, 420, "🛰️ 监控雷达"),
        ("6-14", "CI/CD 神殿（隐藏关）", "🤖 CI/CD 神官",
         "代码一提交，自动测试自动部署。",
         ["GitHub Actions", "自动化测试",
          "自动 Docker Build & Deploy"],
         "🤖 CI/CD 神官", 430, 430, "⚙️ 自动化齿轮"),
        ("6-15", "终极 BOSS：Bugzor 本体", "👹 Bugzor 最终形态巢穴",
         "集齐六块晶石，击败 Bugzor！",
         ["完整 AI 产品：API + RAG + 前端 + Docker + CI",
          "上线可用", "性能达标"],
         "👹 Bugzor 本体", 1500, 1500, "👑 数据大陆守护者徽章", True),
    ]
    return [_skeleton(l) for l in levels]


# ==============================================================================
# 关卡骨架生成器
# ==============================================================================
def _skeleton(raw):
    """把 (id,name,scene,story,know,monster,mh,exp,item[,is_boss]) 变成关卡字典。
    三档难度的判定全部设为 "output_any"，等待后续补充具体题目。
    """
    if len(raw) == 9:
        id_, name, scene, story, know, monster, mh, exp, item = raw
        is_boss = False
    else:
        id_, name, scene, story, know, monster, mh, exp, item, is_boss = raw
    return {
        "id": id_, "name": name, "scene": scene, "story": story,
        "knowledge": know, "monster": monster,
        "monster_hp": mh, "reward_exp": exp, "reward_item": item,
        "is_boss": is_boss,
        "_skeleton": True,  # 标记为骨架，后续补充三档题目
        "modes": {
            "teach": {"label": "教学模式",
                      "instruction": f"（{name}）此关三档题目暂未编写，通关需 1 任意输出。",
                      "template": 'print("我学会了' + name + '")',
                      "check_type": "output_any",
                      "expected": "", "hint": "任意 print 一行即可"},
            "fill": {"label": "填空模式",
                     "instruction": "把 ___ 填成任意内容后输出：",
                     "template": 'print("我通过关卡 ' + id_ + '：___")',
                     "check_type": "output_any", "expected": "",
                     "hint": "___ 处可以填任意话"},
            "challenge": {"label": "挑战模式",
                          "instruction": "编写任意代码并输出一行，即可通关",
                          "template": "", "check_type": "output_any",
                          "expected": None,
                          "hint": "后续会补充具体题目；当前任意 print 即可"},
        },
    }


# ==============================================================================
# 对外接口
# ==============================================================================
def get_all_chapters():
    """获取所有章节字典 {章节号: {title, subtitle, levels}}"""
    meta = CHAPTER_META
    return {
        1: {**meta[1], "levels": CHAPTER1_LEVELS},
        2: {**meta[2], "levels": _chapter2_levels()},
        3: {**meta[3], "levels": _chapter3_levels()},
        4: {**meta[4], "levels": _chapter4_levels()},
        5: {**meta[5], "levels": _chapter5_levels()},
        6: {**meta[6], "levels": _chapter6_levels()},
    }


def get_chapter(n: int):
    return get_all_chapters().get(n)


def total_all_levels() -> int:
    """统计所有关卡总数"""
    return sum(len(c["levels"]) for c in get_all_chapters().values())


if __name__ == "__main__":
    print("总关卡数:", total_all_levels())
    for i, data in get_all_chapters().items():
        sk = sum(1 for lv in data["levels"] if lv.get("_skeleton"))
        fu = len(data["levels"]) - sk
        print(f"第{i}章 {data['title']}: {len(data['levels'])} 关"
              f"（完整可玩 {fu} 关 / 骨架 {sk} 关）")
