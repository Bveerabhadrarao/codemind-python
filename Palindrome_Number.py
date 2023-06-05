n=int(input())
for i in range(n):
    x=int(input())
    v=x
    c=0
    while x:
        r=x%10
        c=c*10+r
        x=x//10
    if v==c:
        print("True")
    else:
        print("False")