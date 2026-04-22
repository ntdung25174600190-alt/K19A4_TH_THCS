# a
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", ucln(a, b))

# b
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN =", bcnn(a, b))

# c
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(tu, mau):
    u = ucln(tu, mau)
    return tu // u, mau // u

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

if mau == 0:
    print("Mẫu không hợp lệ!")
else:
    tu_rg, mau_rg = rut_gon(tu, mau)
    print("Phân số rút gọn:", tu_rg, "/", mau_rg)

# d
n = int(input("Nhập số lượng phần tử: "))

ds = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    ds.append(x)

print("Số nhỏ nhất:", min(ds))
print("Số lớn nhất:", max(ds))