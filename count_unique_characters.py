n=input()
n=n.lower()
n=list(n)
c=0
for i in range(len(n)):
    if n[i]==" ":
        continue
    x=n.count(n[i])
    if x==1:
        c+=1
print(c)