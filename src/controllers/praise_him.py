import re, time, os
from flask import jsonify, abort
from src.models.bible import Bible
from src.models.book import Book
from src.models.verse import Verse

class PraiseHim:
  def get_book(self, text):
    match = re.search('\d?\s?[a-zA-Z]+', text)

    return match.group(0)

  def get_chapter_and_verses(self, text):
    chapter_verse = []

    for value in text.split(' '):
      splits = value.split(':')

      if len(splits) > 1:
        chapter_verse = splits

    return chapter_verse

  def get_start_and_end_verse(self, text):
    return text.split('-')

  def get_text(self, bibles, book_id, chapter, start_verse, end_verse):
    text = {}

    if book_id and chapter and start_verse:
      verse = Verse()

      for bible in bibles:
        verses = verse.get_verses(bible["table"], book_id, chapter, start_verse, end_verse)
        verses.append({
          "url": bible["url"],
          "text": bible["version"]
        })

        text[bible["version"]] = verses

    return text

  def get_attachments(self, verse_text):
    attachments = []
    ts = time.time()

    for key, value in verse_text.items():
      attachment = {
        "title": key
      }

      text = ''
      for line in value:
        try:
          text += f'{line["verse"]} {line["text"]}\n'
        except KeyError:
          attachment["title"] = line["text"]
          attachment["title_link"] = line["url"]

      attachment["text"] = text
      attachment["ts"] = ts

      attachments.append(attachment)

    return attachments

  def handle(self, data):
    token = data["token"][0]
    text = data["text"][0]
    if token != os.environ["TABERNAC_TOKEN"] or text == "":
      abort(404)

    book = self.get_book(text)
    chapter, verses = self.get_chapter_and_verses(text)
    start_verse, end_verse = self.get_start_and_end_verse(verses)

    bibles = Bible().get_all_bibles()
    book_id = Book().get_book_by_name(book)
    verse_text = self.get_text(bibles, book_id, chapter, start_verse, end_verse)

    return jsonify({
      "return_type": "in_channel",
      "text": "Praise Him! †",
      "attachments": self.get_attachments(verse_text)
    })
