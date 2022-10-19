from complex import do_comp
from log import log_in
from frac import do_frac
# import complex
# import frac

print('Выберете с какими числами вы собираетесь работать : \n 1 - комплексные\n 2 - рациональные  ')
while True:
    option=int(input())
    if option<1 or option > 2:
        print("Попробуйте еще раз, такого варианта нет")
    else:
        break 
if option == 1:
    n1=int(input("Введите действительную часть первого числа : "))
    i1=int(input("Введите мнимую часть первого числа : "))
    n2=int(input("Введите действительную часть второго числа : "))
    i2=int(input("Введите мнимую часть второго числа : "))
    action=input("Введите знак операции ")
    equation = do_comp(n1,i1,n2,i2,action)
elif option == 2:
    n1=int(input("Введите числитель первого числа : "))
    i1=int(input("Введите знаменатель первого числа : "))
    n2=int(input("Введите числитель второго числа : "))
    i2=int(input("Введите знаменатель числа : "))
    action=input("Введите знак операции ")
    equation = do_frac(n1,i1,n2,i2,action)

log_in(equation)
print(equation)