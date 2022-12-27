contents = []
hasPassed = [[True]]
iHead= [0, 0]
i1= [0, 0]
i2= [0, 0]
i3= [0, 0]
i4= [0, 0]
i5= [0, 0]
i6= [0, 0]
i7= [0, 0]
i8 = [0, 0]
iTail = [0, 0]
count=1
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day9\inputpuzzle1.txt", "r")
contents = f.readlines()
f.close() 


i=0
while i < len(contents):
    contents[i] = contents[i].strip().split(' ')
    i += 1

def moveHead():
    
        if contents[i][0] == 'L':
            iHead[1] -= 1
            if iHead[1] < 0: 
                extendList(iHead[1], 0)
                iHead[1] = 0
        elif contents[i][0] == 'D':
            iHead[0] += 1
            if iHead[0] > len(hasPassed)-1:
                appendList(1-iHead[0]-(len(hasPassed)), 0)
        elif contents[i][0] == 'U':
            iHead[0] -= 1
            if iHead[0] < 0: 
                extendList(0, iHead[0])
                iHead[0] = 0
        else:
            iHead[1] += 1
            if iHead[1] > len(hasPassed[0])-1:
                appendList(0, (len(hasPassed[0])-1)-iHead[1])


def moveNext(iprev, inext):
    while abs(iprev[0]-inext[0]) > 1 or abs(iprev[1]-inext[1]) > 1:
        if iprev[1] > inext[1]:
            if iprev[0] > inext [0]:
                inext[1] += 1
                inext[0] += 1
            elif iprev[0] < inext [0]:
                inext[1] += 1
                inext[0] -= 1
            else:
                inext[1] += 1
        elif iprev[1] < inext[1]:
            if iprev[0] > inext [0]:
                inext[1] -= 1
                inext[0] += 1
            elif iprev[0] < inext [0]:
                inext[1] -= 1
                inext[0] -= 1
            else:
                inext[1] -= 1
        elif iprev[0]-1 > inext [0]:
            inext[0] += 1
        else:
            inext[0] -= 1
        if inext == iTail:  checkPassed()            

def appendList(r,c):
    while c < 0:
        k=0
        while k < len(hasPassed):
            hasPassed[k].append(False)
            k += 1
        c += 1
    while r < 0:
        k=0
        temp = []
        while k < len(hasPassed[-1]):
            temp.append(False)
            k += 1
        hasPassed.append(temp)
        r += 1
        del temp
def extendList(z,y):
    fixKnots(z,y)
    while z < 0:
        k=0
        while k < len(hasPassed):
            hasPassed[k].insert(0, False)
            k += 1
        z += 1
    while y < 0:
        k=0
        temp = []
        while k < len(hasPassed[-1]):
            temp.append(False)
            k += 1
        hasPassed.insert(0, temp)
        y += 1
        del temp
def fixKnots(z,y):
    iTail[1] -= z
    iTail[0] -= y
    i1[1] -= z
    i1[0] -= y
    i2[1] -= z
    i2[0] -= y
    i3[1] -= z
    i3[0] -= y
    i4[1] -= z
    i4[0] -= y
    i5[1] -= z
    i5[0] -= y
    i6[1] -= z
    i6[0] -= y
    i7[1] -= z
    i7[0] -= y
    i8[1] -= z
    i8[0] -= y
def checkPassed():
    if not hasPassed[iTail[0]][iTail[1]]:
        hasPassed[iTail[0]][iTail[1]] = True
        global count
        count += 1

i=0
while i < len(contents):
    while int(contents[i][1]) > 0:
        moveHead()
        moveNext(iHead, i1)
        moveNext(i1, i2)
        moveNext(i2, i3)
        moveNext(i3, i4)
        moveNext(i4, i5)
        moveNext(i5, i6)
        moveNext(i6, i7)
        moveNext(i7, i8)
        moveNext(i8, iTail)
        contents[i][1] = int(contents[i][1])-1
    i += 1
    
print(count)