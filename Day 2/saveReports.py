import sys
sys.path.insert(0, '/Users/ethem/Documents/GitHub/Advand-of-Code-2024')

from customLibrary import readFile, increaseDecrease, txtToList, stringToList, findValidDiffCount, problemDampener

# PART 1 ____________________________________________

stringOfReports = txtToList('reports')
listOfReports = []
unsafeReports = []

for report in stringOfReports:
    listReport = stringToList(report)
    listOfReports.append(listReport)

counter = -1
invalidIncreaseDecrease = []
onlyIncreasingOrDecreasing = []

for report in listOfReports:
    report = increaseDecrease(report)
    counter = counter + 1

    if report != False and report != None:
        onlyIncreasingOrDecreasing.append(report)
    if report == False:
        invalidIncreaseDecrease.append(counter)

for index in invalidIncreaseDecrease:
    unsafeReports.append(listOfReports[index])

differanceList = []
for report in onlyIncreasingOrDecreasing:
    indexCounter = 0

    differanceReport = []
    for level in report:
        differance = int(report[indexCounter]) - int(report[indexCounter+1])
        
        if differance < 0:
            differance = differance * -1

        differanceReport.append(differance)

        if indexCounter != len(report)-2:
            indexCounter += 1

    differanceList.append(differanceReport)

findValidDiffCount(differanceList,onlyIncreasingOrDecreasing)

# PART 2________________________________________________



#print(unsafeReports)

#print(onlyIncreasingOrDecreasing)


problemDampener(differanceList,onlyIncreasingOrDecreasing,invalidIncreaseDecrease)