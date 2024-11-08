# Zadanie 1
def gmean(*args):
    result = 1
    dl = 0
    for arg in args:
        result *= arg
        dl += 1
    result = result ** (1 / dl)
    return result


def func(*args):
    for i in range(1, len(args) + 1):
        print(" ".join([str(item) for item in args[:i]]))


def func2(*args):
    for index, item in enumerate(args, start=1):
        print(" ".join([str(item)] * index))





# Zadanie 2


def my_max(a, b):
    if (a>b):
        return a
    return b


def my_max(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    else:
        return c



def my_max(*args):
    najwieksza = args[0]
    for i in args:
        if i > najwieksza:
            najwieksza = i
    return najwieksza



# Zadanie 3

liczba = 0;

def rekurencyjna(n):
    global liczba
    if n <= 1:
        return n
    else:
        liczba += 1
        return rekurencyjna(liczba-1) + rekurencyjna(liczba-2)


def nierekurencyjna(n):
    global liczbab
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        liczbab += 1
        a, b = b, a + b
    return b
 




# Zadanie 4

def nwd (a, b):
    while b:
        a, b = b, a%b
        return abs(a)




def ulamek(a, b):
    dzielnik = nwd(a, b)
    p = a // dzielnik
    q = b / dzielnik
    return p, int(q)




# Zadanie 5

def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    return 1


def main():
    print('zadanie 1')
    print(gmean(2, 2, 5, 7))
    func(3, 'Ala', 5)
    func2(3, 'Ala', 5)
    print('zadanie 2')
    print(my_max(1, 2))
    print(my_max(4, 5, 3))
    print(my_max(1, 2, 3, 4, 5, 62, 7, 8, 9, 10))
    print('zadanie 3')
    print(rekurencyjna(2))
    print(nierekurencyjna(12))
    print('zadanie 4')
    print(algortytmeuklidesa(1989, 867))
    print(ulamek(1989, 867))
    print('zadanie 5')
    print(silnia(5))
