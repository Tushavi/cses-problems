n = int(input())
arr = [int(x) for x in input().split()]
print((n*(n+1))//2 - sum(arr))
