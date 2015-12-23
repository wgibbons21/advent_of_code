
looksay = '1321131112'

def lookSayFun(looksay):
    i = 0
    newlooksay = ''
    for r in range(0, 1):
        while i < len(looksay) - 1:
            ctr = 1
            while looksay[i] == looksay[i+1]:
                ctr += 1
                i += 1
            else:
                newlooksay += str(ctr) + str(looksay[i])
            i += 1
        newlooksay += str(1) + str(looksay[i])
    return newlooksay

for i in range(0, 50):
    looksay = lookSayFun(looksay)

print "Length", len(looksay)

