def readFile(fname):
    if type(fname) != str():
        fname = str(fname)
        if '.txt' not in fname:
            fname = fname+'.txt'

    with open(fname,'r') as listID:
        content = listID.readlines()
    
    return content

def checkReportRules(report):
    for level in report:
        return print(level)
    