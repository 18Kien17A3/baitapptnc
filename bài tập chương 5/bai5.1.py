import sqlite3
import matplotlib.pyplot as plt
# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# Truy vấn dữ liệu từ cơ sở dữ liệu
cursor.execute("SELECT 'Tên', 'Tuổi' FROM users")
rows = cursor.fetchall()
# Tách dữ liệu thành hai danh sách riêng biệt cho tên và tuổi
Tên = [row[0] for row in rows]
Tuổi = [row[1] for row in rows]
#In ra các dòng trong bảng sau khi cập nhật
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)
# Đóng kết nối
conn.close()
# Vẽ biểu đồ cột
plt.bar(Tên, Tuổi)
plt.xlabel('Tên')
plt.ylabel('Tuổi')
plt.title('Biểu đồ tuổi của người dùng')
plt.show()