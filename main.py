
from collections import UserDict


class Field:
    """Base class for contact fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for storing a contact name."""
    pass


class Phone(Field):
    """Class for storing and validating a phone number."""

    def __init__(self, value):
        # Phone must contain exactly 10 digits
        if not isinstance(value, str) or (
            len(value) != 10 or not value.isascii()
            or not value.isdigit()
        ):
            raise ValueError("Phone number must contain 10 digits")

        super().__init__(value)


class Record:
    """Class for storing a contact and its phone numbers."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Add a new phone number."""
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def find_phone(self, phone):
        """Find a phone number in the contact."""
        for existing_phone in self.phones:
            if existing_phone.value == phone:
                return existing_phone

        return None

    def edit_phone(self, old_phone, new_phone):
        """Replace an existing phone number."""
        existing_phone = self.find_phone(old_phone)

        if existing_phone is None:
            raise ValueError("Phone number not found")

        # Check the new phone before updating
        validated_phone = Phone(new_phone)
        existing_phone.value = validated_phone.value

    def remove_phone(self, phone):
        """Remove a phone number from the contact."""
        existing_phone = self.find_phone(phone)

        if existing_phone is not None:
            self.phones.remove(existing_phone)

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    """Class for managing contact records."""

    def add_record(self, record):
        """Add a contact record to the address book."""
        self.data[record.name.value] = record

    def find(self, name):
        """Find a contact record by name."""
        return self.data.get(name)

    def delete(self, name):
        """Delete a contact record by name."""
        self.data.pop(name, None)


if __name__ == "__main__":
    # Create an address book
    book = AddressBook()

    # Create and add John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Create and add Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Show all contacts
    print("All contacts:")
    for name, record in book.data.items():
        print(record)

    # Find and edit John's phone
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print("\nAfter editing John's phone:")
    print(john)

    # Find a phone number
    found_phone = john.find_phone("5555555555")
    print(f"\nFound phone: {found_phone}")

    # Delete Jane
    book.delete("Jane")

    print("\nAfter deleting Jane:")
    for name, record in book.data.items():
        print(record)
