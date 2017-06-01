# miercolesSpotifyBot v0.3
Python 3 Spotify bot that adds Spotify tracks to a playlist for future listening based on tracks sent to a Telegram group chat. 

## Git
* [Git Commit Format](http://udacity.github.io/git-styleguide/)
## Usage
1. Clone repo
2. pip install spotipy
3. Set environment variables. 
    On Linux 
    >export SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID  
    >export SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET  
    >export SPOTIFY_REDIRECT_URI=YOUR_REDIRECT_URI  

    On Windows
    >setx SPOTIFY_CLIENT_ID YOUR_CLIENT_ID  
    >setx SPOTIFY_CLIENT_SECRET YOUR_CLIENT_SECRET  
    >setx SPOTIFY_REDIRECT_URI YOUR_REDIRECT_URI  
4. To test proper installation, run spotifyFunctions.py. After inputting your Spotify username, you should have a playlist named *Test*. It should contain the following tracks:

    | Track Name| Artist |
    | ----- | :----------- |
    | '57 Strat 2 | John Jorgenson Electric Band |
    | Please Come Home | Gary Clark Jr. |
    | Daylight | Mandolin Orange |
    | Whiskey Lullaby | J2B2 |
    | The Blues Don't Change | Albert King |
    | Rodeo | Futurebirds|

Output after running spotifyFunctions.py is as follows:
 > `Playlist will be colaborative by default and named Test`  
 > `Tracks to insert using Track ID:`   
 > `Albert King - Blues Don't Change`  
 > `Futurebirds - Rodeo`  
 > `Tracks to insert using URI:`  
 > `Mandolin Orange - Daylight`  
 > `J2B2 - Whiskey Lullaby`  
 > `Tracks to insert using Track URL:`  
 > `John Jorgenson Electric Band - '57 Strat 2`  
    
## spotifyFunctions
This module contains relevant functions for the creation and manipulation of Spotify playlists.
* [Definition of `Playlist' object per Spotify WebAPI documentartion](https://developer.spotify.com/web-api/object-model/#playlist-object-full)

### Functions provided by spotifyFunctions

`login(user)`  
Authenticates a user. Takes username as parameter. 
Returns a `Spotify` object.

`createPlaylist(spotify, user, playlistName, public = True)`  
Create a playlist with name = `playlistName`. It is a public playlist by default. Takes a `Spotify` object, `username` string, `playlistName` string as parameters. Returns a playlist creation confirmation string. 

`getPlaylist(spotify, user, playlistName, limit = 50)`  
Gets a `Playlist` object with name = `playlistName`. Takes a `Spotify` object, `username` string, `playlistName` string as parameters. Returns a `Playlist` object. 
 
 `makeCollaborative(spotify, user, playlist)`  
Makes a `playlist` collaborative. Takes a `Spotify` object, `username` string, `Playlist` object as parameters. Returns a `Playlist` object.
 
 `insertTracks(spotify, user, playlist, tracks)`  
 Inserts `tracks` into a `playlist`. Takes a `Spotify` object, `username` string, `Playlist` object, `tracks` array as parameters. Returns a `snapshot_id` of the transaction. 
 `tracks` is an array that can contain Spotify tracks in the form of a `trackId`, `track URI` or `track URL`. 

 `getPlaylistURI(playlist)`  
 Gets the URI of a `playlist`. Takes a `Playlist` object as parameter. Returns the URI of a `playlist`.
 
 `getPlaylistURL(playlist)`  
 Gets the URL of a `playlist`. Takes a `Playlist` object as parameter. Returns the URL of a `playlist`.
