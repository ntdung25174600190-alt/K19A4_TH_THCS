def kiem_tra_nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if kiem_tra_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return 0
    
nam = int(input("Nhập năm y: "))
thang = int(input("Nhập tháng m: "))

if kiem_tra_nam_nhuan(nam):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")

ngay = so_ngay_trong_thang(thang, nam)
if ngay != 0:
    print(f"Tháng {thang} năm {nam} có tối đa {ngay} ngày.")
else:
    print("Tháng bạn nhập không hợp lệ!")