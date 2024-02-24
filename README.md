# Twitter Bot

## Description
This Python script utilizes the Tweepy library to interact with the Twitter API, allowing you to automate various tasks such as posting tweets, following users, unfollowing users, retrieving tweets based on specific criteria, retweeting, liking tweets, and unliking tweets.

## Prerequisites
Before using the Twitter bot, you need to create a Twitter Developer account to obtain the necessary API keys and access tokens.

## Installation
1. Install Tweepy library:
   ```
   pip install tweepy
   ```

2. Replace placeholders in the code with your actual API keys and access tokens obtained from your Twitter Developer account.

## Usage
1. **Authentication**: The script authenticates with the Twitter API using the provided API keys and access tokens.
2. **Post a Tweet**: Use the `update_status` method to post a tweet.
3. **Follow a User**: Use the `create_friendship` method to follow a user.
4. **Unfollow a User**: Use the `destroy_friendship` method to unfollow a user.
5. **Retrieve Tweets**: Use the `search_tweets` method to retrieve tweets based on a query, count, and result type.
6. **Retweet a Tweet**: Use the `retweet` method to retweet a specific tweet.
7. **Like a Tweet**: Use the `create_favorite` method to like a specific tweet.
8. **Unlike a Tweet**: Use the `destroy_favorite` method to unlike a specific tweet.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
