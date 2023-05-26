n=input().split()
k=list(map(int,input().split()))
lst=[]
for i in k:
    i=str(i)
    i=i[::-1]
    lst.append(int(i))
print(*lst)