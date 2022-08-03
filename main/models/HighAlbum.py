from sqlite3 import connect
from ..config.mysqlconnection import connectToMySQL

class HighAlbum:
    db = 'vinyls'
    def __init__(self, data):
        self.album = data['album'];

    @classmethod

    def get_one_album(cls):

        query = 'SELECT * FROM vinyls.randomhighrating ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    




