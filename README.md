# home-skills

**三个面向真实家庭场景的开源 AI Agent Skill：用电省钱、旧机重生、远程孝心。**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-3-blue.svg)](skills/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 它解决什么问题

大多数家庭每年都在为三件事悄悄付费，却几乎没有人认真解决过：

| 家庭问题 | 现状 | 本项目的答案 |
|---|---|---|
| **电费交得不明不白** | 知道有峰谷电价，但不知道本地时段、不知道自己能省多少、更没有工具帮自己落地 | `peak-shift` — 查清本地电价，算出每台电器能省多少，给出可执行的定时配置 |
| **旧手机在抽屉里吃灰** | 卖不上价、扔了可惜，想改造成监控/相框/副屏却卡在技术门槛上 | `device-reborn` — 评估设备能力，匹配用途模板，手把手带你完成改造 |
| **父母的问题永远教不会** | 电话里说不清"点右上角那个图标"，远程控制工具对老人又是新门槛 | `elder-bridge` — 把模糊的问题翻译成精确的屏幕路径与可照读的话术 |

---

## 包含的 Skill

### 1. `peak-shift` · 家庭峰谷电价用电优化 → **已迁移**

> ⚠️ **本方向已独立为专门仓库 `peak-shift-skill`。**

峰谷电价的规模（31 省数据 + 优化引擎 + 可视化）已超出单个子模块的合理范围，
现已独立。本目录仅保留迁移指引。详见 `skills/peak-shift/SKILL.md`。

### 2. `device-reborn` · 旧设备再利用工具包 `预览`

> 旧设备的「能力评估 + 改造向导」

- 输入设备型号与目标用途，输出可行性判断、分步改造指南与所需资源清单
- 核心资产：机型能力库（`data/devices/`）+ 用途模板库
- 与 3,661★ 的 `linux-android` 走不同路线：**这里面向不懂技术的普通家庭**

### 3. `elder-bridge` · 长辈手机远程协助 `预览`

> 远程协助的「问题翻译器 + 话术生成器」

- 输入长辈模糊的问题描述，输出精确的屏幕操作路径与子女可照读的逐句话术
- 核心资产：常见问题库（`data/faq/`）
- 与 377 个"养老大平台"类项目走反向路线：**只做减法，聚焦远程指屏这一个高频单点**

---

## 快速开始

### 作为 Agent Skill 安装

```bash
git clone https://github.com/xfnylqt/home-skills.git
cp -r home-skills/skills/* ~/.claude/skills/     # Claude Code
# 或 ~/.codex/skills/ / ~/.cursor/skills/ 等
```

### 直接使用脚本

```bash
cd home-skills/skills/peak-shift
python scripts/calc_savings.py --region 北京 --appliance water_heater --power 2000 --hours 2
```

---

## 仓库结构

```
home-skills/
├── skills/                 # 三个独立的 Agent Skill（可单独安装）
│   ├── peak-shift/
│   ├── device-reborn/
│   └── elder-bridge/
├── data/                   # 共享数据层（欢迎社区贡献）
│   ├── tariffs/cn/         # 各省峰谷电价
│   ├── devices/            # 机型能力库
│   └── faq/                # 长辈常见问题库
├── docs/                   # 愿景、路线图、数据格式说明
└── examples/               # 示例
```

---

## 设计原则

1. **本地优先** — 涉及家庭与老人数据，全部本地处理，不上传、不联网
2. **零外部依赖** — 脚本只用 Python 标准库，不增加安装门槛
3. **Skill 独立** — 三个 skill 可单独安装使用，互不依赖
4. **面向非技术用户** — 目标用户是普通家庭，不是极客
5. **数据可贡献** — 电价、机型、问题库均为结构化 YAML，欢迎 PR

---

## 参与贡献

最需要的贡献是**数据**：

- 你所在省市的峰谷电价（`data/tariffs/cn/`）
- 你改造过的旧设备经验（`data/devices/`）
- 长辈遇到的典型问题（`data/faq/`）

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可证

[MIT](LICENSE)

---

> **免责声明**：本项目为独立开源项目。电价数据由社区贡献，可能存在滞后或误差，请以当地供电部门官方公布为准；旧设备改造涉及电池与用电安全，请在理解风险的前提下操作，本项目不对改造后果承担责任。
