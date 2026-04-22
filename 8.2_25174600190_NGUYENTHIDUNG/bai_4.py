def dao_nguoc_danh_sach(lst):
    return lst[::-1]

lst = list(map(int, input("Nhập danh sách: ").split()))
print("Danh sách đảo ngược:", dao_nguoc_danh_sach(lst))