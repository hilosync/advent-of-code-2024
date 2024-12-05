import re

pattern = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
multiplications = 0

with open("input.txt") as input:
    for line in input:
        for match in re.finditer(pattern,line):
            x,y = match.group().removesuffix(")").removeprefix("mul(").split(',')
            multiplications += int(x) * int(y)

print(multiplications)

    

