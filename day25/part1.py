from itertools import islice

keys = []
locks = []

with open("input.txt") as input:
    while True:
        data = list(islice(input, 8))
        if not data:
            break

        profile = [0] * 5
        for i in range(7):
            data[i].removesuffix("\n")
            for j in range(5):
                if data[i][j] == "#":
                    profile[j] += 1
        if data[0].removesuffix("\n") == ".....":
            keys.append(profile)
        else:
            locks.append(profile)

result = 0
for key in keys:
    for lock in locks:
        fits = True
        for i in range(5):
            if lock[i] + key[i] > 7:
                fits = False
        if fits:
            result += 1

print(result)
