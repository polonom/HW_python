# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
print("Введите день недели")
n = int(input())
if n > 7:
    sys.exit("У вас в недели не более 7 дней")
if n == 6 or n == 7:
    print("Да, день выходной ")
else:
    print("Нет, день не выходной ")