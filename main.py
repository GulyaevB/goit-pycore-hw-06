
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or (
            len(value) != 10 or not value.isascii()
            or not value.isdigit()
        ):
            raise ValueError("Phone number must contain 10 digits")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def find_phone(self, phone):
        for existing_phone in self.phones:
            if existing_phone.value == phone:
                return existing_phone

        return None

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    pass


if __name__ == "__main__":
    john = Record("John")

    john.add_phone("1234567890")
    john.add_phone("5555555555")

    print(john)
    print(john.find_phone("5555555555"))
    print(john.find_phone("0000000000"))
