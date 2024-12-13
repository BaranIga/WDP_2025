slownik = {"Ala": 125634489, "Kasia": 123456789, "Damian": 987654321, "Maria": 546312978}

def print_phone_numbers(slownik):
    for imie, numer in slownik.items():
        print(f"{imie} ma numer {numer}")

print(slownik)
print_phone_numbers(slownik)


# b

slownik = {
    "poniedziałek": "Monday",
    "wtorek": "Tuesday",
    "środa": "Wednesday",
    "czwartek": "Thursday",
    "piątek": "Friday",
    "sobota": "Saturday",
    "niedziela": "Sunday"
}

def translate_to_english(days):
    return [slownik.get(day.lower(), f"Nieznany dzień: {day}") for day in days]

def translate_to_polish(days):
    reverse_translation = {i: j for j, i in slownik.items()}
    return [reverse_translation.get(day.lower().capitalize(), f"Unknown day: {day}") for day in days]

polskie_dni = ["wtorek", "czwartek", "poniedziałek", "sobota"]
angielskie_dni = ["Monday", "Tuesday", "Wednesday", "Sunday"]

print("Polskie dni:", polskie_dni)
print("Po angielsku:", translate_to_english(polskie_dni))

print("\nAngielskie dni:", angielskie_dni)
print("Po polsku:", translate_to_polish(angielskie_dni))


# miesiace

def sort_months(months):
    month_order = {
        "styczeń": 1, "luty": 2, "marzec": 3, "kwiecień": 4,
        "maj": 5, "czerwiec": 6, "lipiec": 7, "sierpień": 8,
        "wrzesień": 9, "październik": 10, "listopad": 11, "grudzień": 12
    }
    return sorted(months, key=lambda month: month_order.get(month.lower(), float('inf')))

miesiace = ["maj", "styczeń", "lipiec", "grudzień", "marzec", "październik"]
posortowane_miesiace = sort_months(miesiace)

print("Oryginalna lista miesięcy:", miesiace)
print("Posortowana lista miesięcy:", posortowane_miesiace)



# liczby

def rzymskie_na_arabskie(rzymskie):

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    arabskie = 0
    prev = 0

    for char in reversed(rzymskie):
        value = roman_values.get(char.upper(), 0)

        if value < prev:
            arabskie -= value
        else:
            arabskie += value

        prev = value

    return arabskie

print(rzymskie_na_arabskie("III"))
print(rzymskie_na_arabskie("VI"))
print(rzymskie_na_arabskie("X"))
print(rzymskie_na_arabskie("LVIII"))
print(rzymskie_na_arabskie("MCMXCIV"))



# odrotnie liczby

def arabskie_na_rzymskie(arabskie):
    slownik = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    posorotwane_wartosci = sorted(slownik.keys(), reverse=True)

    rzymskie = ""
    for value in posorotwane_wartosci:
        while arabskie >= value:
            rzymskie += slownik[value]
            arabskie -= value

    return rzymskie

print(arabskie_na_rzymskie(3))
print(arabskie_na_rzymskie(4))
print(arabskie_na_rzymskie(9))
print(arabskie_na_rzymskie(58))
print(arabskie_na_rzymskie(1994))
