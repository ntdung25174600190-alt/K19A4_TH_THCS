def luy_thua(a, n):
    if n == 0:
        return 1
    return a * luy_thua(a, n - 1)

def tinh_luy_thua():
    a = int(input("Nhập số tự nhiên a: "))
    n = int(input("Nhập số mũ n: "))

    ket_qua = luy_thua(a, n)
    print("Kết quả:", ket_qua)

tinh_luy_thua()