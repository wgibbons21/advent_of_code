import re

fileHandle = open('/Users/waltergibbons/Desktop/Day5.txt')
contents = fileHandle.readlines();

pattern1= "(\\w)\\1+"
pattern2= "[aeiou].*[aeiou].*[aeiou].*"
pattern3= "ab|cd|pq|xy"
count = 0

print "Has 2 or more of the same character:"
for i in range(0, contents.__len__()):
    if re.search(pattern1 , contents[i]):
        print(contents[i]),

print "\nHas 3 or more vowels:"
for i in range(0, contents.__len__()):
    if re.search(pattern2 , contents[i]):
        print(contents[i]),

print "\nHas naughty pattern:"
for i in range(0, contents.__len__()):
    if re.search(pattern3 , contents[i]):
        print(contents[i]),


print "\nAnswers:"
for i in range(0, contents.__len__()):
    if re.search(pattern1 , contents[i]):
        if re.search(pattern2 , contents[i]):
           if not re.search(pattern3, contents[i]):
               count +=1
               print  contents[i],

print count