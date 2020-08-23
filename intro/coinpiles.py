for _ in range(int(input())) :
    a,b = (int(x) for x in input().split())
    if (a+b)%3 == 0 and a<=2*b and 2*a>=b :
        print('YES')
    else :
        print('NO')
