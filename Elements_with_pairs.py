n=int(input())
k=list(map(int,input().split()))
if n%2==1:
    k.append(0)
print(*k)