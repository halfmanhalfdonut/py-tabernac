import random
from src.models.base import Base

class Book(Base):
  TOTAL_BOOKS = 66

  def get_random_book(self):
    return random.randint(1, self.TOTAL_BOOKS)

  def get_book(self, id):
    replacements = ( id, )
    cursor = self.db.get_connection().cursor()
    cursor.execute('SELECT "name" FROM "books" WHERE book_id = ?', replacements)
    return cursor.fetchone()[0]

  def get_book_by_name(self, name):
    replacements = ( name, )
    cursor = self.db.get_connection().cursor()
    cursor.execute('SELECT "book_id" FROM "books" WHERE name = ?', replacements)
    return cursor.fetchone()[0]
