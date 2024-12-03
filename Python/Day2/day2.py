import sys

def safe(report, tolerate = False):
    diff = [(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    if (tolerate):
        return any(safe(report[:i] + report[i + 1:]) for i in range(len(report)))
    else:
        return all((d > 0 and abs(d) < 4) for d in diff) or all((d < 0 and abs(d) < 4) for d in diff)

formatedInput = open(sys.argv[1]).read().split("\n")

result = [0,0] 
for reportStr in formatedInput:
    report = [int(n) for n in reportStr.split(" ")]
    result[0] += safe(report)
    result[1] += safe(report, True)

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")