import math

def phep_tinh_co_ban(a, b):
    print(f"\n--- Kết quả giữa {a} và {b} ---")
    print(f"Cộng: {a} + {b} = {a + b}")
    print(f"Trừ: {a} - {b} = {a - b}")
    print(f"Nhân: {a} * {b} = {a * b}")

    if b != 0:
        print(f"Chia: {a} / {b} = {a / b}")
    else:
        print("Chia: Không thể chia cho 0")

def tinh_luy_thua_1(a, b, n):
    mu = b + n
    ket_qua = a ** mu
    return ket_qua

def tinh_luy_thua_2(a, b, n):
    if a == 0:
        return "Lỗi" \
        ""
    
    mu = (n + 2) / a
    if b < 0 and mu % 1 != 0:
        return "Lỗi"
        
    ket_qua = b ** mu
    return ket_qua
def main():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        n = float(input("Nhập số n: "))

        phep_tinh_co_ban(a, b)
        print(f"\n Kết quả tính lũy thừa")
        
        res1 = tinh_luy_thua_1(a, b, n)
        print(f"Lũy thừa a^(b+n): {res1}")
        
        res2 = tinh_luy_thua_2(a, b, n)
        if isinstance(res2, str):
            print(f"Lũy thừa b^((n+2)/a): {res2}")
        else:
            print(f"Lũy thừa b^((n+2)/a): {res2:.4f}")

    except ValueError:
        print("Lỗi")

if __name__ == "__main__":
    main()