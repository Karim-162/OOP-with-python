n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")  # Spacing before numbers
    for k in range(1, i + 1):
        print(k, end=" ")  # Printing numbers
    print()
