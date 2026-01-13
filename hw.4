class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) == 10

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError(f"Некорректный номер телефона: {phone_number}. Должно быть ровно 10 цифр.")

        new_contact = Contact(name, phone_number)

        cls.all_contacts.append(new_contact)
class Contact:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.phone_number = phone_number
        self.id = id

    @classmethod
    def validate_phone_number(cls, phone_number):
        return isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) == 10

class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError(f"Некорректный номер телефона: {phone_number}. Должно быть ровно 10 цифр.")

        cls.last_id += 1
        new_contact = Contact(name, phone_number, cls.last_id)

        cls.all_contacts.append(new_contact)
    @classmethod
    def remove_contact(cls, contact_id):

        for i, contact in enumerate(cls.all_contacts):
            if contact.id == contact_id:
                del cls.all_contacts[i]
                return
print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0500100200")
ContactList.add_contact("Виктор Цой", "0500223456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

print(ContactList.last_id)

ContactList.add_contact("Вася Пупкин", "0500100200")
ContactList.add_contact("Виктор Цой", "0500223456")
print(ContactList.last_id)

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)