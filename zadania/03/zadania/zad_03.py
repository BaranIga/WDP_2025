a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))
c = float(input("Podaj liczbę: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

