n = int(input("Enter number of lines of pattern: "))

for i in range(1, n + 1):
    # print(" " * (n  - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")