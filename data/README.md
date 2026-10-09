# data/ — 共享数据层

三个 skill 共用的结构化数据。**这是本项目最有价值的资产**，也是最欢迎社区贡献的部分。

```
data/
├── tariffs/cn/    # 各省峰谷电价（peak-shift 用）
├── devices/       # 机型能力库（device-reborn 用）
├── recipes/       # 用途模板库（device-reborn 用）
└── faq/           # 常见问题库（elder-bridge 用）
```

## 通用原则

| 原则 | 说明 |
|---|---|
| **格式统一** | 全部使用 JSON（零依赖解析，见 `tariffs/cn/_SCHEMA.md` 的说明） |
| **可溯源** | 每个文件必须包含 `source` 字段 |
| **有日期** | 必须包含 `effective_date` 或 `updated_date` |
| **诚实标注** | 未核实的内容必须标 `verified: false` |
| **示例隔离** | 示例数据必须标 `example: true`，避免被误用 |

## 各类数据

### `tariffs/cn/` — 峰谷电价

格式详见 [`tariffs/cn/_SCHEMA.md`](tariffs/cn/_SCHEMA.md)。

被 `peak-shift` 读取，用于计算挪峰填谷能省多少钱。

### `devices/` — 机型能力库

记录旧手机/平板的能力评级，供 `device-reborn` 判断"这台设备能不能做某个用途"。

计划字段：型号、系统版本范围、性能评级、是否可刷机、已知问题、改造成功率。

> 🚧 格式待 M3 阶段定义。

### `recipes/` — 用途模板库

记录每种改造用途的完整步骤，供 `device-reborn` 生成改造指南。

计划覆盖用途：监控摄像头、电子相框、副屏、车机、家庭服务器、长辈专用机。

> 🚧 格式待 M3 阶段定义。

### `faq/` — 常见问题库

记录长辈常遇到的手机问题及其精确操作路径，供 `elder-bridge` 生成话术脚本。

计划字段：App、问题描述、关键词、操作路径、常见误解、相关诈骗提示。

> 🚧 格式待 M4 阶段定义。

## 如何贡献

见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

> ⚠️ **最重要的原则**：宁可标注「未核实」，也不要填入不确定的数值。用户会依据这些数据做真实的用电与消费决策，**错误的数据比没有数据更糟**。
