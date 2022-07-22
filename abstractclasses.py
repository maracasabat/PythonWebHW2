from abc import ABC, abstractmethod
from collections import UserDict


class Record(ABC):
    @abstractmethod
    def add_address(self):
        pass

    def add_birthday(self):
        pass


class NoteBookRecord(ABC):
    @abstractmethod
    def add_teg(self):
        pass

    @abstractmethod
    def del_teg(self):
        pass


class SomeBook(UserDict, ABC):
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
