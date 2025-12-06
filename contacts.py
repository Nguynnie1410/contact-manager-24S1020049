
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



def search_contact():
    name = input("Nhập tên cần tìm: ")

    found = False
    for contact in phonebook:
        if contact['name'].lower() == name.lower():
            print(f"Đã tìm thấy: {contact['name']} - {contact['phone']}")
            found = True
            break
    
    if not found:
        print("Không tìm thấy liên hệ.")

def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 1-4.")

if _name_== "_main_":
main()



