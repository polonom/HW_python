l=int(input())
mylist=[0,1]
for i in range(1,l):
    n=mylist[i-1]+mylist[i]
    mylist.append(n)
print(*mylist[ :l ], sep=' ')