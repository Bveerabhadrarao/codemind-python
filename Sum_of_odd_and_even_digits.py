n=int(input())
l=list(map(int,input().split()))
odd=0
even=0
for i in range(len(l)):
    if i%2==0:
        odd+=l[i]
    else:
        even+=l[i]
if (odd-even)==0:
    print("YES")
else:
    print("NO")