from os import access
from pip._vendor import requests
import random
from random import randrange
import string
import urllib


Client_ID = "5c7e22d7440f49ffac5ba14e35db6d94" 
Client_Secret ="a8b7b071b2d8497b9bb03004969b6dcf "

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL,{'GRANT_TYPE': 'client_credentials','client_id':Client_ID, 'client_secret': Client_Secret})

auth_response_data= auth_response.json()
access_token = auth_response_data['access_token']

    
    
    
def random_song():

        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)
        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'
        response = requests.get(
            url,
           headers= {
               "Content Type" : "application/json",
               "Authorization" : f"Bearer {access_token}"
               
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
                'ids': song_id
            }
        )
        
        return response.ok
    