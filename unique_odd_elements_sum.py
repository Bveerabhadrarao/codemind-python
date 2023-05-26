n=int(input())
k=list(map(int,input().split()))
lst=[]
s=0
for i in k:
    if i not in lst:
        lst.append(i)
for j in lst:
    if j%2==1:
        s=s+j
print(s)