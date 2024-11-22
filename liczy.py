def zamien_litery_i_licz_zmiany(wyraz):
    zmieniony_wyraz = ""
    liczba_zmian = 0

    # Iteracja przez wyraz
    for i, znak in enumerate(wyraz):
        if znak == 'a':
            zmieniony_wyraz += 'A'
            liczba_zmian += 1
        elif znak == 'b':
            zmieniony_wyraz += 'B'
            liczba_zmian += 1
        else:
            zmieniony_wyraz += znak

    # Sprawdzamy, czy liczba znaków jest nieparzysta
    if len(wyraz) % 2 != 0:
        srodkowy_index = len(wyraz) // 2
        srodkowy_znak = zmieniony_wyraz[srodkowy_index]
        if not srodkowy_znak.isupper():
            zmieniony_wyraz = (
                zmieniony_wyraz[:srodkowy_index] +
                srodkowy_znak.upper() +
                zmieniony_wyraz[srodkowy_index + 1:]
            )
            liczba_zmian += 1

    return zmieniony_wyraz, liczba_zmian

# Przykładowe użycie
wyraz = "abacaba"
zmieniony_wyraz, liczba_zmian = zamien_litery_i_licz_zmiany(wyraz)
print(f"Zmieniony wyraz: {zmieniony_wyraz}")
print(f"Liczba zmian: {liczba_zmian}")
