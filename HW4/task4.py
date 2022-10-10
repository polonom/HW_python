from random import randint
def writeinfile(lin):
    with open('file4.txt', 'w') as data:
        data.write(lin)

def Makemnog(k):
    koeff=[randint(0,100) for i in range(k+1)]
    poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1]) #[j==1]
# Поиск и замены:
    poly=poly.replace('x^1+', 'x+')
    poly=poly.replace('x^0', '')
    poly+=('','1')[poly[-1]=='+']
    poly=(poly, poly[:-2])[poly[-2:]=='^1']
    writeinfile(poly)
k=int(input("Напишите максимальную степень "))
Makemnog(k)

