import os

from spotify_client import SpotifyClient
def start():
     spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
     random_song = spotify_client.get_random_song()
     song_id = [song['id'] for song in random_song]
     
     added_song = spotify_client.add_songs(song_id)
     if added_song:
         for song in random_song:
             print(f"Added {song['name']} to playlist")
     
     if __name__ == '__main__':
                 start()