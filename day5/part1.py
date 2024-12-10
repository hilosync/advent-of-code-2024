
rulesDict = {}
manuals = []

with open("input.txt") as input:
    rules = True
    for line in input:
        if line == '\n':
            rules = False
            continue
        if rules:
            x, y = line.removesuffix('\n').split("|")
            if y in rulesDict:
                rulesDict[y].add(x)
            else:
                rulesDict[y] = set(x)
        else:
            manuals.append(list(line.removesuffix('\n').split(",")))

result = 0
# print(rulesDict)
for manual in manuals:
    beforeSet = set()
    middlePage = int(manual[len(manual)//2])
    for page in manual:
        if page in beforeSet:
            middlePage = 0
            break
        if page in rulesDict:
            beforeSet.update(rulesDict[page])
    result += middlePage

print(result)


