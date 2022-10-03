def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


n = int(input())
mylist = []
for i in range(1, n+1):
    mylist.append(fac(i))
print(mylist)
