# 贡献指南

感谢参与。本项目最需要的贡献是**数据**，而不是代码。

## 最需要什么

| 优先级 | 贡献类型 | 位置 |
|---|---|---|
| 🔥 最高 | 你所在省市的峰谷电价 | `data/tariffs/cn/` |
| 🔥 高 | 你改造旧设备的真实经验 | `data/devices/`、`data/recipes/` |
| 中 | 长辈遇到的典型手机问题 | `data/faq/` |
| 中 | 文档改进、错别字 | `docs/` |
| 低 | 脚本功能增强 | `skills/*/scripts/` |

## 贡献电价数据

1. 阅读 `data/tariffs/cn/_SCHEMA.md`
2. 以当地**发改委或供电公司官方文件**为准
3. 新建 `data/tariffs/cn/{省份拼音}.json`
4. 在 PR 描述中附上官方来源链接或截图

**硬性要求**：

- `source` 字段必须填写真实来源
- `effective_date` 必须填写
- 未核对官方原文时，`verified` 必须为 `false`
- 示例数据必须标 `example: true`

> 宁可标注"未核实"，也不要填入不确定的数值。**错误的数据比没有数据更糟**——用户会据此做真实的用电决策。

## 贡献旧设备经验

1. 在 `data/devices/{机型}.json` 记录设备能力
2. 在 `data/recipes/{用途}.json` 记录改造步骤
3. 优先提供**不刷机**的成功路径

**硬性要求**：如实记录失败案例同样有价值——请标注哪些机型不行、卡在哪一步。

## 提交规范

```bash
git checkout -b data/add-zhejiang-tariff
# 修改文件
git commit -m "data(tariffs): add Zhejiang 2026 peak/valley tariff"
git push origin data/add-zhejiang-tariff
```

提交信息格式：`<type>(<scope>): <description>`

| type | 用途 |
|---|---|
| `data` | 新增或修正数据 |
| `feat` | 新功能 |
| `fix` | 修复 |
| `docs` | 文档 |
| `chore` | 杂项 |

## 代码规范

- **零外部依赖**：脚本只使用 Python 标准库
- 支持 Python 3.8+
- 中文注释，变量名用英文
- 涉及金额计算的输出必须标注「估算」

## 数据质量原则

1. **可溯源**：每个数据点都能指回原始出处
2. **有日期**：政策会变，没有日期的数据等于没有数据
3. **诚实**：不确定就标不确定
4. **不编造**：这是这个项目存在的意义——用户已经受够了查不到、算不清

## 联系我们

提 Issue 即可。数据类问题请附来源。
