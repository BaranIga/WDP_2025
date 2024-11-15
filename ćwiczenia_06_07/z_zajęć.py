# zad_01

def silnia(x):
    wynik = 1
    for i in range(1, x+1):
        wynik *= i
    return wynik

def permutacja(n, k):
    if k>n or n<0 or k<0:
        return False
    return silnia(n) // (silnia(k) * silnia(n-k))

def trojkat(n):
    width = n * 5
    for i in range(n):
        print((n-i)*" ", end=" ")
        for k in range(i+1):
            print((permutacja(i, k)), end=" ")
        print()


trojkat(10)

print("__________________________________________________")

# zad_02

def isTwin(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True


def twinNumbers(n = 1000):
    for p in range(3, n, 2):
        if isTwin(p) and isTwin(p+2):
            print("Liczby bliźniacze to: ", p, " i ", p+2)

twinNumbers(50)


print("__________________________________________________")



# zad_03

def catalan_numbers(limit=1_000_000):
    C = 1  # c_0
    n = 0
    parzyste = 0
    nieparzyste = 0

    while C < limit:
        print(C)
        if C % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1

        C = (4 * n + 2) * C // (n + 2)
        n += 1

    print("Liczby Catalana mniejsze od ", limit, ": ")
    print("Parzyste:", parzyste)
    print("Nieparzyste: ", nieparzyste)


catalan_numbers()


print("__________________________________________________")


# zad_04
def is_perfect(number):
    if number < 2:
        return False

    suma_dzielnikow = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            suma_dzielnikow += i

    return suma_dzielnikow == number


number = int(input("Podaj liczbę do sprawdzenia: "))
if is_perfect(number):
    print("Liczba ", number, "jest liczba dokonałą")
else:
    print("Liczba", number, "NIE jest liczba doskonałą")


print("__________________________________________________")


# zad_05

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def square_root(a, epsilon=0.00001):
    x = 1
    nastepny_x = 0.5 * (x + a / x)
    while abs(nastepny_x - x) > epsilon:
        x = nastepny_x
        nastepny_x = 0.5 * (x + a / x)
    return x

liczba = 2
print(f"Pierwiastek kwadratowy z", liczba, "wynosi:", square_root(liczba))


print("__________________________________________________")



# zad_06

def szybkie_potegowanie(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / szybkie_potegowanie(x, -n)

    h = szybkie_potegowanie(x, n // 2)
    if n % 2 == 0:
        return h * h
    else:
        return h * h * x


x = float(input("Podaj podstawę potęgowania (x): "))
n = int(input("Podaj wykładnik potęgowania (n): "))

wynik = szybkie_potegowanie(x, n)
print("Wynik, ", x, "^", n, "wynosi: ", wynik)



print("__________________________________________________")
