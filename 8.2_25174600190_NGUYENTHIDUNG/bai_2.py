import random
def tao_danh_sach_binh_phuong(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách ban đầu:", lst)

    binh_phuong = list(map(lambda x: x**2, lst))
    print("Bình phương:", binh_phuong)

    return binh_phuong

n = int(input("Nhập n: "))
tao_danh_sach_binh_phuong(n)