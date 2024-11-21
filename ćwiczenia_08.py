import random
import string
# zad_01

napis = ("Python to język programowania wysokiego poziomu ogólnego przeznaczenia[2], o rozbudowanym pakiecie bibliotek"
         " standardowych[3], którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje"
         " się przejrzystością i zwięzłością")

print("DŁUGOŚĆ NAPISU:", len(napis))
print("ZNAK 12:", napis[12]);
print("ZNAK 7:", napis[7]);
print("ZNAK -4:", napis[-4]);
print(napis[12] + napis[7] + napis[-4])
print(napis.upper())


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
    return 1

def ile_liter(napis, litera):
    return napis.lower().count(litera.lower())
print(ile_liter("karaluch", "a"))

def ile_slow(napis):
    return len(napis.split())
print(ile_slow("byly sobi koty trzy"))


def licz_samogloski_spolgloski(s):
    samogloski = "aeiouyąęó"
    spolgloski = "bcdfghjklmnpqrstvwxzćłńśżź"
    spolgloski = ''.join(set(spolgloski) - set(samogloski))

    s_czyste = ''.join(char.lower() for char in s if char.isalpha())
    liczba_samoglosek = sum(1 for char in s_czyste if char in samogloski)
    liczba_spolglosek = sum(1 for char in s_czyste if char in spolgloski)
    return liczba_samoglosek, liczba_spolglosek
print(licz_samogloski_spolgloski("byly sobi koty trzy"))

def liczenie(napis):
    return sum(1 for char in napis if char.isalpha())
print(liczenie("byly sobie"))


#zad_04
def wstaw_imie_data(imie, data_urodzenia):
    return "My name is {}. My date of birth is {}.".format(imie, data_urodzenia)

imie = "Marcin"
data_urodzenia = "16.05.1986"
print(wstaw_imie_data(imie, data_urodzenia))


#zad_05
def zamien_litery(napis):
    liczba_zmian = 0

    napis = list(napis)
    for i in range(len(napis)):
        if napis[i] == 'a':
            napis[i] = 'A'
            liczba_zmian += 1
        elif napis[i] == 'b':
            napis[i] = 'B'
            liczba_zmian += 1

    if len(napis) % 2 != 0:
        srodkowy_index = len(napis) // 2
        if napis[srodkowy_index].lower() in ['a', 'b']:  # Zamieniamy tylko, jeśli to 'a' lub 'b'
            if napis[srodkowy_index] == 'a':
                napis[srodkowy_index] = 'A'
            elif napis[srodkowy_index] == 'b':
                napis[srodkowy_index] = 'B'
            liczba_zmian += 1

    return ''.join(napis), liczba_zmian

wyraz = "abrakadabra"
nowy_wyraz, zmiany = zamien_litery(wyraz)

print(f"Nowy wyraz: {nowy_wyraz}")
print(f"Liczba dokonanych zmian: {zmiany}")


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

