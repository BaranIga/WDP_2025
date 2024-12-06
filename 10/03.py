# Składnia list comprehension
# [wyrażenie for element in iterowalny_obiekt if warunek]

import math


# a

a = [x**5 for x in range(15)]
print(a)


# b
b = [math.factorial(x) for x in range(10)]
print(b)


# c
c = [math.exp(x) for x in range(9)]
print(c)


# d

d = ['Kowalski', 'Nowak', 'Wiśniewski', 'Wójcik', 'Kozłowski', 'Mazur', 'Jankowski', 'Woźniak', 'Dąbrowski', 'Lewandowski']

wynik = [d for d in d if len(d) > 6]
print(wynik)


# e
def potegi(ciag):
    return [x**3 for x in ciag if x%2 == 0]

ciag = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wynik = potegi(ciag)
print(wynik)
