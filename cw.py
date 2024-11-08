# Zadanie 1
def gmean(*args):
    wynik = 1
    dlugosc = 0
    for arg in args:
        wynik *= arg
        dlugosc += 1
    wynik = wynik ** (1 / dlugosc)
    return wynik


def func(*args):
    for index, item in enumerate(args, start=1):
        print(" ".join([str(item)] * index))


def func2(*args):
    for i in range(1, len(args) + 1):
        print(" ".join([str(item) for item in args[:i]]))


# Zadanie 2


def my_max(a, b):
    return a if a > b else b


def my_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c



def my_max(*args):
    najwieksza = args[0]
    for arg in args:
        if arg > najwieksza:
            najwieksza = arg
    return najwieksza



# Zadanie 3

rekurencyjne = 0


def fibonaccirek(liczba):
    global rekurencyjne
    if liczba <= 1:
        return liczba
    else:
        rekurencyjne += 1
        return fibonaccirek(liczba-1) + fibonaccirek(liczba-2)


nierekurencyjne = 0


def fibonaccinrek(liczba):
    global nierekurencyjne
    if liczba <= 1:
        return liczba
    a = 0
    b = 1
    for _ in range(2, liczba + 1):
        nierekurencyjne += 1
        a, b = b, a + b
    return b



def algortytmeuklidesa(liczba1, liczba2):
    if liczba2 == 0:
        return liczba1
    else:
        return algortytmeuklidesa(liczba2, liczba1 % liczba2)





def skroculamek(a, b):
    dzielnik = algortytmeuklidesa(a, b)
    p = a / dzielnik
    q = b / dzielnik
    return p.__int__(), q.__int__()





def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    return 1


def main():
    print(gmean(2, 2, 5, 7))
    print('-----------')
    func(3, 'Ala', 5)
    print('-----------')
    func2(3, 'Ala', 5)
    print('-----------')
    print(my_max(1, 2))
    print('-----------')
    print(my_max(4, 5, 3))
    print('-----------')
    print(my_max(1, 2, 3, 4, 5, 62, 7, 8, 9, 10))
    print('-----------')
    print(fibonaccirek(2))  # dla 10: 88; dla 29: 832039; dla 100 program za długo liczy
    print(rekurencyjne)
    print('-----------')
    print(fibonaccinrek(12))  # dla 10: 9; dla 29: 28; dla 100: 99
    print(nierekurencyjne)
    print('-----------')
    print(algortytmeuklidesa(1989, 867))
    print(skroculamek(1989, 867))
    print('-----------')
    print(silnia(5))


main()
