n = int(input())
arr = [int(x) for x in input().split()]
res = 0
mr = -1
for i in arr :
    mr = max(i,mr)
    res += mr-i
print(res)
