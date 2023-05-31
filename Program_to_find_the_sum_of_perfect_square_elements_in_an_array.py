def fun(n):
    t=n**0.5
    if (n%t==0):
        return True
    else:
        return False
n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    if fun(i):
        s+=i
print(s)