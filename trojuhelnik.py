def trojuhelnik(X):
    for i in range(1, X + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()
    
    for i in range(X - 1, 0, -1):
        for j in range(1, i + 1):
            print(i, end="")
        print()


X = int(input("Zadej liché číslo: "))

if X % 2 == 0:
    print("Zadej liché číslo.")
else:
    trojuhelnik(X)
