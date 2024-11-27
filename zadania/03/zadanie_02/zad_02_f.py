attempt = 3

for i in range(1, attempt + 1):
    month = int(input("Podaj miesiąc <1, 12>: "))
    if 1 <= month <= 12:
        print(f"Miesiąc {month}")
    else:
        print("niepoprawny numer miesiąca")

ilosc_prob = 0

while(ilosc_prob <= 3):
    miesiac = int(input("podaj numer miesiaca: "))
    if(miesiac>=1 and miesiac<=12):
        print("Dorby miesiąć")
        ilosc_prob+=1
        break
    else:
        print("nie ma takiego miesiąca")