# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
n = int(input("Введите номер четверти : "))
if n != 1 or n != 2 or n != 3 or n != 4:
    sys.exit("please, stop")
if n == 1:
    print("возможный значения x>0,y>0")
if n == 2:
    print("возможный значения x<0,y>0")
if n == 3:
    print("возможный значения x<0,y<0")
if n == 4:
    print("возможный значения x>0,y<0")
