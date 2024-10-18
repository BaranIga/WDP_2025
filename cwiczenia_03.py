# ZADANIE_01

for i in range(2, 101):
    print(i)

#a
suma = 0

for i in range(2, 101):
    if (i % 2 == 0):
        suma += i

print(suma)

#b
liczby_parzyste = 0
liczby_nieparzyste = 0

for i in range(5):
    i = int(input("Wprowadz liczbe calkowita: "))
    if(i%2 == 0):
        liczby_parzyste += 1
    else:
        liczby_nieparzyste += 1

print("Liczb nieparzystych było: ", liczby_nieparzyste, "a parzystych ", liczby_parzyste)

#c

suma_c  = 0

for i in range(1, 101):
    suma_c += i**2

print(suma_c)


#d

suma_d  = 0

for i in range(1, 101):
    suma_d += 2**i

print(suma_d)


#e

suma_e = 0
a = int(input("Podaj liczbę calkowita a: "))
b = int(input("Podaj liczbę calkowita b: "))

if(a>b):
    suma == 0
else:
    for i in range(a, b):
        if(i%2):
            suma_e +=i

print(suma_e)


#f

f = int(input("Podaj liczbę calkowita f: "))
if(f > 0):
    for i in range(f+1):
        for j in range(i + 1):
            print(j, end="")
        print("\n")

#g

suma_g = 0
n = int(input("Podaj liczbę n: "))

for i in range(n):
    a = int(input())
    suma_g += a

print(suma_g)

#h

liczby_podzilne_h = 0

for i in range(n):
    if(i%3 == 0 and i%5):
        liczby_podzilne_h += 1

print(liczby_podzilne_h)


# ZADANIE_02




#a

znak = ''

while (znak != 'x'):
    znak = str(input("Podaj znak: "))
    print(znak)


#b



while True:
    liczba = int(input("Liczba: "))
    if(1 <= liczba <= 10):
        print("nie")
        break
    else:
        print(liczba*2)


#c
liczba1 = -1
liczba2 = -1
liczba3 = -1
while (liczba1<0 or liczba2<0 or liczba3<0 ):
    liczba1 = int(input("Podaj liczbe calkowita: "))
    liczba2 = int(input("Podaj liczbe calkowita: "))
    liczba3 = int(input("Podaj liczbe calkowita: "))


if(liczba1 == 0 or liczba2 == 0 or liczba3 == 0):
    print("odpowiedni komunikat")


#d

import random
d2 = random.randint(1,101)
ilosc_prob = 0

while True:
    liczbad = int(input("Podaj liczbe: "))
    ilosc_prob+=1

    if(liczbad == d2):
        print("Udalo sie po próbach: ", ilosc_prob)
        break
    elif(liczbad > d2):
        print("Szukana wartość jest mniejsza")
    else:
        print("Szukana wartość jest większa")


#e

m = int(input("Podaj liczbe calkowita: "))

if(m>2):
    potega =1
    n = 0
    while(potega<=m):
        n+=1
        potega = 3 ** n
        print(potega)

#f


ilosc_prob = 0

while(ilosc_prob <= 3):
    miesiac = int(input("podaj numer miesiaca: "))
    if(miesiac>=1 and miesiac<=12):
        print("Dorby miesiąć")
        ilosc_prob+=1
        break
    else:
        print("nie ma takiego miesiąca")
