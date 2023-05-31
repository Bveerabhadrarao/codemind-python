n=int(input())
k=list(map(int,input().split()))
k1=[]
for i in k:
    if i not in k1:
        k1.append(i)
print(*k1)