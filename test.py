# nhap muc luong co ban va he so luong (bac) cua N nhan vien
# nhap vao hoa hong cua N nhan vien
# tinh va hien thi cac ban co muc luong tren 5 trieu
# Yeu cau he so bac va hoa hong khong duoc am (truong hop am thi nhap lai den khi dung)

N = int(input("Nhap so luong nhan vien: "))
luong_co_ban = []
for i in range(N):
    while True:
        luong = int(input("Nhập lương cơ bản của nhân viên {i+1}: "))
        if luong >= 0:
            luong_co_ban.append(luong)
            break
        else:
            print("Lương cơ bản không được âm. Nhập lại.")

# salary = float(input("Luong co ban: "))
# heso = float(input("He so: "))
# while heso < 0:
#     bonus = float(input("Enter the bonus: "))
# if salary * heso > 500000:
#     print("The employee has a bonus.")
# else:
#     print("The employee does not have a bonus.")
