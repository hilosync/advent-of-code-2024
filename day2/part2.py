reports = []

with open("input.txt") as input:
    for line in input:
        line.removesuffix("\n")
        reports.append([int(x) for x in line.split(" ")])

def checkIfSafe(report):
    if len(report) < 2:
        return True

    increasing = report[0] < report[1]
    i = 0
    while i < len(report) - 1:
        prev, curr = report[i], report[i+1]

        if increasing and prev > curr:
            return i
        elif not increasing and prev < curr:
            return i
        
        elif abs(prev - curr) < 1 or abs(prev - curr) > 3:
            return i

        i += 1
    return True


safeReports = 0
print(reports[1])
print(reports[1][:0] + reports[1][0+1:])
for report in reports:
    safetyReturn = checkIfSafe(report)
    if type(safetyReturn) is bool:
        safeReports += 1
    else:
        if type(checkIfSafe(report[:safetyReturn] + report[safetyReturn+1:])) is bool or type(checkIfSafe(report[:safetyReturn+1] + report[safetyReturn+2:])) is bool or type(checkIfSafe(report[1:])) is bool:
            safeReports += 1
    
print(safeReports)
            









