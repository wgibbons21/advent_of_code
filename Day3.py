
fileHandle = open("/Users/waltergibbons/Desktop/Day3.txt")
contents = fileHandle.read()

location = [0,0]
dict = {}

print contents.__len__(), "Characters in file"
for i in range(0, contents.__len__()):
    string = str(location)
    if   contents[i] == ">":
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

print dict.__len__(), "Houses Visited"
print "Final Location", location


