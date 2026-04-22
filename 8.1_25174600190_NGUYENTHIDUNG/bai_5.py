import msvcrt
def gia_tri_ascii():
    print("Nhấn phím bất kỳ (ESC để thoát):")

    while True:
        ch = msvcrt.getch()

        if ch == b'\x1b': 
            print("\nĐã thoát")
            break

        try:
            ky_tu = ch.decode('utf-8')
            print(f"Ký tự: {ky_tu} -> ASCII: {ord(ky_tu)}")
        except:
            print("Phím không hợp lệ")

gia_tri_ascii()