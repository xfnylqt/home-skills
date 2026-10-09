---
name: peak-shift
description: 【已迁移】本目录不再包含峰谷电价的实现。峰谷电价能力已独立为专门的 Agent Skill 仓库 peak-shift-skill，包含全国 31 个省级行政区的电价数据、优化引擎与可视化。请勿在此处继续开发。
license: MIT
metadata:
  status: migrated
  migrated_to: peak-shift-skill
  migrated_on: "2026-10-09"
---

# 已迁移至 `peak-shift-skill`

本目录曾是峰谷电价能力的实现位置。**现已迁移。**

## 迁移原因

峰谷电价能力的规模已超出「家庭生活技能集」中单个子模块的合理范围：

| 维度 | 规模 |
|---|---|
| 数据 | 31 个省级行政区，每条含来源机构、URL、政策文号、生效日期、可信度分级 |
| 计算 | 15 分钟粒度优化引擎，含跨天窗口、可中断负荷、基准线建模 |
| 可视化 | 3 类图表 + HTML 报告生成 |
| 文档 | SKILL.md + 3 份参考文档 |

继续留在集合仓库中会导致三个问题：

1. 数据与代码的更新节奏被其他模块拖累
2. 无法独立发版、独立贡献
3. 与「家庭生活技能集」的其他方向（旧设备再利用、长辈协助）产生耦合

## 迁移去向

→ **`peak-shift-skill`**（同工作区内的独立仓库）

新的分层结构：

```
cn-tou-tariff（数据）→ peak-shift-engine（计算）→ peak-shift-studio（可视化）
                              ↓
                    peak-shift-skill（Agent Skill 封装层）
```

## 本目录现状

已移除：

- ~~`scripts/calc_savings.py`~~ —— 简化版计算器，被 `peak-shift-engine` 完整取代
- ~~`assets/report-template.md`~~ —— 被 `peak-shift-studio` 的模板取代
- ~~`../../data/tariffs/cn/*.json`~~ —— schema 已变更（新增 `confidence`、`residential_tou_available` 等字段）

保留本文件作为**迁移指引**，避免引用旧路径时产生困惑。

## 本仓库（home-skills）的定位

`home-skills` 现聚焦于另外两个方向，与峰谷电价解耦：

| 方向 | 目录 | 状态 |
|---|---|---|
| 旧设备再利用 | `skills/device-reborn/` | 骨架 |
| 长辈手机远程协助 | `skills/elder-bridge/` | 骨架 |

峰谷电价方向请移步 `peak-shift-skill`。
