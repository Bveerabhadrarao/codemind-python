n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    if i%2==1:
        s+=i
    else:
        break
print(s)