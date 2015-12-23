import re
fileHandle = open('/Users/waltergibbons/Desktop/Day8.txt')

contents = fileHandle.readlines()

countChars = 0

for i in range(0, contents.__len__()):
    contents[i] = contents[i].strip('\n')
    countChars += contents[i].__len__()
    #print contents[i], contents[i].__len__()

def processQuotes(line):
    line = line.lstrip('"')
    line = line.rstrip('"')
    line = line.replace('\\"', 'Q')
    line = line.replace('\\\\', 'S')
    line = re.sub(r"\\x..", 'X', line)
    return line

for i in range(0,contents.__len__()):
    #print contents[i], "len= ", contents[i].__len__()
    contents[i] = processQuotes(contents[i])
    #print "", contents[i], " len= ", contents[i].__len__()

ctr = 0
for i in range(0, contents.__len__()):
    ctr += contents[i].__len__()

print "Begining Count:", countChars
print "Total Count:", ctr
print "Answer:", countChars - ctr
