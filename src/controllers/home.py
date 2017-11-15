import time
from flask import jsonify
from src.models.bible import Bible
from src.models.book import Book
from src.models.chapter import Chapter
from src.models.verse import Verse

class Home:
  def randomize(self):
    bible = Bible()
    random_bible = bible.get_random_bible()
    bible_table = random_bible["table"]

    book = Book()
    book_id = book.get_random_book()
    book_name = book.get_book(book_id)

    chapter = Chapter()
    chapter_id = chapter.get_random_chapter(bible_table, book_id)

    verse = Verse()
    verse_id = verse.get_random_verse(bible_table, book_id, chapter_id)
    verse_text = verse.get_verse(bible_table, book_id, chapter_id, verse_id)

    return jsonify({
      "response_type": "in_channel",
      "text": "Praise Him! †",
      "attachments": [
        {
          "title": random_bible["version"],
          "title_link": random_bible["url"],
          "text": f'{random_bible["version"]} † {book_name} {chapter_id}:{verse_id} † {verse_text}',
          "ts": time.time()
        }
      ]
    })