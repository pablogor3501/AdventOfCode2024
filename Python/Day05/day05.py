import sys

formatedInput = open(sys.argv[1]).read().split("\n\n")
rules = [list(map(int, line.split("|"))) for line in formatedInput[0].split("\n")]
updates = [list(map(int, line.split(","))) for line in formatedInput[1].split("\n")]

result = [0,0]
ruleDict = { k:[value for key,value in rules if key == k] for k, _ in rules }

for update in updates:
    incorrectPositions = [len(set(update[:i]).intersection(set(ruleDict.get(update[i], {})))) for i in range(1, len(update))]
    if not any(incorrectPositions):
        result[0] += update[len(update) // 2]
    else:
        [update.insert(i + 1 - incorrectPositions[i], update.pop(i + 1)) for i in range(len(incorrectPositions)) if (incorrectPositions[i])]
        result[1] += update[len(update) // 2]

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")