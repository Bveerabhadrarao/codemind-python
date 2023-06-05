n=int(input())
s=0
x=n
x=str(x)
x=list(x)
x.reverse()
a=len(x)
for i in x:
    s=s+(int(i)**a)
    a-=1
if s==n:
    print("True")
else:
    print("False")