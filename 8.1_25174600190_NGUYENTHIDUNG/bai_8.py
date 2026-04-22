import math

# 1. Hình Tròn
def hinh_tron():
    r = float(input("Nhập bán kính hình tròn: "))
    if r <= 0:
        print("Lỗi: Bán kính phải lớn hơn 0.")
    else:
        chu_vi = 2 * math.pi * r
        dien_tich = math.pi * (r ** 2)
        print(f"Chu vi: {chu_vi:.2f}, Diện tích: {dien_tich:.2f}")

# 2. Hình Vuông
def hinh_vuong():
    a = float(input("Nhập độ dài cạnh: "))
    if a <= 0:
        print("Lỗi, nhập lại")
    else:
        print(f"Chu vi: {4 * a:.2f}, Diện tích: {a * a:.2f}")

# 3. Hình Chữ Nhật
def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Lỗi, nhập lại")
    else:
        print(f"Chu vi: {(a + b) * 2:.2f}, Diện tích: {a * b:.2f}")

# 4. Hình Tam Giác
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        print("Lỗi: Các cạnh phải lớn hơn 0.")
    elif a + b > c and a + c > b and b + c > a:
        chu_vi = a + b + c
        p = chu_vi / 2
        dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Chu vi: {chu_vi:.2f}, Diện tích: {dien_tich:.2f}")
    else:
        print("Lỗi, nhập lại")


def menu():
    print("\n--- CHƯƠNG TRÌNH TÍNH CHU VI & DIỆN TÍCH ---")
    print("1. Hình Tròn")
    print("2. Hình Vuông")
    print("3. Hình Chữ Nhật")
    print("4. Hình Tam Giác")
    
    chon = input("Chọn hình muốn tính (1-4): ")
    
    if chon == '1': hinh_tron()
    elif chon == '2': hinh_vuong()
    elif chon == '3': hinh_chu_nhat()
    elif chon == '4': hinh_tam_giac()
    else: print("Lựa chọn không hợp lệ!")
    
if __name__ == "__main__":
    menu()