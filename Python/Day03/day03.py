import sys
import re

formatedInput = open(sys.argv[1]).read()

regex = "(mul\([0-9]{0,3},[0-9]{0,3}\)|do\(\)|don't\(\))"
mulList = re.findall(regex, formatedInput)
result = [0,0]

multiply = { "do()": True, "don't()": False, "add": True }

for mul in mulList:
    if (mul.startswith("mul")):
        prod = mul.lstrip("mul(").rstrip(")").split(",")
        result[1] += int(prod[0]) * int(prod[1]) * multiply["add"]
        result[0] += int(prod[0]) * int(prod[1])
    else:
        multiply["add"] = True if (multiply[mul]) else False 

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")