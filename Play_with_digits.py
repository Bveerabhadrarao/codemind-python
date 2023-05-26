n=int(input())
k=list(map(int,input().split()))
c=0
for i in k:
    s=0
    while i>0:
        r=i%10
        s+=r
        i=i//10
    c+=s
print(c)