fileHandle = open("/Users/waltergibbons/Desktop/Day6.txt")

contents = fileHandle.readlines()

instruction = [[0 for x in xrange(5)] for x in xrange(contents.__len__())]
grid = [[0 for x in xrange(1000)] for x in xrange(1000)] #create 1000x1000 grid

for i in range(0, contents.__len__()):              #iterates through the input file parsing it into a list 2D list of 5 elements                                     #set element 0 in list to the action
    if str(contents[i]).__contains__('on'):         #instruction[ "on", begin X, begin Y, end X, end Y]
        instruction[i][0] = 'on'
    elif str(contents[i]).__contains__('off'):
        instruction[i][0] = 'off'
    elif str(contents[i]).__contains__('toggle'):
        instruction[i][0] = 'toggle'

    #chop up list
    strList = str(contents[i]).split()
    strList.pop(0)
    if strList.__len__() == 3:
        strList.pop(1)
    else:
        strList.pop(0)
        strList.pop(1)

    #assign elements to 2D list array
    instruction[i][1] = int (strList[0].partition(',')[0])
    instruction[i][2] = int (strList[0].partition(',')[2])
    instruction[i][3] = int (strList[1].partition(',')[0])
    instruction[i][4] = int (strList[1].partition(',')[2])

for i in range(0, instruction.__len__()):                       #iterate through each line of instruction
    for j in range(instruction[i][1], instruction[i][3]+1):     #move over each x value
        for k in range(instruction[i][2], instruction[i][4]+1): #move over each y value for each x value
            if instruction[i][0] == 'on':
                #rint "Instruction is on, current value:", grid[j][k]
                grid[j][k] += 1
            elif instruction[i][0] == 'off':
                if grid[j][k] > 0:
                    #print "Instruction is off, current value:", grid[j][k]
                    grid[j][k] -= 1
            elif instruction[i][0] == 'toggle':
                #print "Instruction is toggle, current value:", grid[j][k]
                grid[j][k] += 2


ctr = 0                                         #use to tally light turned on

for j in range(0, 1000):                        #count up light "on" in grid
    for k in range (0, 1000):
        ctr += grid[j][k]

print "Total light on", ctr