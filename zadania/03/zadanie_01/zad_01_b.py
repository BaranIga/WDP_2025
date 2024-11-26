suma_liczb_parzystych = 0
suma_liczb_nieparzystych = 0

for i in range(5):
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 == 0:
        suma_liczb_parzystych += 1
    else:
        suma_liczb_nieparzystych += 1

print(f"ilośc liczb parzystych {suma_liczb_parzystych} i nieparzystych {suma_liczb_nieparzystych}")