def seq(n):
    return (1+(1/n))**n


n = int(input())
mylist = []
for i in range(1, n+1):
    mylist.append(seq(i))
# print(mylist)
counter = 0
for j in range(0, len(mylist)):
    counter += mylist[j]
print('%.2f' % counter)
