from zoneinfo import reset_tzpath

n = int(input("Podaj liczbę: "))

count = 0

for i in range(1, n+1):
    liczba = float(input(f"podaj liczbę {i}: "))
    if liczba % 3 == 0:
        count += 1

print(count)