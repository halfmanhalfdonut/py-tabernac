import random
from src.models.base import Base

class Bible(Base):
  def get_all_bibles(self):
    bibles = []

    cursor = self.db.get_connection().cursor()
    for row in cursor.execute('SELECT "table", "version", "info_url" FROM "bible_versions"'):
      bibles.append({
        "table": row[0],
        "version": row[1],
        "url": row[2]
      })

    return bibles

  def get_random_bible(self):
    bibles = self.get_all_bibles()
    return bibles[random.randint(0, len(bibles) - 1)]

  def get_bible(self, id):
    replacements = ( id, )

    cursor = self.db.get_connection().cursor()
    cursor.execute('SELECT "table", "version", "info_url" FROM "bible_versions" where id = ?', replacements)

    keys = ( "table", "version", "url" )

    return dict(zip(keys, cursor.fetchone()))