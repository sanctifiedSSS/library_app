class BookController:
    """
    Класс BookController отвечает за управление логикой операций с книгами
    и взаимодействие с уровнем сервисов, предоставляя упрощённый интерфейс для консоли.
    """

    def __init__(self, service):
        self.service = service

    def get(self, id):
        """
        Возвращает книгу по её ID.
        """

        return self.service.get(id)

    def get_all(self):
        """
        Возвращает список всех книг.
        """

        return self.service.get_all()

    def add(self, book):
        """
        Добавляет новую книгу.
        """

        self.service.add(book)

    def update(self, old_book, new_book):
        """
        Обновляет существующую книгу новыми данными.
        """

        self.service.update(old_book, new_book)

    def delete(self, id):
        """
        Удаляет книгу по её ID.
        """

        self.service.delete(id)

    def find_books(self, query):
        """
        Выполняет поиск книг по названию, автору или году.
        """

        return self.service.find_books(query)
