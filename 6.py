print("Żeby znaleźć NWD -> ")
a = int(input("Podaj większą liczbę: "))
b = int(input("Podaj mniejszą liczbe: "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
