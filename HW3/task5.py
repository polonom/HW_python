l = int(input())
mylist = [0, 1]
k = [1]
for i in range(1, l):
    n = mylist[i-1]+mylist[i]
    mylist.append(n)
    m = ((-1)**(i))*n
    k.insert(0, m)
print(*k[:l], *mylist[:l+1], sep=' ')
