#
# PART 1 of Challange
#

with open('locationID.txt','r') as listID:
    content = listID.readlines()

list1 = []
list2 = []

for id in content:
    row = id.split(" ")
    list1.append(int(row[0]))
    list2.append(int(row[-1]))

list1.sort()
list2.sort()

distanceList= []
if len(list1) == len(list2):
    for index in range(len(list1)):
        distance = int(list1[index]) - int(list2[index])
        if distance < 0:
            distance = distance * -1
        
        distanceList.append(distance)

#
# Part 2 of challange        
#

countList = []

for item in list1:
    counter = list2.count(item)
    countList.append(counter)

similarityScoreList = []
if len(countList) == len(list2):
    for index in range(len(list2)):
        similarityScore = list1[index] * countList[index]
        similarityScoreList.append(similarityScore)




