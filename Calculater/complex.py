from math import *
x=0
y=0
def init(a,b):
    global x
    global y
    x=a
    y=b
def do_comp(a,b,c,d, sign: str):
    f1=complex(a,b)
    f2=complex(c,d)
    if sign =="+":
        linen= f"{f1} + {f2} = {f1+f2} "
    elif sign =="-":
        linen= f"{f1} - {f2} = {f1-f2} "
    elif  sign =="*":
        linen= f"{f1} * {f2} = {f1*f2} "
    elif sign =="+":
        linen= f"{f1} / {f2} = {f1/f2} "
    else:
        linen = "Нет такого знака в данном калькуляторе"
    return linen     
