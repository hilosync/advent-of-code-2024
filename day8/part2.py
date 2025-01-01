from collections import defaultdict

antenna_map = defaultdict(list)

with open("input.txt") as input:
    y = 0
    for line in input:
        max_x = len(line)
        line = line.removesuffix("\n")
        for x in range(len(line)):
            if line[x] == ".":
                continue
            else:
                antenna_map[line[x]].append((x, y))
        y += 1
    max_y = y

visited = set()
result = 0
for antenna_locations in antenna_map.values():
    if len(antenna_locations) == 1:
        continue

    for index, antenna in enumerate(antenna_locations):
        if antenna not in visited:
            visited.add(antenna)
            result += 1
        for antenna_pair in antenna_locations[index + 1 :]:
            diff_x = antenna[0] - antenna_pair[0]
            diff_y = antenna[1] - antenna_pair[1]

            possible_antinode_1 = (antenna[0] + diff_x, antenna[1] + diff_y)
            possible_antinode_2 = (antenna_pair[0] - diff_x, antenna_pair[1] - diff_y)

            while (
                possible_antinode_1[0] >= 0
                and possible_antinode_1[0] < max_x
                and possible_antinode_1[1] >= 0
                and possible_antinode_1[1] < max_y
            ):
                if possible_antinode_1 not in visited:
                    visited.add(possible_antinode_1)
                    result += 1
                possible_antinode_1 = (
                    possible_antinode_1[0] + diff_x,
                    possible_antinode_1[1] + diff_y,
                )

            while (
                possible_antinode_2[0] >= 0
                and possible_antinode_2[0] < max_x
                and possible_antinode_2[1] >= 0
                and possible_antinode_2[1] < max_y
            ):
                if possible_antinode_2 not in visited:
                    visited.add(possible_antinode_2)
                    result += 1
                possible_antinode_2 = (
                    possible_antinode_2[0] - diff_x,
                    possible_antinode_2[1] - diff_y,
                )


print(result)
