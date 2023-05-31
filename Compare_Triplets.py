n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
d=0
for i in range(len(n)):
    if n[i]>m[i]:
        c+=1
    elif n[i]<m[i]:
        d+=1
print(c,d)