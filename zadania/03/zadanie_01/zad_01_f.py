liczba = int(input("Podaj liczbę: "))

if liczba > 0:
    for i in range(1, liczba+1):
        print(" ".join(str(x) for x in range(1, i+1)))