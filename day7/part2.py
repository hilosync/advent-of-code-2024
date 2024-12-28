from collections import defaultdict

calculations = defaultdict(list)

with open("input.txt") as input:
    for line in input:
        result, measurements = line.split(":")
        measurements = measurements.removeprefix(" ").removesuffix("\n")
        calculations[result].append(measurements.split(" "))


def find_result(curr_result, i):
    if curr_result == target and i == len(value):
        return True

    if curr_result > target or i == len(value):
        return False

    return (
        find_result(curr_result * int(value[i]), i + 1)
        or find_result(curr_result + int(value[i]), i + 1)
        or find_result(int(str(curr_result) + value[i]), i + 1)
    )


result = 0
for key, calculation in calculations.items():
    target = int(key)

    for value in calculation:
        if find_result(int(value[0]), 1):
            result += target

print(result)
