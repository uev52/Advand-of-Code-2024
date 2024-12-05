def readFile(fname):
    if type(fname) != str():
        fname = str(fname)
        if '.txt' not in fname:
            fname = fname+'.txt'

    with open(fname,'r') as listID:
        content = listID.readlines()
    
    return content

def txtToList(fname):
    content = readFile(fname)

    return content

def stringToList(string):
    dividers = [" ", ",","-",", "," ,"," -","- ","  "," - "," , "]
    if type(string) != list:
        for divider in dividers:
            if divider in string:
                myList = string.split(divider)
    
    return myList
    

def increaseDecrease(report):
    sameDirectionList = []
    increaseOrDecrease = all(int(report[i]) < int(report[i+1]) for i in range(len(report) - 1)) or \
    all(int(report[i]) > int(report[i+1]) for i in range(len(report) - 1))
    
    
    if increaseOrDecrease == True:
        return report
    else:
        return False

def findValidDiffCount(reports, onlyIncrease):
    checkedReports = []
    unsafereports = []
    for report in reports:
        validatedReport = []
        for differance in report:
            if differance >0 and differance <=3:
                validatedReport.append(True)
            else:
                validatedReport.append(False)
        checkedReports.append(validatedReport)
    
    safeReportCounter= 0
    indexCounter = -1

    for report in checkedReports:
        indexCounter += 1
        if False in report:
            unsafereports.append(onlyIncrease[indexCounter])
        else:
            safeReportCounter += 1
            

    return safeReportCounter, unsafereports


def problemDampener(reports, onlyIncrease, invalidReports):
    unsafeReports = findValidDiffCount(reports, onlyIncrease)
    unsafeReports2 = []
    for index in invalidReports:
        unsafeReports2.append(onlyIncrease[index])

    allUnsafeReports = unsafeReports[1]+ unsafeReports2

    for report in allUnsafeReports:
        indexCounter= 0
        differanceReport = []
        for level in report:
            differance = int(report[indexCounter]) - int(report[indexCounter+1])
        
            
            if differance < 0:
                differance = differance * -1
            
            differanceReport.append(differance)

            if indexCounter != len(report)-2:
                indexCounter += 1

        print(differanceReport)

