import itertools

filehandle = open("/Users/waltergibbons/Desktop/Day9.txt", 'r')
contents = filehandle.readlines()
filehandle.close()

dict = {}
uniqList = []

for i in range(0, contents.__len__()):
    tempStr = str(contents[i]).split()

    tempStr.pop(1)
    tempStr.pop(2)
    #tempStr.pop(2)
    dict[str(tempStr[0] + tempStr[1])] = int(tempStr[2])
    dict[str(tempStr[1] + tempStr[0])] = int(tempStr[2])

    #print(tempStr[0])
    contents[i] = tempStr
    if contents[i][0] not in uniqList:
        uniqList.append(contents[i][0])
    elif contents[i][1] not in uniqList:
        uniqList.append(contents[i][1])

permCityList = []
i = 1

for p in itertools.permutations(uniqList, 8):
    permCityList.append(p)

def CalculateTourDist(cityList):
    totalDist = 0
    for i in range(0, cityList.__len__()-1):
        totalDist = totalDist + dict[cityList[i] + cityList[i+1]]
    return totalDist

shortest = 0
for i in range(0, permCityList.__len__()):
    if CalculateTourDist(permCityList[i]) >= shortest:
        shortest = CalculateTourDist(permCityList[i])
        print(shortest)
print "Shortest Route is:", shortest, "miles"

print CalculateTourDist(permCityList[1])
