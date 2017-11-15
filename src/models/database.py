import sqlite3
import os

class Database:
  def __init__(self):
    self.connection = sqlite3.connect(os.environ['TABERNAC_DB'])

  def get_connection(self):
    return self.connection

  def close(self):
    self.connection.close()