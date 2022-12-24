contents = []
scenicScore = []
trees = []
readable = True
f = open("C:\\Users\Alan\Documents\Repos\AdventOfCode\Day8\inputpuzzle1.txt", "r")
contents = f.readlines()
f.close() 

i=0
while i < len(contents):
    contents[i] = contents[i].strip()
    i += 1

i=0  #initialize grids
while i < len(contents):
    trees.append([])
    scenicScore.append([])
    j=0
    while j < len(contents[i]):
        trees[i].append(int(contents[i][j]))
        scenicScore[i].append(1)
        j += 1
    i += 1

i=j=1
b=1
bN = bE = bW = bS = False
while i < len(trees)-1:
    j=1
    while j < len(trees[0])-1:
        bN = bE = bW = bS = False
        while not (bN and bE and bW and bS):
            if not bN:
                if i-b == 0:
                    bN = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                elif int(trees[i-b][j]) >= int(trees[i][j]):
                    bN = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                else:   b += 1
            elif not bE:
                if j+b == len(trees[i])-1:
                    bE = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                elif int(trees[i][j+b]) >= int(trees[i][j]):
                    bE = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                else:   b += 1
            elif not bW:
                if j-b == 0:
                    bW = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                elif int(trees[i][j-b]) >= int(trees[i][j]):
                    bW = True
                    scenicScore[i][j] = scenicScore[i][j] * b
                    b=1
                else:   b += 1
            else:
                if i+b == len(trees)-1:
                    bS = True
                    scenicScore[i][j] *= b
                    b=1
                elif int(trees[i+b][j]) >= int(trees[i][j]):
                    bS = True
                    scenicScore[i][j] *= b
                    b=1
                else:   b += 1
        j += 1
    i += 1

i=j=1
max=0
while i < len(trees)-1:
    j=1
    while j < len(trees[0])-1:
        if scenicScore[i][j] > max: max = scenicScore[i][j]
        j += 1
    i += 1
print(max)