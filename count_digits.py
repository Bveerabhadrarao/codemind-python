a=int(input())
k=list(map(int,input().split()))
t=[]
for i in k:
    if i<0:
        i=i*(-1)
    s=str(i)
    t.append(len(s))
print(*t)