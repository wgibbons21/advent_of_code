
fileHandle = open("/Users/waltergibbons/Desktop/Day3.txt")
contents = fileHandle.read()

location = [0, 0]
dict = {}

print contents.__len__(), "Characters in file"

for i in range(0, contents.__len__(), 2):
    print "Santa moves", i
    string = str(location)
    if  contents[i] == ">":
        print "Santa moved right"
        location[0] = location[0] + 1
        dict[string] = 1;
    elif contents[i] == "<":
        print "Santa moved left"
        location[0] = location[0] - 1
        dict[string] = 1;
    elif contents[i] == "^":
        print "Santa moved up"
        location[1] = location[1] + 1
        dict[string] = 1;
    elif contents[i] == "v":
        print "Santa moved down"
        location[1] = location[1] - 1
        dict[string] = 1;
    #print string


location = [0, 0]
for i in range(1, contents.__len__(), 2):
    print "RoboSanta moves", i
    string = str(location)
    if  contents[i] == ">":
        print "RoboSanta moved left"
        location[0] = location[0] + 1
        dict[string] = 1;
    elif contents[i] == "<":
        print "RoboSanta moved right"
        location[0] = location[0] - 1
        dict[string] = 1;
    elif contents[i] == "^":
        print "RoboSanta moved down"
        location[1] = location[1] + 1
        dict[string] = 1;
    elif contents[i] == "v":
        print "RoboSanta moved up"
        location[1] = location[1] - 1
        dict[string] = 1;
    #print string

print dict.__len__(), "Houses Visited"
#print dict
print "Final Location", location


