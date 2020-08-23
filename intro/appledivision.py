def partlist(arr, ins) :
    a = arr.copy()
    for i in ins[::-1] :
        del a[i]
    return a

def func(arr, cur, best_total, best_possible) :
    indices = []
    for i,v in enumerate(arr) :
        indices.append(i)
        cur += v
        if cur == best_possible or best_total == best_possible:
            return best_possible
        elif cur > best_possible :
            cur -= v
            continue
        else :
            best_total = max(best_total, func(partlist(arr,indices),cur,best_total,best_possible))
            cur -= v
    return max(best_total,cur)

n = int(input())
p = [int(x) for x in input().split()]
if n == 1 :
    print(p[0])
else :
    p = sorted(p,reverse=True)
    sump = sum(p)
    a = func(p, 0, 0, sump//2)
    print(sump - 2*a)
