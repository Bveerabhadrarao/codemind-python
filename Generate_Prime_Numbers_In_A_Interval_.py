n=int(input())
m=int(input())
c=0 
for i in range(n,m+1):
    if i==1:
        continue
    fc=0
    for j in range(2,i):
        if i==1:
            break
        if i%j==0:
            fc=fc+1
            break
    if fc==0:
        print(i)