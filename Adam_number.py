def rev(x):
    r=0
    while x:
        s=x%10
        r=r*10+s
        x=x//10
    return r
n=int(input())
s=n*n
x=rev(n)
sm=x*x
smm=rev(sm)
if smm==s:
    print("True")
else:
    print("False")