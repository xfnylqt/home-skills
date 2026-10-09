---
name: elder-bridge
description: Translate vague problems reported by elderly parents into precise on-screen steps, and generate word-for-word scripts their adult children can read aloud. Use when the user asks 爸妈不会用手机, 怎么远程教父母, 教爸妈发微信, 长辈手机问题, how to guide an older relative through a phone task, or wants a step script for remote assistance. Covers common Chinese apps (WeChat, Alipay, settings) and includes scam warnings. Does not provide remote-control capability itself.
license: MIT
metadata:
  author: home-skills
  version: "0.1.0"
---

# Elder Bridge — 长辈手机远程协助

核心能力：**把「说不清」变成「指得到」，把「教不会」变成「照着念」。**

## 何时使用

- 用户描述父母/祖父母在手机上的问题（通常很模糊，如「发不出图片」「找不到那个按钮」）
- 用户想要一段可以照着念的指导话术
- 用户需要知道「该在屏幕哪个位置比划」
- 用户想帮长辈设置手机（字体、WiFi、App 安装）

**不适用**：远程控制底层实现、医疗建议、硬件故障诊断。

## 工作流程

### 步骤 1 — 澄清问题

长辈的描述往往不精确。基于 `data/faq/` 寻找匹配项：

- 高置信匹配 → 直接进入步骤 2
- 模糊 → **用排除法提问**（「打开微信后，屏幕上能看到对方的头像吗？」），但**最多问两轮**，避免让子女觉得麻烦

### 步骤 2 — 定位操作路径

输出精确的屏幕路径，例如：

```
微信首页 → 底部第三个标签「发现」→ 第一项「朋友圈」→ 右上角相机图标
```

### 步骤 3 — 生成话术脚本

按 `references/script-format.md` 生成逐句话术，要求：

- **每句只讲一个动作**
- 用长辈的方位词（「右下角」「最底下那排」），不用专业术语
- 每句后附一个**确认问题**（「您看到那个绿色的图标了吗？」）
- 卡住时的备选说法

示例：

> 「妈，您先打开微信。」
> 「看到最底下那排图标了吗？从左边数第三个，写着『发现』的。」
> 「点一下它。」

### 步骤 4 — 提供远程方式（可选）

若问题无法靠话术解决，引导使用屏幕共享方案（复用现有的成熟工具），并说明**建议由子女发起，长辈只需点同意**。

### 步骤 5 — 附加提醒

若问题涉及转账、链接、验证码等，**主动附加防骗提示**。

## 硬性规则

1. **每句话只包含一个动作。** 一句话里塞两个步骤是最大的失败原因。
2. **必须使用长辈能理解的方位词**，禁止出现「设置里的子菜单」「点击右上角的图标」这类模糊或专业表述。
3. **每句话后必须带确认问题**，确保长辈跟上了。
4. **澄清问题最多两轮**——子女自己要的是省事，不是被审问。
5. **涉及资金操作的场景必须给出防骗提醒。**
6. **不做医疗判断**，涉及健康问题建议就医。

## 参考文件

| 文件 | 用途 |
|---|---|
| `references/script-format.md` | 话术脚本输出格式 |
| `references/scam-patterns.md` | 常见诈骗场景提示 |
| `data/faq/` | 常见问题库（按 App × 问题类型组织） |
