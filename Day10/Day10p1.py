contents = []
sum=0
x=1
cycle=0
nextSection=20
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day10\inputpuzzle.txt", "r")
contents = f.readlines()
f.close() 


i=0
while i < len(contents):
    contents[i] = contents[i].strip().split(' ')
    i += 1

i=0
while i < len(contents):
    if contents[i][0]=='addx':
        cycle += 2
        if cycle > nextSection:
            sum += x*nextSection
            nextSection +=40
        x += int(contents[i][1])
    else: cycle += 1    
    i += 1

print(sum)