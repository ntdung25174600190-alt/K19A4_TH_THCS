# a
def P_a(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich

n = int(input("Nhập n: "))
print("P(n) =", P_a(n))

# b
def S_b(n):
    tong = 0
    for i in range(1, n + 1):
        tong += (-1)**(i+1) * i
    return tong

n = int(input("Nhập n: "))
print("S(n) =", S_b(n))

# c
def S_c(n):
    tong = 0
    for i in range(1, n + 1):
        tong += sum(range(1, i + 1))
    return tong

n = int(input("Nhập n: "))
print("S(n) =", S_c(n))

# d
def P_d(x, y, n):
    tong = 0
    for k in range(1, n + 1):
        tong += (x + 32*y + y**k)
    return x**y + tong

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n (>1): "))

print("P(x,y) =", P_d(x, y, n))