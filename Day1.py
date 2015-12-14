
data = open('/Users/waltergibbons/Desktop/Day1.txt')

contents = data.read()

print contents.__len__()

i = 0
ctr = 0

for i in range(0, 7000):
    if contents[i] == '(':
        print "Encounted", contents[i] , "Floor", ctr
        ctr = ctr + 1
    else:
        if contents[i] == ')':
            print "Encounted", contents[i] , "Floor", ctr
            ctr = ctr - 1


print "Counter", ctr
