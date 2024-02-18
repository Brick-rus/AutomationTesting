# ----------------------------------------задача------------------------------------------------------------
# Класс Книга должен содержать информацию о названии, авторе и жанре книги. Метод show должен показать информацию
# об объекте. Создайте два разных объекта и вызовите у них метод show

# class Book:
#
#     def __init__(self, title: str, author: str, genre: str):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#
#     def show(self):
#         print(f" Название книги {self.title}, автор книги {self.author}, а её жанр {self.genre}.")
#
#
# book_1 = Book(title="Lord of the rings", author="Tolkien", genre="fantasy")
# book_1.show()
#
# book_2 = Book(title="War and piece", author="Tolstoi", genre="history")
# book_2.show()
#
# book_3 = Book(title="A Byte of Python", author="Swaroop Chitlur", genre="educational")
# book_3.show()

# ----------------------------------------задача------------------------------------------------------------
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе
# Метод show должен показать информацию об объекте. Создайте два разных объекта и вызовите у них метод show

# class Bank:
#
#     def __init__(self, user: str, balance: int):
#         self.user = user
#         self.balance = balance
#
#     def show(self):
#         print(f" Здравствуйте {self.user}, Ваш баланс составляет {self.balance}.")
#
#
# user_1 = Bank(user="Ivanov Ivan", balance=25630)
# user_1.show()
#
# user_2 = Bank(user="Petrov Evgeniy", balance=100000)
# user_2.show()
#
# user_3 = Bank(user="Aleksandra Timohina", balance=0)
# user_3.show()