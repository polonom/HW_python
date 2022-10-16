n=int(input())
listn=[x for x in range(1,n+1)]
newlist=list(map(lambda i: (1+(1/i))**i,listn))
print('%.2f' % sum(newlist))
