from zoneinfo import reset_tzpath

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))

sum = 0

if a > b:
    sum = 0
else:
    for i in range(a, b+1):
        if i%2 != 0:
            sum += i

print(sum)
