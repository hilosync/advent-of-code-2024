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

def checkXMAS(y1,x1,y2,x2,y3,x3,y4,x4):
    if words[y1][x1] == 'X' and words[y2][x2] == 'M' and words[y3][x3] == 'A' and words[y4][x4] == 'S':
        return 1
    return 0


for y in range(len(words)):
    for x in range(len(words[y])):

        if x <= len(words[y]) - 4:
            result += checkXMAS(y,x,y,x+1,y,x+2,y,x+3)

            if y >= 3:
                result += checkXMAS(y,x,y-1,x+1,y-2,x+2,y-3,x+3)

            if y <= len(words) - 4:
                result += checkXMAS(y,x,y+1,x+1,y+2,x+2,y+3,x+3)
        
        if x >= 3:
            result += checkXMAS(y,x,y,x-1,y,x-2,y,x-3)

            if y >= 3:
                result += checkXMAS(y,x,y-1,x-1,y-2,x-2,y-3,x-3)

            if y <= len(words) - 4:
                result += checkXMAS(y,x,y+1,x-1,y+2,x-2,y+3,x-3)

        if y >= 3:
            result += checkXMAS(y,x,y-1,x,y-2,x,y-3,x)
        
        if y <= len(words) - 4:
            result += checkXMAS(y,x,y+1,x,y+2,x,y+3,x)

        
print(result)