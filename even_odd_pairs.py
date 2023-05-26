n=int(input())
k=list(map(int,input().split()))
k1=[]
k2=[]
k3=[]
for i in range(n):
    if k[i]%2==0:
        k1.append(k[i])
    else:
        k2.append(k[i])
if len(k1)<len(k2):
    for i in range(len(k1)):
        k3.append(k1[i])
        k3.append(k2[i])
    h=len(k1)
    for j in range(h,len(k2)):
        k3.append(k2[j])
else:
    for i in range(len(k2)):
        k3.append(k1[i])
        k3.append(k2[i])
    f=len(k2)
    for j in range(f,len(k1)):
        k3.append(k1[j])
if n%2!=0:
    k3.append(0)
print(*k3)