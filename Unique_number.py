n=int(input())
n=str(n)
n=list(n)
for i in range(len(n)):
    if n.count(n[i])>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")