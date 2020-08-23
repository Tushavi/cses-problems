s = input()
n = len(s)
di = {}
for ch in s :
    di[ch] = di.get(ch,0) + 1
odd = False
ans = [0]*n
filled = 0
for k,v in di.items() :
    if v%2 == 1 :
        if odd :
            ans = 'NO SOLUTION'
            break
        odd = True
        ans[n//2] = k
        v -= 1
    ans[filled:filled+v//2] = [k]*(v//2)
    ans[-1-filled:-1-filled-v//2:-1] = [k]*(v//2)
    filled += v//2
print(''.join(ans))
