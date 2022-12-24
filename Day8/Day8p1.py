contents = []
isVisible = []
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
    isVisible.append([])
    j=0
    while j < len(contents[i]):
        trees[i].append(int(contents[i][j]))
        isVisible[i].append(False)
        j += 1
    i += 1

i=0 #comparizon
while i < len(contents):
    end = len(contents[i])-1
    j=0
    push = 1
    isVisible[i][0] = isVisible[i][len(contents[i])-1] = True
    while j+push <= end:
        if  trees[i][j] <= trees[i][end]:
            if trees[i][j+push] > trees[i][j]:
                isVisible[i][j+push] = True
                j += push
                push = 1
            else:
                push += 1
        else:
            if trees[i][end-push] > trees[i][end]:
                isVisible[i][end-push] = True
                end -= push
                push = 1
            else:
                push += 1
    i += 1

i=1   # column comparizon
while i < len(contents[0])-1:
    end = len(contents[0])-1
    j=0
    push = 1
    isVisible[0][i] = isVisible[len(contents)-1][i] = True
    while j+push <= end:
        if  trees[j][i] <= trees[end][i]:
            if trees[j+push][i] > trees[j][i]:
                isVisible[j+push][i] = True
                j += push
                push = 1
            else:
                push += 1
        else:
            if trees[end-push][i] > trees[end][i]:
                isVisible[end-push][i] = True
                end -= push
                push = 1
            else:
                push += 1
    i += 1

i = count = 0  #count not visible
while i < len(contents):
    j=0
    while j < len(contents[i]):
        if isVisible[i][j]:
            count +=1
        j += 1
    i += 1

print(count)