n = int(input())
if n%4 in {1,2} :
    print('NO')
else :
    print('YES')
    a = []
    b = []
    if n%2 == 0 :
        for i in range(1,1+n//2) :
            if i%2 == 0 :
                a += [i,n-i+1]
            else :
                b += [i,n-i+1]
        print(n//2)
        print(' '.join([str(x) for x in a]))
        print(n//2)
        print(' '.join([str(x) for x in b]))
    else :
        a = [1,n-1]
        b = [n]
        for i in range(2,1+n//2) :
            if i%2 == 0 :
                a += [i,n-i]
            else :
                b += [i,n-i]
        print(1+n//2)
        print(' '.join([str(x) for x in a]))
        print(n//2)
        print(' '.join([str(x) for x in b]))
