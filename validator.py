class Validator:
    """
    Класс Validator отвечает за проверку корректности данных книги.
    """

    def __init__(self):
        pass

    def validate(self, book):
        """
        Проверяет корректность данных объекта книги.
        """

        if book.title == "":
            raise Exception("Название не может быть не заполнено.")
        if book.author == "":
            raise Exception("Автор не может быть не заполнен.")
        if book.year == "":
            raise Exception("Год не может быть не заполнен.")
        if book.year == None:
            raise Exception()
        if book.status != "В наличии" and book.status != "Выдана":
            raise Exception(f"Статус может быть только 'В наличии' или 'Выдана'.")
        
        
    