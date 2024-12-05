# a

tab1 = [32, 9.21, "text", False, (3, 2, 1), {"klucz": "wartość"}, None, [1, 9, 2, 8], "kot", "pies"]
tab1[2] = "zmieniony element"
print("Element o indeksie 8: ", tab1[8])
print("Element o parzystsych indeksach w odwortnej kolejności: ", tab1[::-1][::-2])
print("Element czwarty od końca: ", tab1[-4])
print()


# b

tab2_01 = [8, 6, 4, 2, 0]
tab2_02 = [1, 3, 5, 7, 9]

def sorted(list):
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            return False
    return True

print(sorted(tab2_01))
print(sorted(tab2_02))
print()



# c

def suma_list(list1, list2):
    if (len(list1) != len(list2)):
        return False

    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

list3_01 = [1, 2, 3]
list3_02 = [9, 8, 7]

print("Suma wektorów: ", suma_list(list3_01, list3_02))
print()


# d

def func(list, n1, n2):
    for i in range(len(list)):
        if list[i] == n1:
            list[i] = n2

list4 = [2, 9, 2, 8, 2, 9]
n1 = 9
n2 = 100

print("Funckja przed zamianą: ", list4)

func(list4, n1, n2)

print("Funckja po zamianie: ", list4)
print()


# e

def funce(list, n1, n2):
    newList = []

    for i in range(len(list)):
        if i == n1:
            newList.append(n2)
        else:
            newList.append(i)

    return newList

list5 = [1, 2, 1, 2, 4, 3, 5, 7]
n1_e = 1
n2_e = 100

print("Funckja przed zamianą: ", list5)

func(list5, n1_e, n2_e)

print("Funckja po zamianie: ", list5)
print()


# f




# g

def month(month):
    months = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec",
        "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

    return months.index(month) + 1

def sort_months(month_list):







print(month("luty"))
