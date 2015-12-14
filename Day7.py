fileHandle = open('/Users/waltergibbons/Desktop/Day7.txt')

contents = fileHandle.readlines()
contents.sort()
dict

for i in range(contents.__len__()):
    contents[i] = contents[i].split()

    #print contents[i][0][0].isdigit()

    if contents[i].__len__() == 3 and contents[i][0][0].isdigit():
        print contents[i]