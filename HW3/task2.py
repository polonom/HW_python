import random
n = int(input())
listn = []
for i in range(n+1):
    listn.append(random.randint(1, 20))
print(listn)
newlist = []
for j in range((len(listn)+1)//2):
    newlist.append(listn[j]*listn[-j-1])
print(newlist)
