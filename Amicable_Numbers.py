n=int(input())
x=n
m=int(input())
y=m
s=0
c=0
for i in range(1,n):
    if n%i==0:
        c+=i
    if m%i==0:
        s+=i
if x==s and y==c:
    print("Amicable")
else:
    print("Not Amicable")