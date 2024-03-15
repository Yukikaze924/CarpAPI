import pymysql
import configs.config as config

from pymysql.connections import Connection
from pymysql.cursors import Cursor


class Mysql:

    db: Connection
    cursor: Cursor

    def __init__(self):
        self.db = pymysql.connect(host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  user=config.DB_USER,
                                  password=config.DB_PASSWORD,
                                  database=config.DB_NAME)
        self.cursor = self.db.cursor()

    def getCursor(self):
        return self.cursor
