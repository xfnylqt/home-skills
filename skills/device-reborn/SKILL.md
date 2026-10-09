---
name: device-reborn
description: Assess and guide the reuse of idle old phones and tablets as home devices - security camera, digital photo frame, secondary display, car dash unit, home server, or senior-friendly phone. Use when the user asks 旧手机能干什么, 闲置手机怎么利用, turning an old phone into a camera or photo frame, or whether a specific old device can serve a given purpose. Prioritizes no-root, no-flash routes for non-technical users.
license: MIT
metadata:
  author: home-skills
  version: "0.1.0"
---

# Device Reborn — 旧设备再利用向导

把抽屉里的旧手机，变成家里真正有用的设备。**面向不懂技术的普通家庭，不是极客。**

## 何时使用

- 用户问「旧手机还能干什么」
- 用户想把闲置手机/平板改造成：监控摄像头、电子相框、副屏、车机、家庭服务器、长辈专用机
- 用户问「我这台 XX 能不能做 YY」
- 用户改造卡在某一步

**不适用**：购买建议、二手回收估价、刷机后的售后问题。

## 工作流程

### 步骤 1 — 收集设备信息

需要：品牌型号、系统（Android / iOS）、系统版本、是否已 root / 能否刷机、可用存储。

### 步骤 2 — 评估设备能力

查阅 `data/devices/` 中的机型能力库：

- 命中 → 读取该机型的能力评级
- 未命中 → 基于公开参数做保守判断，并**明确标注为推断**

### 步骤 3 — 匹配用途模板

读取 `data/recipes/{用途}.yaml`，对照设备能力给出结论：

| 结论 | 含义 |
|---|---|
| **推荐** | 设备能力充足，路线成熟 |
| **可行** | 能做，但有明确限制（性能/版本/发热） |
| **勉强** | 能跑但体验差，需说明代价 |
| **不建议** | 明确不可行，给出替代方案 |

### 步骤 4 — 生成改造指南

按 `references/guide-format.md` 输出：

1. 可行性结论与理由
2. 分步操作指引（**优先推荐不刷机路线**）
3. 所需 App / 脚本 / 配件清单
4. 安全提示（电池、散热、安全补丁）

### 步骤 5 — 生成配置

需要脚本或配置文件时，调用 `scripts/gen_config.py` 生成。

## 硬性规则

1. **优先不刷机路线。** 只有当用途必须刷机时才推荐，并明确风险。
2. **安全提示不可省略**：长期插电的电池鼓包风险、旧系统的安全漏洞，必须在动手前说明。
3. **不提供固件、不代刷机**、不对改造后果承担责任。
4. **设备能力判断必须有依据**：来自数据文件，或明确标注为推断。
5. **对不明型号诚实**：宁可说「不确定，建议先查参数」，不要编造。

## 参考文件

| 文件 | 用途 |
|---|---|
| `references/guide-format.md` | 改造指南输出格式 |
| `references/safety-notes.md` | 电池 / 散热 / 安全须知 |
| `data/devices/` | 机型能力库 |
| `data/recipes/` | 用途模板库 |
