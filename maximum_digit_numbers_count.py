def digit(n):
    #n=abs(n)
    k=str(n)
    return len(k)
n=int(input())
lst=list(map(int,input().split()))
l=[]
l1=[]
for i in range(n):
    m=digit(lst[i])
    l.append(m)
b=max(l)
#print(l)
for i in range(n):
    if digit(lst[i])==b:
        l1.append(lst[i])
print(*l1)