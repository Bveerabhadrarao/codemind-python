n=input().split()
s=""
for i in n:
    i=list(i)
    i.reverse()
    r=""
    for k in i:
        r+=k
    s=s+" "+r
print(s[1:])