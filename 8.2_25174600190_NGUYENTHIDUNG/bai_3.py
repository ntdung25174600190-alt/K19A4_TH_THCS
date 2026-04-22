import random

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", lst)

    print("Các số nguyên tố:")
    for x in lst:
        if la_so_nguyen_to(x):
            print(x, end=" ")

n = int(input("Nhập n: "))
in_so_nguyen_to(n)