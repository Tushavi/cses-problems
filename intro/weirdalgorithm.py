n = int(input())
arr = [str(n)]
def func(num) :
    if num%2==0 :
        return num//2
    else :
        return num*3+1
while n!=1 :
    n = func(n)
    arr.append(str(n))
print(' '.join(arr))
