n=int(input())
k=list(map(int,input().split()))
lst=[]
for i in k:
    if i not in lst:
        lst.append(i)
print(sum(lst))