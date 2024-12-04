reports = []

with open("input.txt") as input:
    for line in input:
        line.removesuffix("\n")
        reports.append([int(x) for x in line.split(" ")])

safeReports = 0

for report in reports:
    safe = True
    if len(report) < 2:
        continue

    increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        prev, curr = report[i], report[i+1]

        if increasing and report[i] > report[i+1]:
            safe = False
            break
        if not increasing and report[i] < report[i+1]:
            safe = False
            break
        
        if 1 <= abs(report[i] - report[i+1]) <= 3:
            continue
        else:
            safe = False
            break
    
    safeReports += safe

print(safeReports)
            









