def square_root(a, epsilon=0.00001):
    x = a
    while True:
        next_x = 0.5 * (x + a / x)
        if abs(next_x - x) < epsilon:
            return next_x
        x = next_x

# Przykład użycia
liczba = 25
print(f"Pierwiastek kwadratowy z {liczba} wynosi:", square_root(liczba))

def abs(x):
    if x >= 0:
        return x
    else:
        return -x





def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def square_root(a, epsilon=0.00001):
    x = a
    nastepny_x = 0.5 * (x + a / x)
    while abs(nastepny_x - x) < epsilon:
        nastepny_x = 0.5 * (x + a / x)
        x = nastepny_x
        return x

liczba = 25
print(f"Pierwiastek kwadratowy z", liczba, "wynosi:", square_root(liczba))
