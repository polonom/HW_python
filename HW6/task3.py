import random 
n=int(input())
listn=[]
for i in range(n+1):
    listn.append(random.randint(1,20))
print(listn)
newlist=[x for l,x in enumerate(listn) if l%2 ]
print(sum(newlist))
