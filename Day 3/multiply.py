import sys
sys.path.insert(0, '/Users/ethem/Documents/GitHub/Advand-of-Code-2024')

from customLibrary import readFile

content = readFile('input')
content = "".join(content)
splitString = content.split("mul(")

filteredValues = []
for item in splitString:
    value = item.split(")")
    if len(value[0]) >= 3 and len(value[0]) <= 7:
        filteredValues.append(value[0])

fixedCorruption = []
for item in filteredValues:
    mulValues = item.split(",")
    fixedCorruption.append(mulValues)

mulResult = []
for item in fixedCorruption:

    if len(item) == 2:
        mulVal = int(item[0]) * int(item[1])
        mulResult.append(mulVal)

sumMul = sum(mulResult)

print(sumMul)
