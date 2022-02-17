import re
from prettytable import PrettyTable
import progressbar
import spotify_utils
import billboard_utils

trackTable = PrettyTable()
song_list = []

widgets = [' [',
           progressbar.Timer(format='Fetching Track IDs from Spotify'),
           '] ',
           progressbar.Bar('*'),
           ]

artist_name_filter = ['Featuring', 'feat', 'Feat.', '&', 'With', 'Duet', '+', 'x', 'X', 'Or', '(', ')', '[', ']', '!',
                      '.', ':']

trackTable.field_names = ["Track Name", "Artist", "Billboard Rank", "Spotify Track ID"]

date = input('Enter date (YYYY-MM-DD) : ')
song_names, song_artists, song_ranks = billboard_utils.getCharts(date=date)
spotifyTrackIds = []
bar = progressbar.ProgressBar(max_value=len(song_names), widgets=widgets)

for i in range(len(song_names)):
    track_name = re.sub(r'[^\w\s\+\$\#]', '', song_names[i].get_text())
    artist = ' '.join(i for i in song_artists[i].get_text().split() if i not in artist_name_filter)
    rank = song_ranks[i].get_text()
    spotifyTrackId = spotify_utils.getSpotifyTrackID(track_name, artist)

    spotifyTrackIds.append(spotifyTrackId)
    trackTable.add_row([track_name, artist, rank, spotifyTrackId])
    # song_list.append(Song(name=track_name, artist=artist, rank=rank, spotify_track_id=spotifyTrackId))
    bar.update(i)

print('\n')
print(trackTable)

playlist_name = 'Billboard Hot 100 ' + date

playlist_id = spotify_utils.createPlaylist(playlist_name)
spotifyTrackIds = [x for x in spotifyTrackIds if x != 0]
print(spotifyTrackIds)
spotify_utils.addTracks(playlist_id=playlist_id, track_list=spotifyTrackIds)
