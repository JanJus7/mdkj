n = int(input("POdaj wysokość choinki n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print(" " * (n - 2) + "||")
