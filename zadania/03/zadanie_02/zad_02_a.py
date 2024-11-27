znak = ""
count = 0

while znak != "x":
    znak = str(input("wprowadź znak: "))
    print(znak)
    count += 1

print(f"pobrano {count} znaków")
