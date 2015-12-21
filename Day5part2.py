import re

fileHandle = open('/Users/waltergibbons/Desktop/Day5.txt')
contents = fileHandle.readlines()

pattern1 = "\\b\w*(\w{2})\w*\\1"
pattern2 = "(.).\\1"
#pattern3 = "ab|cd|pq|xy"
count = 0

print "\nAnswers for:", pattern1
for i in range(0, contents.__len__()):
    if re.search(pattern1, contents[i]):
        if re.search(pattern2, contents[i]):
            count += 1
    #print i,

print count