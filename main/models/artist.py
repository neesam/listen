from ..config.mysqlconnection import connectToMySQL

class Artist:
    db = 'vinyls'
    def __init__(self, data):
        self.artist = data['artist']

    @classmethod

    def get_one_artist(cls):

        query = 'SELECT * FROM vinyls.randomartist ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return results