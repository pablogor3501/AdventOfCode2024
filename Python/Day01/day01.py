import sys

formatedInput = open(sys.argv[1]).read().replace("\n","   ").split("   ")

left = [int(formatedInput[i]) for i in range(len(formatedInput)) if not (i % 2)]
right = [int(formatedInput[i]) for i in range(len(formatedInput)) if (i % 2)]
left.sort(), right.sort()

result = [0, 0]
for i in range(len(left)):
    result[0] += abs(left[i] - right[i])
    result[1] += left[i] * right.count(left[i])    

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")