class hcn:
    def __init__(self):
        self.dai = 0
        self.rong = 0

    def nhap_2_canh(self):
        self.dai = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

    def tinh_chu_vi(self):
        return 2*(self.dai + self.rong)
    
    def tinh_dien_tich(self):
        return self.dai * self.rong
    
    def print(self):
        print(f"Hình chữ nhật có chiều dài: {self.dai}, chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

hinh_cn = hcn()
hinh_cn.nhap_2_canh()
hinh_cn.print()