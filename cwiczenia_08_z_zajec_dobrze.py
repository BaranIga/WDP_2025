import random

# zad_01

napis = ("Python to język programowania wysokiego poziomu ogólnego przeznaczenia[2], o rozbudowanym pakiecie bibliotek"
         " standardowych[3], którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje"
         " się przejrzystością i zwięzłością")

print("DŁUGOŚĆ NAPISU:", len(napis))
print("ZNAK 12:", napis[12]);
print("ZNAK 7:", napis[7]);
print("ZNAK -4:", napis[-4]);
print(napis[12] + napis[7] + napis[-4])
print(napis.lower())


# zad_02

full_name = "Baran Iga"
#A
surname, first_name = full_name.split()
print(f"Nazwisko: {surname}")
print(f"Imię: {first_name}")

#B
reversed = f"{first_name} {surname}"
print(reversed)

#C
def anagram(word):
    lista_znakow = list(word)
    random.shuffle(lista_znakow)
    return ''.join(lista_znakow)
print(anagram(first_name))
print(anagram(surname))

#D
inicjaly = f"{first_name[0]}{surname[0]}"
print(f"Inicjały: {inicjaly}")

#E
new_name = surname[0] + first_name[1:]
new_surname = first_name[0] + surname[1:]
new_full_name = new_name + " " + new_surname
print(new_full_name)


#zad_03
def znaki_parzyste(napis):
    return napis[::2]
print(znaki_parzyste("samochod"))

def ostatnie_nzaki(napis, n=1):
    return napis[-n:]
print(ostatnie_nzaki("samochod"))

def reverse_string(napis):
    return napis[::-1]
print(reverse_string("samochod"))

def palindrom(napis):
    napis = napis.replace(" ", "").lower()
    return napis[::-1]
print(palindrom("byly sobie kotki trzy"))

def ile_liter(napis, litera):
    return napis.lower().count(litera.lower())
print(ile_liter("karaluch", "a"))

def ile_slow(napis):
    return len(napis.split())
print(ile_slow("byly sobi koty trzy"))


def licz_s_i_s(napis):
    samogloski = "aeiouy"
    liczba_samoglosek = 0
    liczba_spolglosek = 0

    for znak in napis:
        if znak.isalpha():
            if znak in samogloski:
                liczba_samoglosek += 1
            else:
                liczba_spolglosek += 1

    return liczba_samoglosek, liczba_spolglosek

print("---------")
print(licz_s_i_s("byly sobi koty trzy"))


#zad_04
def wstaw_imie_data(imie, data_urodzenia):
    return "My name is {}. My date of birth is {}.".format(imie, data_urodzenia)

imie = "Marcin"
data_urodzenia = "16.05.1986"
print(wstaw_imie_data(imie, data_urodzenia))


#zad_05

def zamien_liter(wyraz):
    zmieniony_wyraz = ""
    liczba_zmian = 0

    for i, znak in enumerate(wyraz):
        if znak == 'a':
            zmieniony_wyraz += 'A'
            liczba_zmian += 1
        elif znak == 'b':
            zmieniony_wyraz += 'B'
            liczba_zmian += 1
        else:
            zmieniony_wyraz += znak

    if len(wyraz) % 2 != 0:
        srodkowy_index = len(wyraz) // 2
        srodkowy_znak = zmieniony_wyraz[srodkowy_index]
        if srodkowy_znak.isupper():
            zmieniony_wyraz = (
                zmieniony_wyraz[:srodkowy_index] +
                srodkowy_znak.lower() +
                zmieniony_wyraz[srodkowy_index + 1:]
            )
            liczba_zmian += 1
        else:
            zmieniony_wyraz = (
                    zmieniony_wyraz[:srodkowy_index] +
                    srodkowy_znak.upper() +
                    zmieniony_wyraz[srodkowy_index + 1:]
            )
            liczba_zmian += 1

    return zmieniony_wyraz, liczba_zmian

print(zamien_liter("abrakiadbra"))



#zad_06
def szyfrowanie_ascii(tekst, klucz):
    zaszyfrowany_tekst = ''.join([chr(ord(char) + klucz) for char in tekst])
    return zaszyfrowany_tekst

tekst = "Hello"
klucz = 3
print(szyfrowanie_ascii(tekst, klucz))


#zad_07
def suma_liczb(tekst):
    suma = 0
    liczba = 0
    for char in tekst:
        if char.isdigit():
            liczba = liczba * 10 + int(char)
        else:
            if liczba != 0:
                suma += liczba
                liczba = 0
    if liczba != 0:
        suma += liczba

    return suma


tekst = "W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków"
wynik = suma_liczb(tekst)

print(f"Suma liczb w tekście wynosi: {wynik}")
