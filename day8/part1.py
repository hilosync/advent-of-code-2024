from collections import defaultdict

antenna_map = defaultdict(list)

with open("input.txt") as input:
    y = 0
    for line in input:
        line = line.removesuffix("\n")
        for x in range(len(line)):
            if line[x] == ".":
                continue
            else:
                antenna_map[line[x]].append((x, y))
        y += 1

visited = set()
for antenna in antenna_map.values():
    if len(antenna) == 1:
        continue
