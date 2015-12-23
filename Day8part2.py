import re
fileHandle = open('/Users/waltergibbons/Desktop/Day8.txt')

contents = fileHandle.readlines()
countChars = 0
length = len(contents)

for i in range(0, length):
    contents[i] = contents[i].strip('\n')
    countChars += len(contents[i])

def processQuotes(line):
    #line = line.lstrip('"')
    #line = line.rstrip('"')
    print "Before", line, len(line)
    line = line.replace('\"', 'QQ')
    line = line.replace('"', 'QQQ')
    line = line.replace('\\', 'SS')
    #line = line.lstrip('"')
    #line = line.rstrip('"')
    print "After", line, len(line)
    return line

for i in range(0, length):
    #print contents[i], "len=", len(contents[i])
    contents[i] = processQuotes(contents[i])
    #print contents[i], "len=", len(contents[i])

ctr = 0
for i in range(0, length):
    ctr += len(contents[i]) + 2

print "Begining Count:", countChars
print "Total Count:", ctr
print "Answer:", ctr - countChars
