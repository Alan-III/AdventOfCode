contents = []
sum=0
x=1
cycle=0
nextSection=40
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day10\inputpuzzle.txt", "r")
contents = f.readlines()
f.close() 


i=0
while i < len(contents):
    contents[i] = contents[i].strip().split(' ')
    i += 1
def draw():
    if abs(x-cycle) <= 1:
        f.write('#')
    else: f.write('.')

i=0
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day10\CRToutput.txt", 'w')
while i < len(contents):
    draw()
    if contents[i][0]=='addx':
        cycle += 1
        if cycle == nextSection: 
            f.write('\n')
            cycle = 0
        draw()
        cycle += 1
        if cycle == nextSection: 
            f.write('\n')
            cycle = 0           
        x += int(contents[i][1])
    else: 
        cycle += 1
        if cycle == nextSection: 
            f.write('\n')
            cycle = 0   
    i += 1
f.close() 