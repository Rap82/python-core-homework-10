"""Імпортуємо *UserDict(клас словників) з бібліотеки *collections
який буде батьківським для нашого *class AddressBook"""
from collections import UserDict


class Field:
    """Клас є батьківським для всіх полів, у ньому реалізується логіка,
    загальна для всіх полів."""

    def __init__(self, value):
        if not self.is_valide(value):
            raise ValueError
        self.value = value

    def is_valide(self, _):
        """Метод перевіряє дані з конструктора *__init__(self, value)
        на валідність(чи вони відповідають умовам завдання).
        В батьківському *class Field, повертаємо всім аргументам *True.
        В субкласах для яких *class Field - буде батьківським - цей метод будемо модифікувати
        в залежності від вимог до даних субкаласу."""

        return True

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас --- обов'язкове поле з ім'ям."""


class Phone(Field):
    """Клас немає власного конструкора, наслідує поля і методи від *class Field"""

    def is_valide(self, value):
        return len(value) == 10 and int(value)

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value


class Record:
    """Клас відповідає за логіку додавання/видалення/редагування
    необов'язкових полів та зберігання обов'язкового поля Name."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Метод додає телефон в поле рекорд class Record"""

        self.phone = Phone(phone)
        self.phones.append(self.phone)

    def remove_phone(self, del_phone: Phone):
        """Метод видаляє збережений телефон з поля рекорд class Record"""
        
        del_phone = Phone(del_phone)
        self.phones.remove(del_phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        """Метод змінює збережений телефон з поля рекорд *class Record.
        Якщо такого телефона не має повертає згенерованну нами помилку *raise ValueError
        """
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        found = False

        for i, _ in enumerate(self.phones):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone
                return self.phones[i]

        if not found:
            raise ValueError

    def find_phone(self, numbre_phone):
        """Мотод пошуку телефону в полі рекорд *class Record"""

        numbre_phone = Phone(numbre_phone)

        for i, _ in enumerate(self.phones):
            if self.phones[i] == numbre_phone:
                return self.phones[i]

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Субклас для батьтківського *UserDict,  де реалізовано логіку роботи з адресоною книжкою,
    Додавати записи, видаляти записи, шукати записи за іменем."""

    def add_record(self, name):
        """Метод додає запис(рекорд) в адресну книжку *class AddressBook"""

        
        self.data[f"{name.name}"] = name

    def delete(self, name):
        """Метод видаляє запис(рекорд) в адресну книжку *class AddressBook"""

        
        for key_name in self.data.keys():
            if key_name == name:
                self.data.pop(key_name)
                return self.data
        return None

    def find(self, name):
        """Метод шукає запис(рекорд) за іменем в адресній книжці *class AddressBook"""


        for key_name in self.data.keys():
            if key_name == name:
                return self.data[name]
        return None
