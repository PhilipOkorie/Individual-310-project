import tweepy


consumerkey = "ueQaTBvQNy9la96aDeO4e3nn8"
consumersecret = "LVVExjxlpZlAHaySrTw0okcNSTiix2LDo4ALxaLJYqMZPb5ibd"
accesstoken = "3297429638-z2y1cugaD49cH8XEZeli2VYe4yLMPjE72ZtZ1nm"
accesssecret = "NkZhLAKCltu79L1pMLps2tgvlLzFA7hukMBQrzAxoEpqg"
 
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesssecret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))
    
 
 