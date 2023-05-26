n=int(input())
k=list(map(int,input().split()))
cnt=0
for i in range(1,len(k)-1):
    if k[i-1]+k[i]==k[i+1]:
        cnt+=1
    else:
        cnt=0
        break
if cnt==0:
    print("no")
else:
    print("yes")