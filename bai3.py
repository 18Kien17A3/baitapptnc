class PS:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.hop_le = self.kiem_tra_hop_le()
    
    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            print("Phân số không hợp lệ! Mẫu số phải khác 0.")
            return False
        return True

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            self.mau_so = int(input("Mẫu số không hợp lệ. Nhập lại mẫu số (mẫu số khác 0): "))

    def in_phan_so(self):
        if not self.hop_le:
            print("Phân số không hợp lệ.")
        elif self.tu_so == 0:
            print("0")
        else:
            print(f"{self.tu_so}/{self.mau_so}")

phan_so = PS()
phan_so.nhap_phan_so()
phan_so.in_phan_so()
