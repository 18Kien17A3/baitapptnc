from xml.dom import minidom

# Tải file sample.xml
doc = minidom.parse("sample.xml")

# Lấy root element 
root = doc.documentElement
print("Root element:", root.tagName)

# Lấy danh sách các staff
staffs = root.getElementsByTagName("staff")

# Duyệt qua từng staff và in thông tin
for staff in staffs:
    staff_id = staff.getElementsByTagName("id")[0].firstChild.data
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data

    print(f"staff ID: {staff_id}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
