from repository import BookRepository
from validator import Validator
from service import BookService
from controller import BookController
from console import Console

def main():
    """
    Основная точка входа в программу.

    Создаёт зависимости, включая репозиторий, валидатор, сервис, контроллер и консоль.
    Затем запускает консольный интерфейс для взаимодействия с пользователем.
    """

    repository = BookRepository()
    validator = Validator()
    service = BookService(repository, validator)
    controller = BookController(service)
    console = Console(controller)
    

    console.run()

if __name__ == "__main__":
    main()