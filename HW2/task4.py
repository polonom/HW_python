n=int(input())
mylist=[]
for i in range(-n,n+1):
    mylist.append(i)
res=1
l=[]
l=open('/Users/polinakivokurtseva/Desktop/Python/HW2/file.txt').read().splitlines()
for i in range(len(l)):
       print(l)
       j=int(l[i])
       res = res * mylist[j] 
print(mylist)
print(res)