import random
from src.models.base import Base

class Verse(Base):
  def get_random_verse(self, bible, book_id, chapter_id):
    replacements = ( book_id, chapter_id, )

    cursor = self.db.get_connection().cursor()
    cursor.execute(f'SELECT COUNT("verse_id") FROM {bible} WHERE book_id = ? AND chapter_id = ?', replacements)

    return random.randint(1, cursor.fetchone()[0])

  def get_verse(self, bible, book_id, chapter_id, verse_id):
    replacements = ( book_id, chapter_id, verse_id )

    cursor = self.db.get_connection().cursor()
    cursor.execute(f'SELECT "text" FROM {bible} WHERE book_id = ? AND chapter_id = ? AND verse_id = ?', replacements)

    return cursor.fetchone()[0]

  def get_verses(self, bible, book_id, chapter_id, start_verse_id, end_verse_id):
    if end_verse_id:
      verse_range = range(int(start_verse_id), int(end_verse_id) + 1)
    else:
      verse_range = [ int(start_verse_id) ]

    verse_tuple = tuple(verse_range)
    placeholders = ( book_id, chapter_id, )
    replacements = placeholders + verse_tuple
    verse_placeholder = ','.join('?' * len(verse_tuple))
    verses = []

    cursor = self.db.get_connection().cursor()
    for row in cursor.execute(f'SELECT "verse_id", "text" FROM {bible} WHERE book_id = ? AND chapter_id = ? AND verse_id IN ({verse_placeholder})', replacements):
      verses.append({
        "verse": row[0],
        "text": row[1]
      })

    return verses