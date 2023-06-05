n=int(input())
s=n
c=0
while n:
    x=n%10
    c=c*10+x
    n=n//10
if c==s:
    print("True")
else:
    print("False")