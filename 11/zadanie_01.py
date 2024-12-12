# a

countries = {"Polska", "Włochy", "Wielka Brytania", "Austria", "Hiszpania"}
print(countries)

countries.add("Francja")
print(countries)

print("Polska" in countries)

countries.remove("Austria")
print(countries)


# b

cities1 = {"Warszawa", "Kraków", "Gdańsk", "Wrocław", "Poznań"}
cities2 = {"Łódź", "Lublin", "Gdańsk", "Katowice", "Bydgoszcz"}

print("Zbiór 1: ", cities1)
print("Zbiór 2: ", cities2)

suma_zbiorow = cities1.union(cities2)  # suma_zbiorow = cities1 | cities2
print("Suma zbiorów: ", suma_zbiorow)

czesc_wspolna = cities1.intersection(cities2)  # czesc_wspolna = cities1 & cities2
print("Część wspólna: ", czesc_wspolna)

roznica = cities1.difference(cities2)  # roznica = cities1 - cities2
print("Różnica: ", roznica)

podzbior = cities1.issubset(cities2)  # podzbior = cities1 <+ cities2
print("Czy cities1 jest podzbiorem cities2: ", podzbior)
