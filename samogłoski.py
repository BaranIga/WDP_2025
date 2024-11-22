def licz_samogloski_i_spolgłoski(napis):
    # Definicja samogłosek
    samogloski = "aeiouyąęóAEIOUYĄĘÓ"
    liczba_samoglosek = 0
    liczba_spolglosek = 0

    # Iteracja przez znaki w napisie
    for znak in napis:
        if znak.isalpha():  # Sprawdzamy, czy znak jest literą
            if znak in samogloski:
                liczba_samoglosek += 1
            else:
                liczba_spolglosek += 1

    return liczba_samoglosek, liczba_spolglosek

# Przykładowe użycie
napis = "Koty lubią żółte myszy."
samogloski, spolgłoski = licz_samogloski_i_spolgłoski(napis)
print(f"Liczba samogłosek: {samogloski}")
print(f"Liczba spółgłosek: {spolgłoski}")
