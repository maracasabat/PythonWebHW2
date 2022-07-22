from abc import ABC, abstractmethod
from collections import UserDict


class AbstractRecord(ABC):
    @abstractmethod
    def add_address(self):
        pass

    def add_birthday(self):
        pass


class AbstractNoteBook(ABC):
    @abstractmethod
    def add_teg(self):
        pass

    @abstractmethod
    def del_teg(self):
        pass


class AbstractAddressBook(ABC):
    @abstractmethod
    def add_record(self):
        pass

    @abstractmethod
    def delete_record(self):
        pass

    @abstractmethod
    def update_record(self):
        pass

    @abstractmethod
    def to_file(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass


class Record(AbstractRecord):
    def add_address(self):
        pass

    def add_birthday(self):
        pass


class NoteBookRecord(AbstractNoteBook):
    def add_teg(self):
        pass

    def del_teg(self):
        pass


class SomeBook(UserDict, AbstractAddressBook):
    def add_record(self):
        pass

    def delete_record(self):
        pass

    def update_record(self):
        pass

    def to_file(self):
        pass

    def save_data(self):
        pass

    def load_data(self):
        pass
