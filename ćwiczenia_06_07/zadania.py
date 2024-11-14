// zad_01
def write_list(list):
    print(' '.join([str(item) for item in list]).center(30))

x = input("Podaj liczbe poziomow: ")
line = [1]
write_list(line)
for i in range(int(x) - 1):
    next_line = [1]
    for j in range(len(line) - 1):
        next_line.append(line[j] + line[j + 1])
    next_line.append(1)
    line = next_line
    write_list(line)


// zad_02

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

twinNumbers(150)


// zad_03
from tkinter.constants import PROJECTING


def catalan_numbers(limit=1_000_000):
    C = 1  # c_0
    n = 0
    parzyste = 0
    nieparzyste = 0

    while C < limit:
        print("C_", n, "=", C)

        if C % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1

        C = (4 * n + 2) * C // (n + 2)
        n += 1

    print("Liczby Catalana mniejsze od ", limit, ": ")
    print("Parzyste:", parzyste, ", Nieparzyste:", nieparzyste)


catalan_numbers()


// zad_04
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
    print("Liczba", number, "nie jest liczba doskonałą")


// zad_06

def szybkie_potegowanie(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / szybkie_potegowanie(x, -n)

    half = szybkie_potegowanie(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


x = float(input("Podaj podstawę potęgowania (x): "))
n = int(input("Podaj wykładnik potęgowania (n): "))

wynik = szybkie_potegowanie(x, n)
print("Wynik, ", x, "^", n, "wynosi: ", wynik)

