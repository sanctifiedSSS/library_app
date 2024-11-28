class BookService:
    """
    Класс BookService отвечает за обработку бизнес-логики работы с книгами.
    Включает операции валидации данных и взаимодействия с репозиторием.

    Атрибуты:
    ---------
    repository : BookRepository
        Репозиторий для управления данными книг.
    validator : Validator
        Объект для проверки корректности данных книги.
    """

    def __init__(self, repository, validator):
        self.repository = repository
        self.validator = validator

    def get(self, id):
        """
        Возвращает книгу по её ID.
        """

        return self.repository.get(id)

    def get_all(self):
        """
        Возвращает список всех книг.
        """
        
        return self.repository.get_all()

    def add(self, book):
        """
        Добавляет новую книгу после проверки её данных.
        """

        self.validator.validate(book)
        self.repository.add(book)

    def update(self, old_book, new_book):
        """
        Обновляет данные существующей книги.
        """

        self.validator.validate(new_book)
        self.repository.update(old_book, new_book)

    def delete(self, id):
        """
        Удаляет книгу по её ID.
        """

        self.repository.delete(id)
    
    def find_books(self, query):
        """
        Выполняет поиск книг по части названия, имени автора или году издания.
        """

        books = self.repository.get_all() 

        results = [
            book for book in books 
            if query in book.title.lower() or 
               query in book.author.lower() or 
               query in str(book.year)
        ]

        return results if results else None


