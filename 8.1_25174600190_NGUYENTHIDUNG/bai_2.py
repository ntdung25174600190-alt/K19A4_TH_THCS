def fibonacci():
    n = int(input("Nhập n: "))

    if n <= 0 or n > 20:
        print("Nhập lại")
        return

    a, b = 0, 1
    print("Dãy Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci()