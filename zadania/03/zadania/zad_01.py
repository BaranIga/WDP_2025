napis = str(input("Podaj jakiś napis: "))

napis = napis.replace(" ", "")
napis = napis.replace("W", "")

print(napis[::2])
