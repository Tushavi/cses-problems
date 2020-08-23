for _ in range(int(input())) :
    row,col = (int(x) for x in input().split())
    sq = max(row,col)
    start_right = sq%2==0
    a = (sq-1)*(sq-1)
    l = sq*sq
    if start_right :
        if col == sq :
            print(a+row)
        else :
            print(l-col+1)
    else :
        if row == sq :
            print(a+col)
        else :
            print(l-row+1)
