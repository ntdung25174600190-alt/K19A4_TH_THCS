def so_ngay_trong_thang(thang, nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        nam_nhuan = True
    else:
        nam_nhuan = False

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan else 28
    else:
        return "Tháng không hợp lệ"

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print("Số ngày:", so_ngay_trong_thang(thang, nam))