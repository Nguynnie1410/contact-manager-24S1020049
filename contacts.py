
phonebook = []

def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    
    contact = {'name': name, 'phone': phone}
    phonebook.append(contact)

    print("Đã thêm liên hệ.")


