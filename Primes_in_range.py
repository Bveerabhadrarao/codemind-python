def p(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
m=int(input())
n=int(input())
cnt=0
#print(m)
#print(n)
l=[]
for i in range(m,n+1):
    if p(i):
        l.append(i)
        cnt+=1
print(cnt)
#print(l)