import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b  
        self.c = c  
    
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = self.chu_vi() / 2  # Nửa chu vi
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __str__(self):
        return f"Tam giác có các cạnh: a = {self.a}, b = {self.b}, c = {self.c}"

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if not self.kiem_tra_vuong():
            raise ValueError("Tam giác này không phải tam giác vuông!")
    
    def kiem_tra_vuong(self):
        canh = sorted([self.a, self.b, self.c])
        return math.isclose(canh[0]**2 + canh[1]**2, canh[2]**2)
    
    def __str__(self):
        return f"Tam giác vuông có các cạnh: a = {self.a}, b = {self.b}, c = {self.c}"

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)
    
    def __str__(self):
        return f"Tam giác cân có hai cạnh bằng nhau: a = {self.a}, b = {self.b}"

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)
    
    def __str__(self):
        return f"Tam giác đều có ba cạnh bằng nhau: a = {self.a}"

tam_giac = TamGiac(3, 4, 5)
print(tam_giac)
print(f"Chu vi: {tam_giac.chu_vi()}")
print(f"Diện tích: {tam_giac.dien_tich():.2f}")

tam_giac_vuong = TamGiacVuong(3, 4, 5)
print(tam_giac_vuong)
print(f"Chu vi: {tam_giac_vuong.chu_vi()}")
print(f"Diện tích: {tam_giac_vuong.dien_tich():.2f}")

tam_giac_can = TamGiacCan(5, 7)
print(tam_giac_can)
print(f"Chu vi: {tam_giac_can.chu_vi()}")
print(f"Diện tích: {tam_giac_can.dien_tich():.2f}")

tam_giac_deu = TamGiacDeu(6)
print(tam_giac_deu)
print(f"Chu vi: {tam_giac_deu.chu_vi()}")
print(f"Diện tích: {tam_giac_deu.dien_tich():.2f}")
