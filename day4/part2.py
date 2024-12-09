words = []

with open("input.txt") as input:
    for line in input:
        words.append(list(line))


'''
Forward: x + 3 done
Backwards: x - 3
Down: y + 3
Up: y - 3
Daig right up: y - 3, x + 3
Diag left up: y - 3, x - 3
diag right down: y + 3, x + 3
diag left down: y + 3, x - 3
'''

result = 0

def checkXMAS(y1,x1,y2,x2,y3,x3,y4,x4,y5,x5):
    if words[y1][x1] == 'A':
        if words[y2][x2] == 'S' and words[y3][x3] == 'M' or words[y2][x2] == 'M' and words[y3][x3] == 'S':
            if words[y4][x4] == 'S' and words[y5][x5] == 'M' or words[y4][x4] == 'M' and words[y5][x5] == 'S':
                return 1
    return 0


for y in range(len(words)):
    for x in range(len(words[y])):

        if x <= len(words[y]) - 2 and x >= 1 and y >= 1 and y <= len(words)-2:
            result += checkXMAS(y,x,y-1,x-1,y+1,x+1,y-1,x+1,y+1,x-1)
        
print(result)