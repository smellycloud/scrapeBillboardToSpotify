import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "playlist-modify-private"
SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='http://localhost:8080'
def authenticateAccount():
    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyImplicitGrant(client_id=SPOTIPY_CLIENT_ID))
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID,
                                  client_secret=SPOTIPY_CLIENT_SECRET,
                                  redirect_uri=SPOTIPY_REDIRECT_URI))

    return sp


spotify = authenticateAccount()
print(spotify.me())


def getSpotifyTrackID(track, artist):
    track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=10, offset=0, market=None)
    try:
        result = track_id['tracks']['items'][0]['id']
    except:
        result = 0
    return result


def createPlaylist(name, public=False, collaborative=False):
    try:
        playlist = spotify.user_playlist_create(user=spotify.me()['id'], name=name, public=public,
                                                collaborative=collaborative)
        print('Playlist', name, 'created successfully!')
        print('Playlist ID : ', playlist['id'])
        return playlist['id']
    except:
        print('Error while creating playlist')


def addTracks(track_list, playlist_id):
    try:
        spotify.playlist_add_items(playlist_id=playlist_id, items=track_list)
        print('Tracks added successfully!')
    except:
        print('Could not add tracks')
