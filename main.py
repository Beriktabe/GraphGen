import random


def prettify(matr): #f - взвешенный
    strg = ""
    for i in range(0, n):
        for j in range(0, n):
            strg += str(matr[i][j])
            if j < n-1:
                strg += ", "
        strg += "\n"
    return strg
def toList(matr, f):
    strg = ""
    for i in range(0, n):
        for j in range(0, n):
            if matr[i][j] > 0:
                strg += str(i) + ", " + str(j)
                if f:
                    strg += ", " + str(matr[i][j])
                strg += "\n"

    return strg

def matrix(n, a):
    sp = []
    for i in range(n):
        sp.append([a]*n)
    return sp

def orientedFull():
    mat = matrix(n, 1)
    for i in range(0, n):
        mat[i][i] = 0
    return mat

def weightedNotFull(l, r): #l - кол-во ребер, r - макс значение веса
    mat = matrix(n, 0)
    for i in range(0, n-1):
        if l == 0:
            break
        rndNum = random.randrange(1, r, 1)
        mat[i][i+1] = rndNum
        mat[i + 1][i] = rndNum
        l -= 1

    while l > 0:
        rndN = random.randrange(0, n, 1)
        rndM = random.randrange(0, n, 1)
        if (rndN != rndM) and (mat[rndN][rndM] == 0):
            mat[rndN][rndM] = random.randrange(1, r, 1)
            l -= 1
    return mat

def notWeightedNotOriented(l):
    return weightedNotFull(l, 2)

def connectedWeighted(l, r): #l - доп кол-во ребер
    return weightedNotFull(n-1+l, r)

def cycleNotFullNotOriented(l, g): #g - кол-во циклов
    mat = notWeightedNotOriented(l)
    while g > 0:
        rndN = random.randrange(0, n, 1)
        if mat[rndN][rndN] == 0:
            mat[rndN][rndN] = 1
        g -= 1

    return mat

n = 0
mf = False
print("1) Ориентированный полный.")
print("2) Взвешенный(ребра) неполный.")
print("3) Неориентированный невзвешенный.")
print("4) Связный взвешенный.")
print("5) С циклом неполный неориентированный.")
ch = input('Какой граф создать?:')

n = int(input('Кол-во вершин: '))
mat = matrix(n, 0)
if ch == "1":
    mat = orientedFull()
elif ch == "2":
    a = int(input('кол-во ребер: '))
    b = int(input('макс значение веса: '))
    mf = True
    mat = weightedNotFull(a, b)
elif ch == "3":
    a = int(input('кол-во ребер: '))
    mat = notWeightedNotOriented(a)
elif ch == "4":
    a = int(input('кол-во доп ребер: '))
    b = int(input('макс значение веса: '))
    mf = True
    mat = connectedWeighted(a, b)
elif ch == "5":
    a = int(input('кол-во ребер: '))
    b = int(input('кол-во циклов: '))
    mat = cycleNotFullNotOriented(a, b)

print(prettify(mat))
f = open('graphM.txt', 'w')
f.write(prettify(mat))
print(toList(mat, mf))
f = open('graphL.txt', 'w')
f.write(toList(mat, mf))