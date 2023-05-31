n=int(input())
k=list(map(str,input().split()))
s=""
for i in k:
    s+=i
s=int(s)
s+=1
s=str(s)
print(*list(s))