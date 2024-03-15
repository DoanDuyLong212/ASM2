class sach:
    def __init__(self,Ten_sach,Ten_tac_gia,Nha_xuat_ban,Nam_XB,Gia_ban):
        self.Ten_sach = Ten_sach
        self.Ten_tac_gia = Ten_tac_gia
        self.Nha_xuat_ban = Nha_xuat_ban
        self.Nam_XB = Nam_XB
        self.Gia_ban = Gia_ban
    def nhap(self):
        self.Ten_sach = input("Nhap ten sach: ")
        self.Ten_tac_gia = input("Nhap ten tac gia: ")
        self.Nha_xuat_ban = input("Nhap ten nha xuat ban: ")
        self.Nam_XB = int(input("Nhap nam xuat ban: "))
        self.Gia_ban = float(input("Nhap gia ban: "))
    def in_sach(self):
        print(f"Ten sach: {self.Ten_sach}")
        print(f"Ten tac gia: {self.Ten_tac_gia}")
        print(f"Nha xuat ban: {self.Nha_xuat_ban}")
        print(f"Nam xuat ban: {self.Nam_XB}")
        print(f"Gia: {self.Gia_ban}")
def doc_file(file_name):
    books = []
    with open("FU.txt", "r") as file:
        total_books = int(file.readline())
        for _ in range(total_books):
            ten_sach = file.readline().strip()
            ten_tac_gia = file.readline().strip()
            nha_xuat_ban = file.readline().strip()
            nam_XB = int(file.readline().strip())
            gia_ban = float(file.readline().strip())
            next(file)
            books.append(sach(ten_sach, ten_tac_gia, nha_xuat_ban, nam_XB, gia_ban))
    return books
def main():
    while True:
        print("Menu")
        print("1. Nhap thong tin cua n cuon sach cua FU")
        print("2. In ra man hinh thong tin vua nhap")
        print("3. Sap xep thong tin giam dan theo nam xuat ban va hien thi")
        print("4. Tim kiem theo ten sach")
        print("5. Tim kiem theo ten tac gia")
        print("6. Thoat")
        select = input("please enter your choice: ")
        if select == '6':
            break
        elif select == '1':
            data = []
            n = int(input("nhap vao so luong sach: "))
            for i in range(n):
                a = sach(None, None, None, None, None)
                a.nhap()
                data.append(a)
            with open("FU.txt",'w') as file:
                file.write(f"{n}\n")
                for i in data:
                    file.write(f"{i.Ten_sach}\n{i.Ten_tac_gia}\n{i.Nha_xuat_ban}\n{i.Nam_XB}\n{i.Gia_ban}\n\n")
                file.close()
        elif select == '2':
            a = open("FU.txt",'r')
            content = a.read()
            print(content)
        elif select == '3':
            data = doc_file('FU.txt')
            sorted_data = sorted(data, key=lambda x: (x.Nam_XB, x.Gia_ban), reverse=True)
            with open('FU2022.txt','w') as file:
                file.write(f"{len(data)}\n")
                for i in sorted_data:
                    file.write(f"{i.Ten_sach}\n{i.Ten_tac_gia}\n{i.Nha_xuat_ban}\n{i.Nam_XB}\n{i.Gia_ban}\n\n")
            print(open('FU2022.txt', 'r').read())
        elif select == '4':
            user_input = input("Ten sach can tim: ")
            data = doc_file('FU.txt')
            found = False
            for i in data:
                a = i.Ten_sach
                if a == user_input:
                    found = True
                    print(f"{i.Ten_sach},{i.Ten_tac_gia},{i.Nha_xuat_ban}")
            if not found:
                print('Khong tim thay cuon sach nao')
        elif select == '5':
            user_input = input("Ten tac gia can tim: ")
            data = doc_file('FU.txt')
            found = False
            dem = 1
            for i in data:
                if i.Ten_tac_gia == user_input:
                    found = True
                    print(f"{i.Ten_tac_gia},{i.Ten_sach},{dem}")
                    dem += 1
            if not found:
                print("khong tim thay tac gia tren")
        else:
            print("Ban da nhap sai, vui long nhap lai")
            continue
if __name__ == "__main__":
    main()