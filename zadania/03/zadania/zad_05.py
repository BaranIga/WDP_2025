a = int(input("podaj a: "))
n = int(input("podaj n: "))
r = int(input("podaj r: "))

an = a + (n - 1) * r

print(f"{n} - ty wyraz ciagu to: {an}")



def ciag(a1, n, r):
    an = a + (n - 1) * r
    return an

print(ciag(3, 6, 4))