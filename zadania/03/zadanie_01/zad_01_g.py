n = int(input("Podaj liczbę: "))

sum = 0

for i in range(1, n+1):
    liczba = float(input(f"podaj liczbę {i}: "))
    sum += liczba

print(sum)