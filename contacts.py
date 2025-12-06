
phonebook = []

def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    
    contact = {'name': name, 'phone': phone}
    phonebook.append(contact)

    print("Đã thêm liên hệ.")


def view_contacts():
    if not phonebook:
        print("Danh bạ rỗng.")
        return
    
    print("\n--- DANH SÁCH LIÊN HỆ ---")
    for i, contact in enumerate(phonebook, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")



