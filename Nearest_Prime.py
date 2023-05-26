def p(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return 0
    else:
        return 1
t=int(input())
while t:
    n=int(input())
    k=[]
    for i in range(n,1,-1):
        if(p(i)):
            j=i
            break
    for i in range(n,n+100):
        if(p(i)):
            k=i
            break
    if (k-n)<(n-j):
        print(k)
    else:
        print(j)
    t-=1
    