filehandle = open("/Users/waltergibbons/Desktop/Day9.txt")

contents = filehandle.readlines()
filehandle.close()


for i in range(0, contents.__len__()):
    contents[i] = contents[i].split()
    contents[i] = contents[i].
    print contents[i]
