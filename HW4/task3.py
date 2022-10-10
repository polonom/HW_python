linen=str(input())
newlinen = linen.split(" ")
res=[]
for i in newlinen:
    if i not in res:
        res.append(i)
print(*res, sep=" ")