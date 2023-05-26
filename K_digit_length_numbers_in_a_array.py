n,m=map(int,input().split())
k=list(map(int,input().split()))
c=0
for i in k:
    if i<0:
        i=i*(-1)
    i=str(i)
    i=list(i)
    if len(i)==m:
        c+=1
print(c)