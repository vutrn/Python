
N = -1

while N < 0:
    N = int(input("Nhập số lượng nhân viên: "))
# N = int(input("Nhập số lượng nhân viên: "))


luong_co_ban = []
he_so_luong = []
hoa_hong = []
luong_thuc_te = []

for i in range(N):
    while True:
        luong = int(input(f"Nhập lương cơ bản của nhân viên {i+1}: "))
        if luong >= 0:
            luong_co_ban.append(luong)
            break
        else:
            print("Nhap lai")
    while True:
        bac = float(input(f"Nhập hệ số lương (bac) của nhân viên {i+1}: "))
        if bac >= 0:
            he_so_luong.append(bac)
            break
        else:
            print("Nhap lai")
    while True:
        hh = float(input(f"Nhập hoa hồng của nhân viên {i+1}: "))
        if hh >= 0:
            hoa_hong.append(hh)
            break
        else:
            print("Nhap lai")

for i in range(N):
    luong_thuc_te.append(luong_co_ban[i] * he_so_luong[i] + hoa_hong[i])

print("Những nhân viên có mức lương trên 5 triệu:")
for i in range(N):
    if luong_thuc_te[i] > 5000:
        print(f"Nhân viên {i+1}: Mức lương = {luong_thuc_te[i]:,.0f} VND")
