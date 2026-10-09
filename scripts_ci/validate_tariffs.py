#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CI：校验 data/tariffs/cn/*.json 的格式合规性（纯标准库）。"""

import json
import sys
from pathlib import Path

REQUIRED_TOP = ["region", "province_code", "effective_date", "source", "verified", "periods"]
REQUIRED_PERIOD = ["name", "start", "end", "price"]
VALID_NAMES = {"peak", "flat", "valley"}


def validate(path):
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return ["JSON 解析失败：%s" % e]

    for k in REQUIRED_TOP:
        if k not in data:
            errors.append("缺少必填字段：%s" % k)

    periods = data.get("periods")
    if not isinstance(periods, list) or not periods:
        errors.append("periods 必须是非空数组")
        return errors

    for i, p in enumerate(periods):
        if not isinstance(p, dict):
            errors.append("periods[%d] 不是对象" % i)
            continue
        for k in REQUIRED_PERIOD:
            if k not in p:
                errors.append("periods[%d] 缺少字段 %s" % (i, k))
        if p.get("name") not in VALID_NAMES:
            errors.append("periods[%d].name 取值非法：%r（应为 peak/flat/valley）" % (i, p.get("name")))

    if not any(isinstance(p, dict) and p.get("name") == "valley" for p in periods):
        errors.append("必须至少包含一个 valley（谷段）定义")

    if data.get("verified") is False and not data.get("example"):
        # 未核实且非示例数据 → 提醒但不阻断
        errors.append("[提醒] verified=false 且未标 example，请确认数据来源")

    return errors


def main():
    root = Path(__file__).resolve().parent.parent / "data" / "tariffs" / "cn"
    files = sorted(root.glob("*.json"))
    if not files:
        print("未找到任何电价数据文件：%s" % root)
        return 1

    hard_fail = False
    for f in files:
        errs = [e for e in validate(f)]
        hard = [e for e in errs if not e.startswith("[提醒]")]
        if hard:
            hard_fail = True
            print("[FAIL] %s" % f.name)
            for e in errs:
                print("       - %s" % e)
        elif errs:
            print("[WARN] %s" % f.name)
            for e in errs:
                print("       - %s" % e)
        else:
            print("[ OK ] %s" % f.name)

    if hard_fail:
        print("\n校验未通过。请参考 data/tariffs/cn/_SCHEMA.md 修正。")
        return 1
    print("\n全部通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
