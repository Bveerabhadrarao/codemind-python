n=int(input())
k=list(map(int,input().split()))
lst=[]
for i in k:
    if i not in lst:
        lst.append(i)
m=[]
for j in lst:
    m.append(j)
    a=k.count(j)
    m.append(a)
print(*m)