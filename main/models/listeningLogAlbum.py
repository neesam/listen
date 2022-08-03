from ..config.mysqlconnection import connectToMySQL

class ListeningLogAlbum:
    db = 'vinyls'
    def __init__(self, data):
        self.id = data['album_id']
        self.album = data['album']
        self.artist = data['artist']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod

    def add_album(cls, data):

        query = "INSERT INTO listening_log_albums (album, artist, image, created_at, updated_at) VALUES (%(album)s, %(artist)s, %(image)s, NOW(), NOW());"

        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    @classmethod

    def get_albums(cls):

        query = "SELECT * FROM listening_log_albums ORDER BY created_at DESC;"

        results = connectToMySQL(cls.db).query_db(query)

        return results