rulesDict = {}
manuals = []

with open("input.txt") as input:
    rules = True
    for line in input:
        if line == "\n":
            rules = False
            continue
        if rules:
            x, y = line.removesuffix("\n").split("|")
            if y in rulesDict:
                rulesDict[y].add(x)
            else:
                rulesDict[y] = set([x])
        else:
            manuals.append(list(line.removesuffix("\n").split(",")))


result = 0
for manual in manuals:
    incorrectRules = False
    index = 0
    while index < len(manual):
        for i in range(index):
            if manual[i] in rulesDict:
                if manual[index] in rulesDict[manual[i]]:
                    incorrectRules = True
                    temp = manual.pop(index)
                    manual = manual[:i] + [temp] + manual[i:]
                    break
        index += 1

    middlePage = int(manual[len(manual) // 2])
    result += middlePage if incorrectRules else 0

print(result)
