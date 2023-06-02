n=input()
s='0123456789'
c=0
for i in n:
    if i in s:
        c+=int(i)
print(c)
        