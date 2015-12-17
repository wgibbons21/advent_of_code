
data = open('/Users/waltergibbons/Desktop/Day1.txt')

contents = data.read()

i = 0
ctr = 0
basement = 0
for i in range(0, 7000):
    if contents[i] == '(':
        #print "Encounted", contents[i] , "Floor", ctr
        ctr = ctr + 1
    elif contents[i] == ')':
        #print "Encounted", contents[i] , "Floor", ctr
        ctr = ctr - 1

    if ctr == -1:
        print(i+1)

print "Floor", ctr, "Entered basement at:", basement
