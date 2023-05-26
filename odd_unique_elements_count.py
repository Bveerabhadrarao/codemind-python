n=int(input())
k=list(map(int,input().split()))
lst=[]
c=0
for i in k:
    if i%2==1 and i not in lst:
        lst.append(i)
        c+=1
print(c)