#### Spotify Functions
# Series de funciones utilies para crear playlists y agregar canciones a las mismas
# Falta extender funcionalidad a seguir playlists y hacer busquedas, etc...


import pprint
import sys

import spotipy
import spotipy.util as util

#####Spotify Functions####
#Intentar volver esto en una clase que hereda de Spotipy para no tener que estar mandando spotify como paramatero
#Agregar manajo de excepciones
###########################

#recibe el nombre del login del usuario
#retorna un objeto spotify.
def login(user):
    scope = 'playlist-modify-public playlist-read-collaborative playlist-modify-private'
    token = util.prompt_for_user_token(user, scope)
    spotify = spotipy.Spotify(token)
    return spotify

#crea un playlist con nombre = playlistName
def createPlaylist(spotify, user, playlistName, public = True):
    spotify.user_playlist_create(user, playlistName, public)
    return 'Created Playlist'

#recupera el objeto Playlist correspondiente a playlist name
def getPlaylist(spotify, user, playlistName, limit = 50):
    playlists = spotify.user_playlists(user, limit)
    playlist = next(item for item in playlists['items'] if item['name'] == playlistName and item['collaborative'] == False)
    return playlist

#Vuelve una playlist colaborativa
def makeCollaborative(spotify, user, playlist):
    playlistId = playlist['id']
    spotify.user_playlist_change_details(user, playlistId, public = False, collaborative = True)
    playlist['collaborative'] = True
    playlist['public'] = False
    return playlist

#Agrega las canciones en el array tracks a la playlist
def insertTracks(spotify, user, playlist, tracks):
    playlistId = playlist['id']
    return spotify.user_playlist_add_tracks(user, playlistId, tracks)

def getPlaylistURL(playlist):
    return playlist['uri']



if (__name__ == '__main__'):
    testSongs = {"Albert King - Blues Don't Change": "3fCdsq5gd2DYoK8dQexTxa",
                  "Futurebirds - Rodeo": "2FMuoG8zdNhyfkCI2ZMgFe",
                  "Mandolin Orange - Daylight": "spotify:track:702VulzPRsk5vlGWNqwmXm",
                  "J2B2 - Whiskey Lullaby": "spotify:track:3xaGuX0Tho1wYsC7W2Gqz3",
                  "John Jorgenson Electric Band - '57 Strat 2": "https://open.spotify.com/track/2gyqukOFoLpgZvyF0HSoz0",
                  "Gary Clark Jr. - Please Come Home": "https://open.spotify.com/track/44jzDTPDYubeE97IZp2v0z"
                 }
    user = input('Username: \n').strip()
    spotify = login(user)
    playlistName = 'Test'
    createPlaylist(spotify, user, playlistName)
    print('Playlist will be colaborative by default and named Test')
    playlist = getPlaylist(spotify, user, playlistName)
    playlist = makeCollaborative(spotify, user, playlist)
    print("Tracks to insert using Track ID: \n{0}\n{1}".format(list(testSongs.keys())[0], list(testSongs.keys())[1]))
    results = insertTracks(spotify, user, playlist, [testSongs[list(testSongs.keys())[0]], testSongs[list(testSongs.keys())[1]]])
    print("Tracks to insert using URI: \n{0}\n{1}".format(list(testSongs.keys())[2], list(testSongs.keys())[3]))
    results = insertTracks(spotify, user, playlist, [testSongs[list(testSongs.keys())[2]], testSongs[list(testSongs.keys())[3]]])
    print("Tracks to insert using Track URL: \n{0}\n{1}".format(list(testSongs.keys())[4], list(testSongs.keys())[5]))
    results = insertTracks(spotify, user, playlist, [testSongs[list(testSongs.keys())[4]], testSongs[list(testSongs.keys())[5]]])
    print(getPlaylistURL(playlist))