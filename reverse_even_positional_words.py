n=input().split()
s=""
for i in range(len(n)):
    if i%2==0:
        i=list(n[i])
        r=""
        for k in i:
            r=k+r
        s=s+" "+r
    else:
        s=s+" "+n[i]
print(s[1:])