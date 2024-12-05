import re

pattern = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)")
enabled = True
multiplications = 0

with open("input.txt") as input:
    for line in input:
        for match in re.finditer(pattern,line):
            match = match.group()
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            else:
                if enabled:
                    x,y = match.removesuffix(")").removeprefix("mul(").split(',')
                    multiplications += int(x) * int(y)

print(multiplications)

    

