from typing import List
from models.models import Book, Author
from config import db
from dto.dto import BookData, AuthorData


class BookService:
    @staticmethod
    def create(book_data: BookData) -> Book:
        book = Book(
            title=book_data.title,
            summary=book_data.summary,
            note=book_data.note,
            price=book_data.price,
            publication_date=book_data.publication_date,
            category=book_data.category,
            author_id=book_data.author_id
        )
        db.session.add(book)
        db.session.commit()
        return book

    @staticmethod
    def get_all() -> List[Book]:
        return Book.query.all()

    @staticmethod
    def get(id: int) -> Book:
        return Book.query.get(id)

    @staticmethod
    def update(id: int, book_data: BookData) -> Book:
        book = Book.query.get(id)
        if book is None:
            return None
        book.title = book_data.title
        book.summary = book_data.summary
        book.note = book_data.note
        book.price = book_data.price
        book.publication_date = book_data.publication_date
        book.categories = book_data.categories
        book.author_id = book_data.author_id
        db.session.commit()
        return book

    @staticmethod
    def delete_book(id: int) -> bool:
        book = Book.query.get(id)
        if book is None:
            return False
        db.session.delete(book)
        db.session.commit()
        return True


class AuthorService:
    @staticmethod
    def create(author_data: AuthorData) -> Author:
        author = Author(
            firstname=author_data.firstname,
            lastname=author_data.lastname
        )
        db.session.add(author)
        db.session.commit()
        return author

    @staticmethod
    def get_all() -> List[Author]:
        return Author.query.all()

    @staticmethod
    def get(author_id: int) -> Author:
        return Author.query.get(author_id)

    @staticmethod
    def update(author_id: int, author_data: AuthorData) -> Author:
        author = Author.query.get(author_id)
        if author is None:
            return None
        author.firstname = author_data.firstname
        author.lastname = author_data.lastname
        db.session.commit()
        return author

    @staticmethod
    def delete(author_id: int) -> bool:
        author = Author.query.get(author_id)
        if author is None:
            return False
        db.session.delete(author)
        db.session.commit()
        return True
