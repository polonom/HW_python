from random import randint
import re
import itertools
def writeinfile(file,lin):
    with open(file, 'w') as data:
        data.write(lin)
def read_pol(file):
    with open(str(file), 'r') as data:
        mnogo = data.read()
    return mnogo
# def Makemnog(k):
#     koeff=[randint(0,100) for i in range(k+1)]
#     poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1]) 
#     poly=poly.replace('x^1+', 'x+')
#     poly=poly.replace('x^0', '')
#     poly+=('','1')[poly[-1]=='+']
#     poly=(poly, poly[:-2])[poly[-2:]=='^1']
#     return poly

def redo_poly(poly):
    poly = poly.replace('= 0', '')
    poly = re.sub("[*|^| ]", " ", poly).split('+')
    poly = [char.split(' ') for char in poly]
    poly = [[x for x in list if x] for list in poly]
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    return poly

def new_poly(poly1, poly2):   
    x = [0] * (max(poly1[0][1], poly2[0][1] + 1))
    for i in poly1 + poly2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

def Sumpoly(poly):
    var = ['*x^'] * len(poly)
    koeff = [x[0] for x in poly]
    degrees = [x[1] for x in poly]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(koeff, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))


k=int(input("Напишите максимальную степень "))
n=int(input("Напишите максимальную степень "))
# with open("file5_1.txt", 'w') as data:
#         data.write(Makemnog(k))
# with open("file5_2.txt", 'w') as data:
#         data.write(Makemnog(n))        
p1=read_pol("file5_1.txt")
p2=read_pol("file5_2.txt")
newp1=redo_poly(p1)
newp2=redo_poly(p2)
writeinfile("filesum.txt",Sumpoly(new_poly(newp1,newp2)))
