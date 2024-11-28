from book import Book

class Console:
    """
    Класс Console предоставляет интерфейс командной строки для управления книгами через контроллер.
    """

    def __init__(self, controller):
        self.controller = controller

    def get_all(self):
        """
        Отображает список всех книг.
        """

        books = self.controller.get_all()
        for book in books:
            print(book.__str__())

    
    def get(self, id):
        """
        Отображает информацию о книге по её ID.
        """

        book = self.controller.get(id)
        if book is None:
            print("Книга не найдена.")
        else:
            print(book.__str__())

    def add(self, title, author, year):
        """
        Добавляет новую книгу.
        """

        book = Book(title, author, year)
        try:
            self.controller.add(book)
            print("Книга добавлена.")
        except Exception as e:
            print(e)
        
    def update(self, id, title, author, year, status):
        """
        Обновляет информацию о книге.
        """

        book = Book(title, author, year, id, status)
        self.controller.update(self.controller.get(id), book)

    def delete(self, id):
        """
        Удаляет книгу по её ID.
        """

        try:
            self.controller.delete(id)
            print("Книга удалена.")
        except Exception as e:
            print(e)

    def update_status(self, id, status):
        """
        Обновляет статус книги (например, "в наличии" или "выдана").
        """

        old_book = self.controller.get(id)
        try:
            self.update(id, old_book.title, old_book.author,  old_book.year, status)
            print("Статус книги обновлен.")
        except Exception as e:
            print(e)
        
    def find_books(self, query):
        """
        Выполняет поиск книг по названию, автору или году.
        """

        books = self.controller.find_books(query)
        
        if not books:
            print("Книги не найдены.")
        else:
            for book in books:
                print(book.__str__())

    def str_to_int(self, string):
        """
        Преобразует строку в целое число. Если преобразование невозможно, выводит сообщение об ошибке.
        """

        try: 
            return int(string)
        except ValueError:
            print("Пожалуйста, введите число.")
            

    def run(self):
        """
        Запускает цикл взаимодействия с пользователем через консоль.
        """

        while True:
            
            print("1. Добавить книгу.")
            print("2. Удалить книгу.")
            print("3. Найти книгу по названию, автору или году издания.")
            print("4. Отобразить все книги.")
            print("5. Изменить статус книги.")            
            print("0. Выйти.")
            print("Введите номер команды: ", end="")

            choice = self.str_to_int(input())

            match choice:
                case 1:
                    self.add(
                        input("Введите название книги.\n> ").strip(), 
                        input("Введите автора книги.\n> ").strip(), 
                        self.str_to_int(input("Введите год издания книги.\n> ")) 
                    )
                case 2:
                    self.delete(self.str_to_int(input("Введите id книги.\n> ")))
                case 3:
                    self.find_books(input("Введите название, автора или год издания книги.\n> ").strip())
                case 4:
                    self.get_all()
                case 5:
                    self.update_status(
                        self.str_to_int(input("Введите id книги, статус который хотите изменить.\n> ")), 
                        input("Введите новый статус (в наличии/выдана).\n> ").strip().lower().capitalize()
                    ) 
                case 0:
                    break

    
