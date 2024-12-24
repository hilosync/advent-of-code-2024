guard_map = []

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


def check_loop(start_location):
    curr_location = start_location
    visited = set()
    while True:
        guard_y, guard_x, guard_direction = curr_location

        if (
            guard_y == 0
            or guard_y == len(guard_map) - 1
            or guard_x == 0
            or guard_x == len(guard_map[0]) - 1
        ):
            return False

        if guard_direction == 0:
            next_square = (guard_y - 1, guard_x)

        if guard_direction == 1:
            next_square = (guard_y, guard_x + 1)

        if guard_direction == 2:
            next_square = (guard_y + 1, guard_x)

        if guard_direction == 3:
            next_square = (guard_y, guard_x - 1)

        if curr_location in visited:
            return True

        visited.add(curr_location)

        if guard_map[next_square[0]][next_square[1]] == 0:
            guard_map[next_square[0]][next_square[1]] = 2
            curr_location = (next_square[0], next_square[1], guard_direction)

        elif guard_map[next_square[0]][next_square[1]] == 2:
            curr_location = (next_square[0], next_square[1], guard_direction)

        elif guard_map[next_square[0]][next_square[1]] == 1:
            new_direction = (guard_direction + 1) % 4
            curr_location = (guard_y, guard_x, new_direction)


loops = 0
for i in range(len(guard_map)):
    for j in range(len(guard_map[0])):
        if guard_map[i][j] == 1 or (i == guard_location[0] and j == guard_location[1]):
            continue

        guard_map[i][j] = 1
        if check_loop(guard_location):
            loops += 1
        guard_map[i][j] = 0

print(loops)
