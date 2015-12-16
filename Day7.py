fileHandle = open('/Users/waltergibbons/Desktop/Day7.txt')

contents = []
contents = fileHandle.readlines()
contents.sort()
for i in range(0, contents.__len__()):
    contents[i] = contents[i].split()
dict = {}

for j in range(0, 100):    #process pre-computed
    for i in range(0,contents.__len__()):
        if contents[i][1] == '->' and contents[i][0][0].isdigit():
            dict[contents[i][2]] =  int(contents[i][0])

        if contents[i][1] == '->' and contents[i][0] in dict:
            dict[contents[i][2]] = int(dict[contents[i][0]])
        if contents[i][0] == 'NOT' and (contents[i][1] in dict):
            dict[contents[i][3]] = int(dict[contents[i][1]]) ^ 65535
        if contents[i][1] == 'LSHIFT' and (contents[i][0] in dict):
            dict[contents[i][4]] = (65535 & (int(dict[contents[i][0]]) << int(contents[i][2])))
        if contents[i][1] == 'RSHIFT' and (contents[i][0] in dict):
            dict[contents[i][4]] = (65535 & (int(dict[contents[i][0]]) >> int(contents[i][2])))
        if contents[i][1] == 'AND' and contents[i][0] in dict and contents[i][2] in dict:
            dict[contents[i][4]] = int(dict[contents[i][0]]) & int(dict[contents[i][2]])
        if contents[i][1] == 'AND' and contents[i][2] in dict and contents[i][0].isdigit():
            dict[contents[i][4]] = 1 & int(dict[contents[i][2]])
        if contents[i][1] == 'OR' and contents[i][0] in dict and contents[i][2] in dict:
            dict[contents[i][4]] = int(dict[contents[i][0]]) | int(dict[contents[i][2]])

print "\nValue of 'a' is", dict['a']

