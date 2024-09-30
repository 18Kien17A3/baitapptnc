class Stack:
    def __init__(self, size):
        """
        Hàm tạo, khởi tạo ngăn xếp với kích thước tối đa size.
        """
        self.size = size         # Kích thước tối đa của ngăn xếp
        self.stack = []          # Mảng động chứa các phần tử ngăn xếp
        self.top = -1            # Chỉ số đỉnh của ngăn xếp, -1 biểu thị ngăn xếp rỗng

    def __del__(self):
        """
        Hàm huỷ, giải phóng bộ nhớ ngăn xếp.
        """
        del self.stack

    def push(self, value):
        """
        Đưa một phần tử vào ngăn xếp.
        """
        if not self.isFull():
            self.stack.append(value)
            self.top += 1
            print(f"Đã đưa {value} vào ngăn xếp.")
        else:
            print("Ngăn xếp đầy, không thể thêm phần tử!")

    def pop(self):
        """
        Lấy một phần tử ra từ đỉnh ngăn xếp.
        """
        if not self.isEmpty():
            value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value
        else:
            print("Ngăn xếp rỗng, không có phần tử nào để lấy!")
            return None

    def isEmpty(self):
        """
        Kiểm tra ngăn xếp có rỗng hay không.
        """
        return self.top == -1

    def isFull(self):
        """
        Kiểm tra ngăn xếp có đầy hay không.
        """
        return self.top == self.size - 1

    def peek(self):
        """
        Xem phần tử ở đỉnh ngăn xếp mà không lấy ra.
        """
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print("Ngăn xếp rỗng.")
            return None
    
    def print(self):
        """In nội dung của ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:")
            for i in range(self.top + 1):
                print(self.stack[i])


stack = Stack(5)   
stack.push(1.2)      
stack.push(2.5)     
stack.push(3.7)     

stack.pop()         
stack.pop()          

print("Ngăn xếp có rỗng không?", stack.isEmpty())  
print("Ngăn xếp có đầy không?", stack.isFull())    

stack.push(4.1)      
stack.push(5.3)     
stack.push(6.6)     
stack.push(7.9)      

stack.print()
