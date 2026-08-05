# 🎮 AI 勇者纪元 - Python 学习 RPG

> 用玩游戏的方式学 Python，把代码能力变成你的战斗力

---

## 📖 项目简介

这是一款基于 Streamlit 的文字 RPG 学习游戏，把 Python 基础语法学习包装成冒险闯关。你扮演一名代码勇者，通过编写 Python 代码击败怪物，逐步掌握 print、变量、字符串、if-else、for 循环等核心语法。

**当前内容**：第一章「语法森林」共 6 关（5 普通 + 1 BOSS）

---

## ⚙️ 环境配置条件

### 1. 操作系统
- ✅ Windows 10 / 11
- ✅ macOS 10.15+
- ✅ Linux（Ubuntu 20.04+ 等）

### 2. Python 版本
- **最低要求**：Python 3.8+
- **推荐版本**：Python 3.10 或 3.11（最稳定）

> ⚠️ 不支持 Python 2.x，也不建议用 3.7 以下版本（dataclass 等特性需要 3.7+）

### 3. 必需依赖
| 包名 | 版本 | 用途 |
|------|------|------|
| streamlit | >=1.28.0 | Web 界面框架 |
| Python 标准库 | - | json / io / pathlib / dataclasses（无需安装） |

### 4. 硬件要求
- 内存：512MB 以上
- 磁盘：50MB 可用空间
- 无需 GPU

### 5. 网络
- 首次安装依赖需要联网（`pip install streamlit`）
- 运行游戏**无需联网**（纯本地运行）

---

## 📦 安装步骤

### 方式 A：全新安装（推荐新手）

#### 第 1 步：安装 Python
1. 访问 https://python.org/downloads
2. 下载 Python 3.10 或 3.11
3. **Windows 用户**：安装时务必勾选 ✅ `Add Python to PATH`

#### 第 2 步：验证 Python 安装
打开命令行（Win: `cmd` / Mac: `终端`），执行：
```bash
python --version
```
看到 `Python 3.x.x` 表示成功。

#### 第 3 步：安装 Streamlit
```bash
pip install streamlit
```
或国内用户加速安装：
```bash
pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 第 4 步：验证 Streamlit
```bash
streamlit hello
```
浏览器自动打开欢迎页说明安装成功。按 `Ctrl+C` 退出。

#### 第 5 步：获取项目代码
任选其一：

**用 Git 克隆**（如果你推到了 GitHub）：
```bash
git clone https://github.com/你的用户名/ai-rpg-game.git
cd ai-rpg-game
```

**手动复制**：把 11 个 .py 文件按以下结构放到同一文件夹：
```
ai_rpg_game/
├── app.py
├── requirements.txt
├── core/
│   ├── __init__.py
│   ├── player.py
│   ├── battle.py
│   └── engine.py
├── data/
│   ├── __init__.py
│   └── chapters.py
└── ui/
    ├── __init__.py
    ├── sidebar.py
    ├── map_view.py
    └── battle_view.py
```

#### 第 6 步：启动游戏
```bash
cd ai_rpg_game
streamlit run app.py
```
浏览器自动打开 `http://localhost:8501`，开始游戏！

---

### 方式 B：用 requirements.txt 安装（推荐进阶）

```bash
cd ai_rpg_game
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎮 玩法说明

### 难度模式
每关提供三档难度，自由切换：

| 模式 | 说明 | 经验奖励 |
|------|------|---------|
| 🟢 教学模式 | 照抄示例代码，熟悉手感 | 50%（减半） |
| 🟡 填空模式 | 补全 `___` 处的关键代码 | 100% |
| 🔴 挑战模式 | 只给需求，从零编写 | 100% |

### 通关奖励
- 每关通关：经验值 + 装备道具
- 每 100 经验：升 1 级（HP+20 / 攻击+5 / 防御+2 / 满血）

### 卡关怎么办
- 点 `💡 查看提示`：获取本关提示
- 点 `👁️ 显示答案`：直接看答案（仍可通关，但建议先自己尝试）

### 存档机制
- 自动存档到 `save/player.json`
- 关闭浏览器再打开，进度仍在
- 侧边栏 `🔄 重新开始` 可清空存档

---

## ⚠️ 注意事项

### 1. 代码运行安全
- 游戏会执行你输入的 Python 代码
- 已做基础沙箱限制，但仍**不要输入危险代码**（如 `os.remove` / `subprocess` 等）
- 建议在虚拟环境中运行（见下方「进阶配置」）

### 2. 浏览器兼容性
- ✅ Chrome / Edge / Firefox（推荐）
- ✅ Safari
- ⚠️ 不支持 IE 浏览器

### 3. 端口冲突
默认使用 8501 端口。若被占用，可指定其他端口：
```bash
streamlit run app.py --server.port 8502
```

### 4. 中文显示
- 代码中含中文字符串，确保编辑器保存为 **UTF-8 编码**
- Windows 命令行若中文乱码，执行：
  ```bash
  chcp 65001
  ```

### 5. 修改代码后刷新
- 用 VS Code 修改代码后，`Ctrl+S` 保存
- 浏览器右上角点 `Rerun` 或按 `R` 键刷新
- 也可开启自动刷新：`streamlit run app.py --server.runOnSave true`

### 6. 存档损坏恢复
若存档损坏导致游戏异常：
1. 删除 `save/player.json`
2. 重新启动游戏，会自动创建新存档

### 7. 不要修改的文件
- `core/` 目录下的文件除非你懂 Python，否则不要改
- 想加新关卡，只改 `data/chapters.py`
- 想改界面，只改 `ui/` 目录下的文件

---

## 🐛 常见问题

### Q1：`streamlit: command not found`
**原因**：Python 的 Scripts 目录未加入 PATH
**解决**：
- Windows：`python -m streamlit run app.py`
- Mac/Linux：`python3 -m streamlit run app.py`

### Q2：`ModuleNotFoundError: No module named 'streamlit'`
**原因**：未安装 streamlit，或装在了别的 Python 环境
**解决**：
```bash
pip install streamlit
# 或
python -m pip install streamlit
```

### Q3：浏览器没有自动打开
**解决**：手动访问 `http://localhost:8501`

### Q4：代码输入框报错「代码出错了」
**原因**：你输入的 Python 代码本身有语法错误
**解决**：检查错误信息，常见问题：
- 中文冒号 `：` 应为英文 `:`
- 中文引号 `""` 应为英文 `""`
- 缩进不一致（统一用 4 个空格）

### Q5：升级后属性没变？
**原因**：升级属性增量在 `core/player.py` 的 `LEVEL_UP_BONUS`
**解决**：修改后重启游戏生效

### Q6：pip 安装太慢
**解决**：使用国内镜像源
```bash
pip install streamlit -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## 🛠️ 进阶配置

### 使用虚拟环境（推荐）
避免污染全局 Python 环境：

```bash
# 创建虚拟环境
python -m venv venv

# 激活（Windows）
venv\Scripts\activate

# 激活（Mac/Linux）
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动游戏
streamlit run app.py
```

### VS Code 推荐扩展
- **Python**（微软官方）：语法高亮、智能提示
- **Streamlit**：Streamlit 代码辅助
- **Code Runner**：快速运行代码片段

### VS Code launch.json 配置
在 `.vscode/launch.json` 添加：
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "AI RPG Game",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": ["run", "app.py"],
            "console": "integratedTerminal"
        }
    ]
}
```
按 F5 即可一键启动游戏。

---

## 📁 项目结构

```
ai_rpg_game/
├── app.py                  # 入口文件（启动游戏）
├── requirements.txt        # 依赖清单
├── README.md               # 本文件
│
├── core/                   # 核心逻辑层（不依赖界面）
│   ├── __init__.py
│   ├── player.py           # 玩家系统（属性/存档/升级）
│   ├── battle.py           # 战斗系统（代码执行与判定）
│   └── engine.py           # 游戏引擎（关卡状态管理）
│
├── data/                   # 数据层
│   ├── __init__.py
│   └── chapters.py         # 关卡内容数据
│
├── ui/                     # 界面层（Streamlit）
│   ├── __init__.py
│   ├── sidebar.py          # 侧边栏角色卡
│   ├── map_view.py         # 关卡地图
│   └── battle_view.py      # 战斗界面
│
└── save/                   # 存档目录（自动生成）
    └── player.json         # 玩家存档
```

---

## 🎯 后续扩展指南

### 加一个新关卡
编辑 `data/chapters.py`，在 `CHAPTER1_LEVELS` 列表末尾加一个字典，参考现有关卡格式。

### 加第二章
在 `data/chapters.py` 新建 `CHAPTER2_LEVELS` 列表，并在 `app.py` 中切换。

### 修改升级规则
编辑 `core/player.py`：
- `EXP_PER_LEVEL`：每级所需经验
- `LEVEL_UP_BONUS`：升级属性增量

### 接入 AI（进阶）
在 `ui/battle_view.py` 中接入 LLM API，让 NPC 会说话、能给代码提示等。

---

## 📞 技术支持

遇到问题可检查：
1. Python 版本是否符合（`python --version`）
2. 依赖是否安装（`pip list | grep streamlit`）
3. 文件结构是否完整（11 个 .py 文件 + requirements.txt）
4. 存档是否损坏（删除 `save/player.json` 重试）

---

## 📜 版本信息

- **版本**：v1.0.0
- **章节**：第一章「语法森林」
- **关卡数**：6 关（5 普通 + 1 BOSS）
- **最后更新**：2026-08-05

---

**祝你冒险愉快，勇者！** 🎮⚔️
