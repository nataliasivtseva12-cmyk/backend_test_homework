class Library :

    def __init__ (self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self. books:
            print(book)


    def find_book(self, book):
        if book in self.books:
            print(f'{book} есть в библиотеке')
        else:
            print(f'{book} нет в библиотеке')# Что вывести, если книги нет?
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'{book} удалена из библиотеки')
        else:
            print(f'{book} данной книги нет в библиотеке')

library = Library()

library.add_book('Гарри Поттер')
library.add_book('Мастер и Маргарита')
library.add_book('Маленький принц')

library.show_books()
print(library.books)
library.find_book('Гарри Поттер')
library.find_book('Война и мир')

library.remove_book('Гарри Поттер')
library.remove_book('Война и мир')

print(library.books)
