m = int(input("Podaj liczbę: "))
liczba = 0
wynik = 3 ** liczba


while wynik <= m:
    print(f"3^{liczba} = {wynik}")
    liczba += 1
    wynik = 3 ** liczba
