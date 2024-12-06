names = ["michal", "nela", "ola", "przemek"]

# a
suma = sum(len(name) for name in names)
print(suma)


# b
copied_names = [name.title() for name in names]
print(copied_names)


# c
names_with_l = [name for name in names if 'l' in name]
print(names_with_l)

# d
women_names = tuple(name for name in copied_names if name[-1] == 'a' and name[0].isupper())
print(women_names)
