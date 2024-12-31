import numpy as np
# 1, Tạo numpy arr có giá trị từ 0 đến 9. Hiển thị các phần tử có trong arr, xem kiểu dl, kích thước 
arr = np.arange(10)
print(arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)

# 2, Tạo arr_odd và arr_even 
arr_odd = arr[arr%2 ==1] # các phần tử lẻ 
arr_even = arr[arr%2 ==0] # các phần tử chẵn 
print("Các phần tử lẻ là: ", arr_odd)
print("Các phần tử chẵn là:", arr_even)

# 3, Tạo arr_update_1 với các phần tử chẵn dữ nguyên, các phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr %2 == 0, arr, 100)
print(arr_update_1)