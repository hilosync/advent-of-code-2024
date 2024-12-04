

input = open('input.txt')

list1 = []
list2 = []

for line in input:
    item1, item2 = line.split("   ")

    list1.append(int(item1))
    list2.append(int(item2))

list1.sort()
list2.sort()

distanceBetweenLists = 0

for i in range(len(list1)):
    distanceBetweenLists += abs(list1[i]-list2[i])

print(distanceBetweenLists)



    