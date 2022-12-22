contents = []
readable = True
f = open("E:\\repos\AdventOfCode\Day5\inputpuzzle1.txt", "r")
while readable:
    line = f.readline()
    if line == '':
        readable = False
    contents.append(line)
f.close()        
stacks = { 
    '1': ['G','F','V','H','P','S'],
    '2': ['G','J','F','B','C','D','Z','M'],
    '3': ['G','M','L','J','N'],
    '4': ['N','G','Z','V','D','W','P'],
    '5': ['V','R','C','B'],
    '6': ['V','R','S','M','P','W','L','Z'],
    '7': ['T','H','P'],
    '8': ['Q','R','S','N','C','H','Z','V'],
    '9': ['F','L','G','P','V','Q','J']
}
x = []
i=j=0
while i < len(contents)-1:
    x = contents[i].split(' ')
    x[5] = x[5].strip()
    cratein = len(stacks[x[3]]) - int(x[1])
    while j < int(x[1]):
        stacks[x[5]].append(stacks[x[3]][cratein])
        del stacks[x[3]][cratein]
        j += 1
    x.clear()
    i += 1
    j = 0

print(stacks)