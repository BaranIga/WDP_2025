def prostokat():
    m = int(input("podaj długość m: "))
    n = int(input("Podaj wysokość n: "))

    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * m)
        else:
            print("*" + " " * (m-2) + "*")

prostokat()