import tweepy

#you must create a twitter developer account to get these
Auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
Auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')

#create API object
api = tweepy.API(Auth)

#test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#post a tweet using update_status
api.update_status("Enter your tweet here")

#follow a user
api.create_friendship("username")

#unfollow a user
api.destroy_freindship("username")

#retrieve tweets based on a query, the count is the number of tweets to retrieve and the result_type is the type of tweets to retrieve
api.search_tweets("q='query', count=100, result_type='recent'")

#retweet a tweet
tweet_ip = "Enter the id of the tweet you want to retweet"
api.retweet(tweet_ip)

#like a tweet 
tweet_like = "Enter the id of the tweet you want to like"
api.create_favorite(tweet_like)

#unlike a tweet
tweet_unlike = "Enter the id of the tweet you want to unlike"
api.destroy_favorite(tweet_unlike)

