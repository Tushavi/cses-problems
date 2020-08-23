n = int(input())
if n == 1 :
    print(1)
elif n < 4 :
    print('NO SOLUTION')
else :
    arr =  [str(2*i+2) for i in range(n-(n+1)//2)]
    arr += [str(2*i+1) for i in range((n+1)//2)]
    print(' '.join(arr))
