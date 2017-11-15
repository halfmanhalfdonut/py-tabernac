import random
from src.models.base import Base

class Chapter(Base):
  def get_random_chapter(self, bible, book_id):
    replacements = ( book_id, )

    cursor = self.db.get_connection().cursor()
    cursor.execute(f'SELECT COUNT(DISTINCT "chapter_id") FROM {bible} WHERE book_id = ?', replacements)

    return random.randint(1, cursor.fetchone()[0])