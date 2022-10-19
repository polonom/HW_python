import fractions

def do_frac(a,b,c,d, sign: str):
    f1=fractions.Fraction(a,b)
    f2=fractions.Fraction(c,d)
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