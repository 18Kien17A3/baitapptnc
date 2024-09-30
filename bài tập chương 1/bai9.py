class DaGiac:
    def __init__(self, *canh):
        self.canh = canh  

    def chu_vi(self):
        return sum(self.canh)

    def dien_tich(self):
        raise NotImplementedError("Phương thức này cần được cài đặt ở lớp con.")

    def __str__(self):
        return f"Đa giác có các cạnh: {self.canh}"

class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__(day, day, cao, cao)  
        self.day = day
        self.cao = cao

    def dien_tich(self):
        return self.day * self.cao

    def __str__(self):
        return f"Hình bình hành với đáy = {self.day}, chiều cao = {self.cao}"

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def __str__(self):
        return f"Hình chữ nhật với chiều dài = {self.chieu_dai}, chiều rộng = {self.chieu_rong}"

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def __str__(self):
        return f"Hình vuông với cạnh = {self.canh}"

# Tạo một hình bình hành
hinh_binh_hanh = HinhBinhHanh(6, 4)
print(hinh_binh_hanh)
print(f"Chu vi: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích: {hinh_binh_hanh.dien_tich()}")

# Tạo một hình chữ nhật
hinh_chu_nhat = HinhChuNhat(5, 3)
print(hinh_chu_nhat)
print(f"Chu vi: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích: {hinh_chu_nhat.dien_tich()}")

# Tạo một hình vuông
hinh_vuong = HinhVuong(4)
print(hinh_vuong)
print(f"Chu vi: {hinh_vuong.chu_vi()}")
print(f"Diện tích: {hinh_vuong.dien_tich()}")
