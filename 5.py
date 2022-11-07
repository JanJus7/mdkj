n = int(input("podaj wielkość jedengo trójkąta: "))
for i in range(1, n + 1):
    print("*" * i + " " * (n - i))
print(" ")
for i in range(1, n + 1):
    print("*" * (n - i + 1) + " " * i)
