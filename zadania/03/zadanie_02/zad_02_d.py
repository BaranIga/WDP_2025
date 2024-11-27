import random

liczba = random.randint(1, 101)
liczba_podana = int(input("zgadnij liczbę: "))
count = 0

while liczba_podana != liczba:
    if liczba_podana > liczba:
        print("Szukana wartość jest mniejsza")
        liczba_podana = int(input("zgadnij liczbę: "))
        count += 1
    else:
        print("Szukana wartość jest większa")
        liczba_podana = int(input("zgadnij liczbę: "))
        count +=  1

print(f"BRAWO! Ilość prób: {count}")

