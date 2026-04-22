import random

def kiem_tra_chan(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", lst)

    ket_qua = list(map(lambda x: True if x % 2 == 0 else False, lst))
    print("Kết quả (chẵn=True, lẻ=False):", ket_qua)

    return ket_qua

n = int(input("Nhập n: "))
kiem_tra_chan(n)
