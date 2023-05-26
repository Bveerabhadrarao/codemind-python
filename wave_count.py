n=int(input())
k=list(map(int,input().split()))
cnt=0
for i in range(1,n-1,2):
    if k[i-1]<k[i] and k[i]>k[i-1]:
        cnt+=1
    else:
        print("-1")
        cnt=0
        break
if cnt!=0:
    print(cnt)