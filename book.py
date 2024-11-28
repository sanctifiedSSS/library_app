class Book:
    """
    Класс для представления книги в библиотеке.
    """

    consecutive_id = 1
    
    def __init__(self, title, author, year, id=None, status="В наличии"):
        self.id = id if id else Book.consecutive_id
        if not id:
            Book.consecutive_id += 1
        
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        
    def __str__(self):
        return f"{self.id} | {self.title} | {self.author} | {self.year} | {self.status}"