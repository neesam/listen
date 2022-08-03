from main.models.listeningLogAlbum import ListeningLogAlbum
from main import app
from main.models.album import Album
from main.models.brookfield import Brookfield
from main.models.artist import Artist
from main.models.HighAlbum import HighAlbum
from flask import redirect, render_template, request, session

@app.route('/vinyls')
def random():

    return render_template('random_vinyl.html', albums = Album.get_one_vinyl())

@app.route('/magic-sheet')
def magicSheet():

    return render_template('profile_page.html', albums = Album.get_one_rym())

@app.route('/my-songs')
def piano():

    return render_template('brookfield.html', brookfield = Brookfield.get_my_albums())

@app.route('/random-artist')
def randomArtist():
    
    return render_template('random_artist.html', artists = Artist.get_one_artist())

@app.route('/random-album')
def randomHighAlbum():
    
    return render_template('random_highrating.html', albums = HighAlbum.get_one_album())

@app.route('/ryan-rym')
def randomRyan():
    
    return render_template('ryan.html', albums = Album.ryan())
    
@app.route('/add')
def add():
    return render_template('add_listening_log.html', albums = Album.get_one_rym)

@app.route('/add-listening-log', methods=['POST'])
def create_rating():

    data = {
        'album': request.form["album"],
        'artist': request.form['artist'],
        'image': request.form['image']
    }

    ListeningLogAlbum.add_album(data)
    
    return redirect('/vinyls')


@app.route('/listening-log')
def listeningLog():
    
        return render_template('listening_log.html', albums = ListeningLogAlbum.get_albums())

@app.route('/top-random')
def topRandom():
    
        return render_template('top_album_random_person.html', albums = Album.random_person())

@app.route('/great-scene')
def great_scene():
    
        return render_template('great_scene.html', albums = Album.great_scene())

@app.route('/jazz')
def jazz():
    
        return render_template('jazz.html', albums = Album.jazz())