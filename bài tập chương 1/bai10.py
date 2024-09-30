import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Điểm({self.x}, {self.y})"


class Elip(Diem):
    def __init__(self, x=0, y=0, truc_lon=1, truc_nho=1):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho
    
    def tinh_dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho
    
    def __str__(self):
        return (f"Elip có tâm tại {super().__str__()}, bán trục lớn {self.truc_lon}, "
                f"bán trục nhỏ {self.truc_nho}, diện tích {self.tinh_dien_tich():.2f}")


class DuongTron(Elip):
    def __init__(self, x=0, y=0, ban_kinh=1):
        super().__init__(x, y, ban_kinh, ban_kinh)
    
    def tinh_dien_tich(self):
        return math.pi * self.truc_lon**2
    
    def __str__(self):
        return (f"Đường tròn có tâm tại {super().__str__()}, bán kính {self.truc_lon}, "
                f"diện tích {self.tinh_dien_tich():.2f}")

elip = Elip(0, 0, 5, 3)
print(elip)

duong_tron = DuongTron(0, 0, 4)
print(duong_tron)
