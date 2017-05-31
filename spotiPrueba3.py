# Esto agrega una canción a un playlist, probar con
# Args
# 1: username
# 2: playlist_id
# 3: track_id
#
#   python spotiPrueba3.py user playlist_id track_id

import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
    print("USER: " + username)
    print("PLAYLIST ID: " + str(playlist_id))
    print("TRACK ID: " + str(track_ids))

else:
    print ("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print (results)
else:
    print ("Can't get token for", username)
