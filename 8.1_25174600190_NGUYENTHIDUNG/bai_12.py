def nhap_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (số năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    phu_cap_tham_nien = tham_nien * 500000
    tong_luong = luong_co_ban + phu_cap_tham_nien
    return tong_luong

def xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong):
    print("\n" + "="*30)
    print("THÔNG TIN NHÂN VIÊN")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên: {tham_nien} năm")
    print(f"Tổng lương: {luong:,} VNĐ")
    print("="*30)

ten, que, tn = nhap_nhan_vien()
tong_thu_nhap = tinh_luong(tn)
xuat_nhan_vien(ten, que, tn, tong_thu_nhap)