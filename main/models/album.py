from sqlite3 import connect
from ..config.mysqlconnection import connectToMySQL

class Album:
    db = 'vinyls'
    def __init__(self, data):
        self.id = data['album_id']
        self.album = data['album']
        self.artist = data['artist']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod

    def get_one_vinyl(cls):

        query = 'SELECT * FROM vinyls.vinyls_sheet1 ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_one_rym(cls):

        query = 'SELECT * FROM vinyls.RYM ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def ryan(cls):

        query = 'SELECT * FROM vinyls.ryan ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def random_person(cls):

        query = 'SELECT * FROM vinyls.topalbumsrandomperson ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def great_scene(cls):

        query = 'SELECT * FROM vinyls.greatscene ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def jazz(cls):

        query = 'SELECT * FROM vinyls.jazz ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results


