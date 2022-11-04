import psycopg2
from psycopg2.extras import RealDictCursor


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='test',
            user='admin',
            password='qwerty',
            host='localhost'
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        print('successful connect to db')
