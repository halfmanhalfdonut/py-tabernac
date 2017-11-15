from src.models.database import Database

class Base:
  def __init__(self):
    self.db = Database()