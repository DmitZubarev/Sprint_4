import pytest


book_name = 'Book'

class TestBooksCollector:

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('name, expected', [
        ('B', True),
        ('B' * 40, True),
        ('B' * 41, False),
        ('', False)
    ])
    def test_add_new_book_invalid_name(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(book_name + '1')
        collector.add_new_book(book_name + '2')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Invalid genre')
        assert 'Invalid genre' not in collector.get_book_genre(book_name)

    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre('Nonexistent book', 'Фантастика')
        assert 'Nonexistent book' not in collector.get_books_genre()

    def test_get_book_genre_existent_book_with_genry(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_get_book_genre_existent_book_without_genry(self, collector):
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre_nonexistent_book(self, collector):
        assert collector.get_book_genre(book_name) is None

    def test_get_books_genre(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_books_genre() == {f'{book_name}': 'Фантастика'}

    def test_get_books_with_specific_genre_valid_genre(self, collector):
        collector.add_new_book(book_name + '1')
        collector.add_new_book(book_name + '2')
        collector.add_new_book(book_name + '3')
        collector.set_book_genre(book_name + '1', 'Фантастика')
        collector.set_book_genre(book_name + '2', 'Фантастика')
        collector.set_book_genre(book_name + '3', 'Ужасы')
        request = collector.get_books_with_specific_genre('Фантастика')
        assert len(request) == 2 and book_name + '2' in request

    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_books_with_specific_genre('Invalid genre') == []

    def test_get_books_with_specific_genre_nonexistent_book(self, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == []

    @pytest.mark.parametrize('genre, expected', [
        ('Фантастика', True),
        ('Ужасы', False),
        ('Детективы', False),
        ('Мультфильмы', True),
        ('Комедии', True)
    ])
    def test_get_books_for_children(self, collector, genre, expected):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert (book_name in collector.get_books_for_children()) == expected

    def test_add_book_in_favorites_existent_book(self, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book(self, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites('Nonexistent book')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [f'{book_name}']
