import sys
sys.path.insert(0, '/Users/ethem/Documents/GitHub/Advand-of-Code-2024')

from customLibrary import readFile, checkReportRules

reports = readFile('reports.txt')

for report in reports:
    #report = [report] # Cast to list
    if type(report) != list:
        report = report.split(" ") # Cast to list and split string into correct elements

    checkReportRules(report)

