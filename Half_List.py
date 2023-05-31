n=int(input())
k=list(map(int,input().split()))
k1=[]
k2=[]
a=len(k)-1
for i in range(len(k)//2):
    k1.append(k[a])
    k2.append(k[i])
    a-=1
    i+=1
k3=k1+k2
print(*k3)