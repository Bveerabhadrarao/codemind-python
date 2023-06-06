n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(len(l)):
    x=l.count(l[i])
    if c<x:
        c=x
        s=l[i]
print(s)