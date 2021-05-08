import numpy as np
import math
import pandas as pd
import xlrd
import openpyxl

#ZAD1

print("Zadanie 1\n")

matrix = np.array([1,2,3])
matrix2 = matrix*2

print(matrix2)

#ZAD2

print("Zadanie 2\n")

matrix3x3 = np.array([[3,7,4], [9,3,5], [1, 4, 6]])

matrix4x4 = np.array([[3,7,4,3], [9,3,5,2], [1,4,6,7], [3,5,4,1]])


print(np.amax(matrix3x3, axis=0))
print(np.amin(matrix3x3, axis=0))


print(np.amax(matrix4x4, axis=0))
print(np.amin(matrix4x4, axis=0))


print(np.amax(matrix3x3, axis=1))
print(np.amin(matrix3x3, axis=1))


print(np.amax(matrix4x4, axis=1))
print(np.amin(matrix4x4, axis=1))

#ZAD 3

print("Zadanie 3\n")

matrix3x3 = np.array([[3,7,4], [9,3,5], [1, 4, 6]])

matrix4x4 = np.array([[3,7,4,3], [9,3,5,2], [1,4,6,7]])


print(matrix3x3.dot(matrix4x4))

#ZAD 4

print("Zadanie 4\n")

matrix1 = np.array([[7,7,4], [9,3,5], [1,4,6]])

matrix2 = np.array([[0.3, 0.3, 0.3], [0.3,0.3,0.3], [1/2,3/4,5/4]])

print(matrix1.dot(matrix2))

#ZAD 5

print("Zadanie 5\n")

a = []

matrix = np.array([[7,7], [9,3], [1,4]])

for i in range(0, 3):
    for j in range(0, 2):
        a.append(math.sin(matrix[i][j]))

print(a)

#ZAD 6

print("Zadanie 6\n")

a = []

matrix = np.array([[7,7], [9,3], [1,4]])

for i in range(0, 3):
    for j in range(0, 2):
        a.append(math.cos(matrix[i][j]))

print(a)

#ZAD 7

matrix = np.array([[7,7], [9,3], [1,4]])

for i in range(0, 3):
    for j in range(0, 2):
        a.append(math.sin(matrix[i][j]))

print(a)

b = []

matrix = np.array([[2,1], [3,3], [6,2]])

for i in range(0, 3):
    for j in range(0, 2):
        b.append(math.cos(matrix[i][j]))

print(b)

print(a+b)

#ZAD 8

matrix = np.array([[7,7, 3], [9,3,2], [1,4,3]])

for i in range(0, 3):
    for j in range(0, 1):
        print(matrix[i][j], matrix[i][j+1], matrix[i][j+2])

print(a)

#Zad9
 a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
 for b in a.flat:
     print(b)
     print("")

#Zad10
 macierz = np.arange(0,81,1).reshape(9,9)
 print(macierz)

 macierz_1 = macierz.reshape(3,27)
 print(macierz_1)
 macierz_2 = macierz.reshape(27,3)
 print(macierz_2)
 macierz_3 = macierz.reshape(81,1)
 print(macierz_3)
 macierz_4 = macierz.ravel()
 print(macierz_4)

#Zad11
 a = np.array([3, 7, 5, 6, 1, 9, 2, 7, 8, 6, 3, 6])
 print(a)
 macierz_1 = a.reshape(3, 4)
 print(macierz_1)
 print(macierz_1.ravel())
 macierz_2 = macierz_1.reshape(4,3)
 print(macierz_2)
 print(macierz_2.ravel())
 macierz_3 = macierz_1.reshape(2,6)
 print(macierz_3)
 print(macierz_3.ravel())



#Pandas

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

print(df[df['Liczba']>1000])

print(df[df['Imie'] == "ERYK"])

print(df.sum()[2])

print(df[((df.Rok >= 2000) & (df.Rok <= 2005))].sum()[2])

print("Dziewczynek:", df[((df.Plec == "K"))].sum()[2])
print("Chłopców:", df[((df.Plec == "M"))].sum()[2])

print(df.groupby(['Rok', 'Plec']).agg({'Liczba':['sum']}))

chlopcy = df[((df.Plec == "M"))]
chlopcyGroupBy = chlopcy.groupby(['Imie', 'Plec']).agg({'Liczba':['sum']})
print(chlopcyGroupBy.sort_values(by=chlopcyGroupBy.columns[0], ascending=False))



dziewczynki = df[((df.Plec == "K"))]
dziewczynkiGroupBy = dziewczynki.groupby(['Imie', 'Plec']).agg({'Liczba':['sum']})
print(dziewczynkiGroupBy.sort_values(by=dziewczynkiGroupBy.columns[0], ascending=False))
