def fun(c):
    s=0
    while c:
        r=c%10
        s+=1
        c=c//10
    return s
n=int(input())
k=list(map(int,input().split()))
h=max(k)
v=fun(h)
sm=0
for i in k:
    r=fun(i)
    if r==v:
        sm+=1
print(sm)