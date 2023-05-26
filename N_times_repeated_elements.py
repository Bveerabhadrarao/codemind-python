n=int(input())
k=list(map(int,input().split()))
m=int(input())
lst=[]
c=0
for i in k:
    if k.count(i)==m and i not in lst:
        lst.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*lst)