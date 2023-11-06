import pytest

from main import BooksCollector

@pytest.fixture
def add_horror_books():
    collector = BooksCollector()
    collector.add_new_book('Dracula')
    collector.add_new_book('Вий')
    collector.set_book_genre('Dracula', 'Ужасы')
    collector.set_book_genre('Вий', 'Ужасы')
    return collector

@pytest.fixture
def add_book():
    collector = BooksCollector()
    collector.add_new_book('Dracula')
    collector.add_new_book('Оно')
    return collector


