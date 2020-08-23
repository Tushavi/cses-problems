n = int(input())
def ways(n) :
    return n*n*(n*n-1)//2
di = {1:0, 2:6, 3:28, 4:96, 5:252, 6:550, 7:1056, 8:1848}
for i in range(1,n+1) :
    if i not in di :
        mx = ways(i)
        corners = 8 # 4*2
        subcorn = 48 # 4*2*(3+3)
        edges = 4*(i-6)*4
        di[i] = mx-corners-subcorn-edges - (ways(i-2) - di[i-2])
    print(di[i])
