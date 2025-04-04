from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from src.library_repository import LibraryRepository

class DictionaryLibraryRepository(LibraryRepository):
    def __init__(self):
        self.books: Dict[str, Tuple[str, int]] = {}

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = (author, year)

    def remove_book(self, title: str) -> bool:
        if title in self.books:
            del self.books[title]
            return True
        return False

    def get_all_books(self) -> List[Tuple[str, str, int]]:
        return [(title, author, year)
                for title, (author, year) in self.books.items()]