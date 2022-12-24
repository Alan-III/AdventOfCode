contents = []
readable = True
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day7\inputpuzzle1.txt", "r")
while readable:
    line = f.readline()
    if line == '':
        readable = False
    else:
        contents.append(line)
f.close() 

i=2
dirs = [["/",0]]
line = []
tempsize = 0
dirorder = [0]

while i < len(contents):
    line = contents[i].split(' ')
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2].strip() == '..':
                #add size to up dir
                dirs[dirorder[len(dirorder)-2]][1] += int(dirs[dirorder[len(dirorder)-1]][1])
                del dirorder[len(dirorder)-1]
            else:
                i += 1
                dirs.append([line[2].strip(),0])
                dirorder.append(len(dirs)-1)
                
    elif line[0] == 'dir':
        #add dir name to list of tempkey
        dirs[dirorder[len(dirorder)-1]].append(line[1].strip())
    else:
        #add number to size
        dirs[dirorder[len(dirorder)-1]][1] += int(line[0])
    i += 1

while len(dirorder)-1 > 0:
    dirs[dirorder[len(dirorder)-2]][1] += int(dirs[dirorder[len(dirorder)-1]][1])
    del dirorder[len(dirorder)-1]

k = 1
spaceneeded = abs(70000000 - dirs[0][1] - 30000000)
tempspace = 70000000
while k < len(dirs):
    if dirs[k][1] >= spaceneeded and tempspace > dirs[k][1]:
        tempspace = dirs[k][1]
    k += 1
print(tempspace)