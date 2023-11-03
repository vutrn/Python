# Nhập số lượng nhân viên
N = int(input("Nhập số lượng nhân viên: "))

# Khởi tạo danh sách lươn cơ bản và hệ số lương
luong_co_ban = []
he_so_luong = []

# Nhập thông tin lương cơ bản và hệ số lương cho từng nhân viên
for i in range(N):
    while True:
        luong = float(input(f"Nhập lương cơ bản của nhân viên {i+1}: "))
        if luong >= 0:
            luong_co_ban.append(luong)
            break
        else:
            print("Lương cơ bản không được âm. Nhập lại.")

    while True:
        bac = float(input(f"Nhập hệ số lương (bac) của nhân viên {i+1}: "))
        if bac >= 0:
            he_so_luong.append(bac)
            break
        else:
            print("Hệ số lương không được âm. Nhập lại.")

# Nhập thông tin hoa hồng cho từng nhân viên
hoa_hong = []
for i in range(N):
    while True:
        hh = float(input(f"Nhập hoa hồng của nhân viên {i+1}: "))
        if hh >= 0:
            hoa_hong.append(hh)
            break
        else:
            print("Hoa hồng không được âm. Nhập lại.")

# Tính lương thực tế cho từng nhân viên
luong_thuc_te = []
for i in range(N):
    luong_thuc_te.append(luong_co_ban[i] * he_so_luong[i] + hoa_hong[i])

# Hiển thị các nhân viên có mức lương trên 5 triệu
print("Những nhân viên có mức lương trên 5 triệu:")
for i in range(N):
    if luong_thuc_te[i] > 5000000:
        print(f"Nhân viên {i+1}: Mức lương = {luong_thuc_te[i]:,.0f} VND")
