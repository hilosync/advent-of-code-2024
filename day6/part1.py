guard_map = []
guard_location = None

with open("input.txt") as input:
    for line in input:
        map_line = []
        for char in line:
            if char == ".":
                map_line.append(0)
            if char == "#":
                map_line.append(1)
            if char == "^":
                guard_location = (len(guard_map) - 1, len(map_line), 0)
                map_line.append(2)
        guard_map.append(map_line)

visited = 1

while True:
    guard_y, guard_x, guard_direction = guard_location

    if (
        guard_y == 0
        or guard_y == len(guard_map) - 1
        or guard_x == 0
        or guard_x == len(guard_map[0]) - 1
    ):
        print(visited)
        break

    next_square = None

    if guard_direction == 0:
        next_square = (guard_y - 1, guard_x)

    if guard_direction == 1:
        next_square = (guard_y, guard_x + 1)

    if guard_direction == 2:
        next_square = (guard_y + 1, guard_x)

    if guard_direction == 3:
        next_square = (guard_y, guard_x - 1)

    if guard_map[next_square[0]][next_square[1]] == 0:
        guard_map[next_square[0]][next_square[1]] = 2
        visited += 1
        guard_location = (next_square[0], next_square[1], guard_direction)

    elif guard_map[next_square[0]][next_square[1]] == 2:
        guard_location = (next_square[0], next_square[1], guard_direction)

    elif guard_map[next_square[0]][next_square[1]] == 1:
        new_direction = (guard_direction + 1) % 4
        guard_location = (guard_y, guard_x, new_direction)
