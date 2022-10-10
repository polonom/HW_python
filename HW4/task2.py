def primfacs(n):
   i = 2
   primfac = [1]
   while i * i <= n: 
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac


n=int(input("Введите число, простые множетили которого вы хотите узнать "))
print(primfacs(n))