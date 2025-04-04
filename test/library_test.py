import unittest
from unittest.mock import Mock
from src.library import Library
from src.library_repository import LibraryRepository

class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock(spec=LibraryRepository)
        self.library = Library(self.mock_repository)

    def test_borrow_book_success(self):
        self.mock_repository.remove_book.return_value = True
        result = self.library.borrow_book("Test Book")
        self.assertTrue(result)
        self.mock_repository.remove_book.assert_called_once_with("Test Book")

    def test_borrow_book_not_found(self):
        self.mock_repository.remove_book.return_value = False
        result = self.library.borrow_book("Non-existent Book")
        self.assertFalse(result)
        self.mock_repository.remove_book.assert_called_once_with("Non-existent Book")

    def test_return_book(self):
        self.library.return_book("Test Book", "Test Author", 2024)
        self.mock_repository.add_book.assert_called_once_with("Test Book", "Test Author", 2024)

    def test_list_books(self):
        expected_books = [("Book1", "Author1", 2024), ("Book2", "Author2", 2023)]
        self.mock_repository.get_all_books.return_value = expected_books
        result = self.library.list_books()
        self.assertEqual(result, expected_books)
        self.mock_repository.get_all_books.assert_called_once()

if __name__ == '__main__':
    unittest.main()