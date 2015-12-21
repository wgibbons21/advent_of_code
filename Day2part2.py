
fileHandle = open('/Users/waltergibbons/Desktop/Day2.txt')

contents = fileHandle.readlines()
#i = 0

lines = contents.__len__()
totalLength = 0

for i in range(0 , lines):
    length = contents[i].partition('x')[0]
    width  = contents[i].partition('x')[2]
    width  = width.partition('x')[0]
    height = contents[i].partition('x')[2]
    height = height.partition('x')[2]
    height = height.partition('\n')[0]

    length = int(length)
    height = int(height)
    width  = int(width)

    dimensions = [length, width, height]
    dimensions.sort()
    print dimensions
    totalLength = totalLength + (dimensions[0]*2 + dimensions[1]*2) + dimensions[0]*dimensions[1]*dimensions[2]

print "Total Length of Ribbon", totalLength