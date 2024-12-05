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

def findValidDiffCount(reports):
    checkedReports = []
    for report in reports:
        validatedReport = []
        for differance in report:
            if differance >0 and differance <=3:
                validatedReport.append(True)
            else:
                validatedReport.append(False)
        checkedReports.append(validatedReport)
    
    safeReportCounter= 0 
    for report in checkedReports:
        
        if False in report:
            safeReportCounter = safeReportCounter
        else:
            safeReportCounter += 1
            print(report)

    return print(safeReportCounter)

     



