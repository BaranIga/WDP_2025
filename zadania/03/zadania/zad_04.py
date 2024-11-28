number = int(input("Podaj liczbę: "))

reversed_number = 0

while number > 0:
    lastNumber = number % 10
    print(lastNumber)
    reversed_number = reversed_number * 10 + lastNumber
    number //= 10
print(reversed_number)