import sqlite3
import matplotlib.pyplot as plt
# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('ct_giadinh.db')
cursor = conn.cursor()
# Truy vấn dữ liệu từ bảng 'khoan_chi'
cursor.execute("SELECT * FROM khoan_chi")
rows = cursor.fetchall()
# Lấy thông tin về các tên cột
column_names = [description[0] for description in
cursor.description][1:]
# Tách dữ liệu thành hai danh sách riêng biệt c
loai_chi = column_names
tien_chi = rows[0][1:]
# Đóng kết nối
conn.close()