for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for i in range(len(l)):
        k=l[i]
        for j in range(i+1,len(l)):
            d=k+l[j]
            if d in l:
                cnt+=1
    if cnt==0:
        print(-1)
    else:
        print(cnt)