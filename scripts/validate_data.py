#!/usr/bin/env python3
"""Check restaurants.csv tags against data/taxonomy/tags.yaml."""
import csv, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
tax = {}
key = None
for line in (root / "data/taxonomy/tags.yaml").read_text().splitlines():
    if ":" in line and "[" in line:
        k, v = line.split(":", 1)
        tax[k.strip()] = {x.strip() for x in v.strip(" []").split(",")}

bad = 0
with open(root / "data/restaurants/restaurants.csv", newline="", encoding="utf-8") as f:
    for i, row in enumerate(csv.DictReader(f), start=2):
        for col, allowed in (("occasions", "occasions"), ("food_items", "food_items")):
            for tag in filter(None, row.get(col, "").split(";")):
                if tag.strip() not in tax[allowed]:
                    print(f"row {i}: unknown {col} tag '{tag}'"); bad += 1
        if not row.get("hours_verified_on"):
            print(f"row {i}: missing hours_verified_on"); bad += 1
print("OK" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
