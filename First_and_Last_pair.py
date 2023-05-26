n=int(input())
k=list(map(int,input().split()))
a=len(k)//2
lst=[]
for i in range(a):
    lst.append(k[i])
    lst.append(k[-(i+1)])
if n%2==1:
    lst.append(k[a])
    lst.append(0)
print(*lst)