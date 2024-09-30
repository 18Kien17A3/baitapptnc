class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1


class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date  
        self.start_date = start_date  

    def display_info(self):
        print(f"Tên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.birth_date.display()
        print("Ngày vào công ty:", end=" ")
        self.start_date.display()

# Chương trình để quản lý nhân viên trong công ty
def main():
    employees = []  # Danh sách để lưu trữ nhân viên

    while True:
        print("\nQuản lý nhân viên:")
        print("1. Thêm nhân viên")
        print("2. Hiển thị thông tin nhân viên")
        print("3. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3): ")

        if choice == '1':
            name = input("Nhập họ tên nhân viên: ")
            day = int(input("Nhập ngày sinh: "))
            month = int(input("Nhập tháng sinh: "))
            year = int(input("Nhập năm sinh: "))
            birth_date = Date(day, month, year)

            day = int(input("Nhập ngày vào công ty: "))
            month = int(input("Nhập tháng vào công ty: "))
            year = int(input("Nhập năm vào công ty: "))
            start_date = Date(day, month, year)

            employee = Employee(name, birth_date, start_date)
            employees.append(employee)
            print("Nhân viên đã được thêm thành công!")

        elif choice == '2':
            print("\nThông tin nhân viên:")
            for emp in employees:
                emp.display_info()
                print("---------------")

        elif choice == '3':
            print("Thoát chương trình.")
            break

        else:
            print("Tùy chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
