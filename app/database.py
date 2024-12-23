from tinydb import TinyDB, Query
from tinydb.operations import set
import os

db_path = os.path.join(os.path.dirname(__file__), "library_db.json")
db = TinyDB(db_path)
books_table = db.table("books")
BookQuery = Query()

def get_all_books():
    """Получить все книги из базы данных."""
    return books_table.all()

def get_book(book_id: int):
    """Получить книгу по её ID."""
    return books_table.get(BookQuery.id == book_id)

def add_book(book_data: dict):
    """Добавить книгу в базу данных."""
    book_id = books_table.insert(book_data)
    books_table.update({"id": book_id}, doc_ids=[book_id])  # Добавляем ID в запись
    return book_id

def update_book(book_id: int, updated_data: dict):
    """Обновить данные книги по её ID."""
    books_table.update(updated_data, BookQuery.id == book_id)
    return get_book(book_id)

def delete_book(book_id: int):
    """Удалить книгу по её ID."""
    books_table.remove(BookQuery.id == book_id)
