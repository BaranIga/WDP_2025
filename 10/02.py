# a

krotka = (False, (3, 2, 1), {"klucz": "wartość"}, None, [1, 9, 2, 8], "kot", "pies")

print(krotka[3])
print(krotka[3:6])
print(krotka[-3])


# b

def zadanie_02_a(krotka, a):
    return krotka + (a, )


def zadanie_02_b(krotka, a):
    copied_tuple = ()
    for i in range(len(krotka)):
        copied_tuple += (krotka[i], )
    copied_tuple += (a, )
    return copied_tuple

print(zadanie_02_a((2, 3, 4, 5, 6, 7), 1))
print(zadanie_02_b((1, 2, 3, 4, 5, 6), 9))

def zadanie_02_c(krotka, a):
    copied_tuple = ()
    for i in range(len(krotka)):
        if i != a:
            copied_tuple += (krotka[i],)
    return copied_tuple

print(zadanie_02_c((1, 2, 3, 4, 5, 6), 4))


# c

def bezPowtórzen(lista):
    elem = list(set(lista))
    print(elem)

lista = [1, 2, 2, 3, 4, 4, 5, 1]
bezPowtórzen(lista)
