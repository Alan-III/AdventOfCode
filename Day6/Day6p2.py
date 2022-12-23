contents = []
readable = True
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day6\inputpuzzle1.txt", "r")
while readable:
    line = f.readline()
    if line == '':
        readable = False
    else:
        contents.append(line)
f.close() 

def compare():
    j=k=0
    while j < 14:
        k = j+1
        while k < 14:
            if x[j]==x[k]:
                return False
            k += 1
        j += 1
    return True

i=0
x = []
while i < len(contents[0]):
    if i < 14:
        x.append(contents[0][i])
    else:
        if compare():
            print(i)
            i = 10000
        else:
            del x[0]
            x.append(contents[0][i])
    i += 1