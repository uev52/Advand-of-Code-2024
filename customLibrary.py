def readFile(fname):
    if type(fname) != str():
        fname = str(fname)
        if '.txt' not in fname:
            fname = fname+'.txt'

    with open(fname,'r') as listID:
        content = listID.readlines()
    
    return content


def checkReportRules(report):
    sameDirectionList = []
    oneDirection = all(int(report[i]) < int(report[i+1]) for i in range(len(report) - 1)) or \
    all(int(report[i]) > int(report[i+1]) for i in range(len(report) - 1))
    
    
    if oneDirection == True:
        sameDirectionList.append(report)
    

    print(sameDirectionList)
    for report in sameDirectionList:
        #print()
        #print()
        #print(report)
        reportDifferance = []
        for level in range(len(report)-1):
            if level != len(report):
                differance = int(report[level]) - int(report[level+1])
                if differance < 0:
                    differance = differance * -1

                if differance < 1 or differance > 3:
                    differance = 'unsafe'
                
                
                reportDifferance.append(differance)


        acceptableDifferance = [1,2,3]
        #print("diff____")
        
        with open("unsafe.txt","a") as file:
            file.writelines(str(reportDifferance)+"\n")


    with open('unsafe.txt','r') as unsafefile:
        unsafeReports = unsafefile.readlines()
        oneWay = len(unsafeReports)
        counter = 0
        for item in unsafeReports:
            test= item[1:-2].split(",")
            

            if "'unsafe'" in test:
                counter = counter +1
                
    safeReports = oneWay - counter

    return print(safeReports)
        


     



