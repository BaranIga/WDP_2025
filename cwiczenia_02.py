# a)
age = int(input("Wprowadz swoj wiek: "))
if (age >= 18 and age <= 100):
        print("Autoryzacja uzyskana")
else: print("Odmowa")


# b)

ab = int(input("Wprowadz liczbe:"))
if ab > 0:
    print("|a|=", ab)
else:
    print("|a|=", -ab)


# c)

ac = 50
bc = 10
if ac > bc:
    print("Hello World")


# d)

ad = int(input("Wprowadz liczbe: "))
if (ad%2 == 0):
    print("Twoja liczba jest parzysta!")
else:
    print("Twoja liczba jest nieparzysta!")


# e)

ae = float(input("Wprowadz liczbe zmiennoprzecinkowa: "))
be = float(input("Wprowadz liczbe zmiennoprzecinkowa: "))

if(ae>be):
    print(ae)
else:
    print(be)


# f)

a = float(input("Wprowadz liczbe zmiennoprzecinkowa: "))
if(a>=1 and a<=10):
    print("liczba jest z przedziału [1, 10]")
elif(a>=17 and a<=21):
    print("liczba jest z przedziału [17, 21]")
else:
    print("zaden z przedzialow")


# g)

a = int(input("Wprowadz liczbe: "))

if(a%3 == 0 and a%5 == 0):
    print("Podzielna przez 3 i 5")

if(a%3 == 0 and a%5 != 0):
    print("Podzielna przez 3, ale nie przez 5")

if(a%5 == 0 and a%3 != 0):
    print("Podzielna przez 5, ale nie przez 3")

if(a%3 !=0 and a % 5 != 0):
        print("Podzielna przez 3, ale nie przez 5")


# h)

ah = int(input("Wprowadz liczbe znowu: "))
bh = int(input("Wprowadz druga liczbe:"))
znak = input("Wprowadz znak. Do wyboru masz (+, -, *, :): ")

if(znak == "+"):
    print(ah+bh)

if(znak == "-"):
    print(ah-bh)

if(znak == "*"):
    print(ah*bh)

if(znak == ":"):
    print(ah/bh)


# i)

ai = float(input("dawaj liczbe: "))
znak_temp = input("wprowadz znak 'F' albo 'C': ")

if(znak_temp == "F"):
    c = ai*(9/5)+32
    print("W C z F wynosi: ", c)

if(znak_temp == "C"):
    f = (ai-32)*(5/9)
    print("W F z C wynosi: ", f)

# j)

a = int(input("liczba: "))
b = int(input("liczba: "))
c = int(input("liczba: "))

if(a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2):
    print("Liczby stanowią trojkę pitagorejska")
else:
    print("To nie jest trojka pitagorejska")
