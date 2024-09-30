class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")


    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 28 
        return 0  # Nếu tháng không hợp lệ

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


date = Date(30, 9, 2024)  
date.display()             

date.next()               
date.display()          