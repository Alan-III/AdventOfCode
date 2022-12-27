contents = []
hasPassed = [[True]]
iHead = [0, 0]
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
        iHead[1] -= int(contents[i][1])
        if iHead[1] < 0: 
            extendList(iHead[1], 0)
            iHead[1] = 0
    elif contents[i][0] == 'D':
        iHead[0] += int(contents[i][1])
        if iHead[0] > len(hasPassed)-1:
            appendList(1-iHead[0]-(len(hasPassed)), 0)
    elif contents[i][0] == 'U':
        iHead[0] -= int(contents[i][1])
        if iHead[0] < 0: 
            extendList(0, iHead[0])
            iHead[0] = 0
    else:
        iHead[1] += int(contents[i][1])
        if iHead[1] > len(hasPassed[0])-1:
            appendList(0, (len(hasPassed[0])-1)-iHead[1])

def moveTail():
    while abs(iHead[0]-iTail[0]) > 1 or abs(iHead[1]-iTail[1]) > 1:
        if iHead[1] > iTail[1]:
            if iHead[0] > iTail [0]:
                iTail[1] += 1
                iTail[0] += 1
            elif iHead[0] < iTail [0]:
                iTail[1] += 1
                iTail[0] -= 1
            else:
                iTail[1] += 1
        elif iHead[1] < iTail[1]:
            if iHead[0] > iTail [0]:
                iTail[1] -= 1
                iTail[0] += 1
            elif iHead[0] < iTail [0]:
                iTail[1] -= 1
                iTail[0] -= 1
            else:
                iTail[1] -= 1
        elif iHead[0]-1 > iTail [0]:
            iTail[0] += 1
        else:
            iTail[0] -= 1
        checkPassed()            

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
    iTail[1] -= z
    iTail[0] -= y
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

def checkPassed():
    if not hasPassed[iTail[0]][iTail[1]]:
        hasPassed[iTail[0]][iTail[1]] = True
        global count
        count += 1

i=0
while i < len(contents):
    moveHead()
    moveTail()
    i += 1

print(count)