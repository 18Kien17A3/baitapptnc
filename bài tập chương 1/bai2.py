class TS:
    def __init__(self):
        self.name = ""
        self.diem_toan = 0
        self.diem_ly = 0 
        self.diem_hoa = 0
        
    def data(self):
        self.name = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm môn Toán của thí sinh:"))
        self.diem_ly = float(input("Nhập điểm môn Lý của thí sinh:"))
        self.diem_hoa = float(input("Nhập điểm môn Hóa của thí sinh:"))

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
        
    def print(self):
        print(f"Họ tên: {self.name}")
        print(f"Điểm môn Toán: {self.diem_toan}, Điểm môn Lý: {self.diem_ly}, Điểm môn Hóa: {self.diem_hoa} ")
        print(f"Tổng điểm: {self.tong_diem()}")

def danh_sach_ts():
    thi_sinh = []
    n = int(input("Nhập số lượng thí sinh:"))
    for _ in range(n):
        ts = TS()
        ts.data()
        thi_sinh.append(ts)
    return thi_sinh

# Hàm in danh sách thí sinh trúng tuyển
def danh_sach_ts_trung_tuyen(thi_sinh, diem_trung_tuyen=20):
    ts_trung_tuyen = [ts for ts in thi_sinh if ts.tong_diem() >= diem_trung_tuyen ]
    ts_trung_tuyen.sort(key=lambda ts: ts.tong_diem(), reverse=True)

    print("Danh sách thí sinh trúng tuyển:")
    for ts in ts_trung_tuyen:
        ts.print()
        print("*" * 50)

thi_sinh = danh_sach_ts()
danh_sach_ts_trung_tuyen(thi_sinh)
