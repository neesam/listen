from ..config.mysqlconnection import connectToMySQL

class Brookfield:
    db = 'vinyls'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.link = data['link']

    @classmethod

    def get_my_albums(cls):

        query = 'SELECT * FROM brookfield ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_brookfield_by_id(cls, data):

        query = 'SELECT * FROM brookfield WHERE id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])