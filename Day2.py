
fileHandle = open('/Users/waltergibbons/Desktop/Day2.txt')

contents = fileHandle.readlines()
#i = 0

lines = contents.__len__()
totalArea = 0

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

    dimensions = [ length, width, height ]
    dimensions.sort()
    print dimensions
    area = (2 * int(length) *int(width)) + (2 * int(width) * int(height)) + (2 * int(height) * int(length)) + dimensions[0]*dimensions[1]
    print "Length", length, "Width", width, "Height", height, "Area", area
    totalArea = totalArea + area

print "Total Area", totalArea