import json
from typing import Dict, Optional

class ContactBook:
    def __init__(self, file_path: str = "TelePhoneBook.json"):
        self.file_path = file_path
        self.contacts = self._load_contacts()

    def _load_contacts(self) -> Dict[str, Dict[str, Optional[str]]]:
        try:
            with open(self.file_path, 'r') as file:
                contacts = json.load(file)
        except FileNotFoundError:
            contacts = {
                "1": {"lastname": "Lastname_1", "firstname": "Firstname_1", "middlename": "Middlename_1",
                      "phonenumber": 111111111, "birthday": "01.01.1900", "email": "id_1@yandex.ru"},
                "2": {"lastname": "Lastname_2", "firstname": "Firstname_2", "middlename": "Middlename_3",
                      "phonenumber": 333333333, "birthday": "01.01.2000", "email": None},
                "3": {"lastname": None, "firstname": "Firstname_3", "middlename": None,
                      "phonenumber": 444444444, "birthday": None, "email": "id_3@yandex.ru"}
            }
        return contacts

    def _save_contacts(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, ensure_ascii=False)

    def list_contacts(self):
        if not self.contacts:
            print("В телефонной книге нет контактов.")
        else:
            for contact_id, contact in self.contacts.items():
                print(f"{contact_id}: {contact}")

    def get_contact(self, contact_id: str):
        contact = self.contacts.get(contact_id)
        if contact:
            print(contact)
        else:
            print(f"Контакт с идентификатором {contact_id} не найден.")

    def add_contact(self):
        contact_id = input("Введите идентификатор контакта: ")
        if contact_id in self.contacts:
            print("Контакт с таким идентификатором уже существует.")
            return

        lastname = input("Введите фамилию: ")
        firstname = input("Введите имя: ")
        middlename = input("Введите отчество: ")
        phonenumber = input("Введите номер телефона: ")
        birthday = input("Введите дату рождения (дд/мм/гггг): ")
        email = input("Введите email: ")

        contact = {'lastname': lastname, 'firstname': firstname, 'middlename': middlename,
                   'phonenumber': phonenumber, 'birthday': birthday, 'email': email}
        self.contacts[contact_id] = contact
        self._save_contacts()
        print("Контакт успешно добавлен.")

    def edit_contact(self):
        contact_id = input("Введите идентификатор контакта: ")
        contact = self.contacts.get(contact_id)
        if not contact:
            print(f"Контакт с идентификатором {contact_id} не найден.")
            return

        print("Выберите поле для редактирования:")
        print("1. Фамилия\n2. Имя\n3. Отчество\n4. Дата рождения\n5. Номер телефона\n6. Email")
        field_choice = input("Введите номер поля: ")

        if field_choice == "1":
            new_value = input("Введите новую фамилию: ")
            contact['lastname'] = new_value
        elif field_choice == "2":
            new_value = input("Введите новое имя: ")
            contact['firstname'] = new_value
        elif field_choice == "3":
            new_value = input("Введите новое отчество: ")
            contact['middlename'] = new_value
        elif field_choice == "4":
            new_value = input("Введите новую дату рождения (дд/мм/гггг): ")
            contact['birthday'] = new_value
        elif field_choice == "5":
            new_value = input("Введите новый номер телефона: ")
            contact['phonenumber'] = new_value
        elif field_choice == "6":
            new_value = input("Введите новый email: ")
            contact['email'] = new_value
        else:
            print("Неверный выбор.")
            return

        self.contacts[contact_id] = contact
        self._save_contacts()
        print("Контакт успешно обновлен.")

    def delete_contact(self):
        contact_id = input("Введите идентификатор контакта для удаления: ")
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self._save_contacts()
            print("Контакт успешно удален.")
        else:
            print(f"Контакт с идентификатором {contact_id} не найден.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nВыберите действие:")
        print("1. Вывести список контактов\n2. Найти контакт\n3. Добавить контакт\n4. Редактировать контакт\n5. Удалить контакт\n0. Выйти")
        choice = input("Введите выбор: ")

        if choice == "1":
            contact_book.list_contacts()
        elif choice == "2":
            contact_id = input("Введите идентификатор контакта: ")
            contact_book.get_contact(contact_id)
        elif choice == "3":
            contact_book.add_contact()
        elif choice == "4":
            contact_book.edit_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()