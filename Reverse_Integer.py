def fun(x):
    s=0
    while x:
        r=x%10
        s=s*10+r
        x=x//10
    return s
n=int(input())
c=0
if n<0:
    n=n*(-1)
    c+=1
    print(fun(n)*(-1))
else:
    print(fun(n))