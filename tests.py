import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector

        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('books_name', ['', 'Что делать, если ваш кот хочет вас убить1', 'Что делать, если ваш кот хочет вас убить12'],
                             ids=[
                            'negative no name',
                            'negative  41',
                            'negative 42',
                             ])
    def test_add_new_book_negative(self, books_name):
        collector = BooksCollector()
        name = books_name
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_cannot_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Вий')
        collector.add_new_book('Оно')
        collector.add_new_book('Вий')
        assert collector.get_books_genre() == {'Вий': '', 'Оно': ''}


    def test_get_books_List_with_specific_genre(self, add_horror_books):

        assert add_horror_books.get_books_with_specific_genre('Ужасы') == ['Dracula', 'Вий']




    def test_added_book_have_not_genre(self, add_book):
        assert add_book.get_book_genre('Dracula') == ''


    def test_book_not_in_genre_age_raiting(self):
        collector = BooksCollector()
        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')
        children_list = collector.get_books_for_children()
        assert 'Dracula' not in children_list


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')
        assert collector.get_book_genre('Dracula') == 'Ужасы'




    def test_get_book_genre_by_name_positive(self, add_horror_books):
        assert add_horror_books.get_book_genre('Вий') == 'Ужасы'

    @pytest.mark.parametrize('book_name, result', [['Вредные советы', None], ['', None], [None, None]])
    def test_get_book_genre_by_name_negative(self, add_horror_books, book_name, result):
        name = book_name
        assert add_horror_books.get_book_genre(name) == result


    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Волшебник изумрудного города')
        collector.set_book_genre('Волшебник изумрудного города', 'Мультфильмы')
        assert collector.get_books_genre() == {'Волшебник изумрудного города': 'Мультфильмы'}

    def test_add_book_in_favorites_and_get_list_of_favourites(self, add_book):
        add_book.add_book_in_favorites('Dracula')
        assert add_book.get_list_of_favorites_books() == ['Dracula']

    def test_delete_book_from_the_list_of_favourites(self, add_book):
        add_book.add_book_in_favorites('Dracula')
        add_book.add_book_in_favorites('Оно')
        add_book.delete_book_from_favorites('Dracula')
        assert add_book.get_list_of_favorites_books() == ['Оно']








