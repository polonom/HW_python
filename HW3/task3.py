import random
n = int(input())
listn = []
for i in range(n+1):
    listn.append(random.uniform(1, 20))
print(listn)
k = list(map(lambda x: x-int(x), listn))
print(max(k)-min(k))
