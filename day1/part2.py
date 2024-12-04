input = open('input.txt')

list1 = []
list2 = []

for line in input:
    item1, item2 = line.split("   ")

    list1.append(int(item1))
    list2.append(int(item2))

input.close()

occurenceCount = {}

for i in list2:
    if i not in  occurenceCount:
        occurenceCount[i] = 0
    occurenceCount[i] += 1

similarityScore = 0

for i in list1:
    if i in occurenceCount:
        similarityScore += i * occurenceCount[i]

print(similarityScore)