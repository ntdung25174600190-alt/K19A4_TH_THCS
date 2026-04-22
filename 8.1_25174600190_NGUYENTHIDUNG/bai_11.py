def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_ket_qua(ho_ten, toan, ly, hoa, dtb):
    print("----------------------------")
    print("KẾT QUẢ HỌC TẬP")
    print("Họ tên:", ho_ten)
    print("Toán:", toan, "| Lý:", ly, "| Hóa:", hoa)
    print("Điểm trung bình:", round(dtb, 2))
    print("----------------------------")

ten, d_toan, d_ly, d_hoa = nhap_thong_tin()
dtb_kq = tinh_trung_binh(d_toan, d_ly, d_hoa)
xuat_ket_qua(ten, d_toan, d_ly, d_hoa, dtb_kq)