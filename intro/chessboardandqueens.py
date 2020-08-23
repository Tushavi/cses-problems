size = 8

def boolify(arr) :
    return [i=='.' for i in arr]

def copy(arr2d) :
    a = []
    for i in arr2d :
        a.append(i.copy())
    return a

def placedat(b, col, row) :
    b[row][col] = False
    for i in range(row+1, size) :
        b[i][col] = False
        if col+row-i >= 0 :
            b[i][col+row-i] = False
        if col-row+i < size :
            b[i][col-row+i] = False
    return b

def doit(grid,row,count) :
    if row>=size :
        return count + 1
    for i in range(size) :
        if grid[row][i] :
            count = doit(placedat(copy(grid),i,row),row+1,count)
    return count

board = [boolify(list(input())) for _ in range(size)]
print(doit(board,0,0))
