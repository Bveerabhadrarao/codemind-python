n=input()
k=list(map(int,input().split()))
e=0
l=0
for i in k:
    if i%2==0:
        e+=1
    else:
        l+=1
print(e,l,end="")