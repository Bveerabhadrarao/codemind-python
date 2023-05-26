n=int(input())
k=list(map(int,input().split()))
cnt=0
for i in range(1,n-2):
    if k[i-1]<k[i] and k[i]>k[i+1]:
        continue
    elif k[i-1]>k[i] and k[i]<k[i+1]:
        continue
    else:
        cnt=1
        break
if cnt==1:
    print("no")
else:
    print("yes")