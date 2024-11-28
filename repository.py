from book import Book

class BookRepository:
    """
    Класс BookRepository отвечает за управление данными книг, включая их хранение, загрузку и обновление.

    Атрибуты класса:
    ----------------
    FILE : str
        Имя файла для хранения данных о книгах.

    Атрибуты экземпляра:
    --------------------
    books : list
        Список объектов книг, хранящихся в репозитории.
    """

    FILE = "books.txt"

    def __init__(self):
        self.books = []
        self.load_from_file()

    def add(self, book):
        """
        Добавляет новую книгу в репозиторий и сохраняет изменения в файл.
        """

        self.books.append(book)
        self.store_to_file()

    def get(self, id):
        """
        Возвращает книгу по её ID.
        """

        for book in self.books:
            if book.id == id:
                return book
        return None
    
    def get_all(self):
        """
        Возвращает список всех книг.
        """

        return self.books
    
    def update(self, old_book, new_book):
        """
        Обновляет данные существующей книги, заменяя её новой версией.
        """

        self.delete(old_book.id)
        self.add(new_book)
        self.store_to_file()
        return
    
    def delete(self, id):
        """
        Удаляет книгу по её ID.
        """

        for b in self.books:
            if b.id == id:
                self.books.remove(b)
                self.store_to_file()
                return
        raise Exception("Книга не найдена.") 
    
    def store_to_file(self):
        """
        Сохраняет список книг в файл в формате:
        "<ID>|<Название>|<Автор>|<Год>|<Статус>"
        """

        with open(self.FILE, "w", encoding="utf-8") as file:
            self.books = sorted(self.books, key=lambda book: book.id)
            for book in self.books:
                file.write(f"{book.id}|{book.title}|{book.author}|{book.year}|{book.status}\n")

    def load_from_file(self):
        """
        Загружает список книг из файла. Если файл отсутствует, создаёт пустой репозиторий.

        Формат файла:
        -------------
        Каждая строка содержит данные книги в формате:
        "<ID>|<Название>|<Автор>|<Год>|<Статус>"

        Исключения:
        -----------
        FileNotFoundError
            Если файл не найден, загружает пустой список книг.
        """

        try:
            with open(self.FILE, "r", encoding="utf-8") as file:
                for line in file:
                    id, title, author, year, status = line.strip().split("|")
                    self.books.append(Book(title, author, year, int(id), status))
            if self.books:
                Book.consecutive_id = max(book.id for book in self.books) + 1
        except FileNotFoundError:
            pass