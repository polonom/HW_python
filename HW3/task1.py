import random 
n=int(input())
listn=[]
for i in range(n+1):
    listn.append(random.randint(1,20))
print(listn)
k=[]
j=0
while (2*j+1) < n+1:
    k.append(listn[2*j+1])
    j+=1
print("на нечётных позициях элементы", k)
res=0
for i in range(len(k)):
    res+=k[i]
print(res)
