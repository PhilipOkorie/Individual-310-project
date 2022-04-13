import random
import string
import requests
import urllib

class SpotifyClient(object):
    def __available__(self,api_key):
        self.api_key= api_key
        pass
    
    def random_song():

        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)

           url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'
       
           response = requests.get(
            url,
           headers= {
               "Content Type" : "application/json",
               "Authorization" : f"Bearer {self.api_key}"
               
           }
       )
        response_json = response.json()
        songs = [song for song in response_json['songs']['items']]
        print(f'Found {len(songs)} from your search')
        
        return songs
    
    def added_song (self, song_id):
        url = 'https://api.spotify.com/v1/me/songs'
        
        response = requests.put(
            url,
            headers={
                "Content Type" : "application/json",
               "Authorization" : f"Bearer {self.api_key}"
               
            },
            json = {
                'ids': song_ids
            }
        )
        
        return response.ok
    