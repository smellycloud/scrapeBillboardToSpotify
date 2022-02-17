# scrapeBillboardToSpotify
Auto generate Spotify playlists with Billboard Top 100 songs from any date

## Instructions
1. In order to create a playlist in Spotify you must have an account with Spotify.
   If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App. https://developer.spotify.com/dashboard/

3. Go to Dashboard -> Edit Settings and change the Redirect URI to http://localhost:8080

4. Change Client ID and Secret ID in spotify_utils.py

```
python3 main.py
```
