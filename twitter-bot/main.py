# require twitter api account and tweepy package
# import tweepy
# import time


# def init_twitter_api():
#     auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
#     auth.set_access_token('access_token', 'access_token_secret')

#     api = tweepy.API(auth)
#     return api


# def limit_handle(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(600)


# def follow_back(api):
#     for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#         if follower.name == 'some_name':
#             follower.follow()

#     return 0

# def like_key_tweet(api, search_key, times):
#     for tweet in limit_handle(tweepy.Cursor(api.search, search_key).items()):
#         try:
#             tweet.favorite()
#             print('like the tweet')
#         except tweepy.TweepError as err:
#             print(err.reason)
#         except StopIteration:
#             break


# def main():
#     api = init_twitter_api()
#     follow_back(api)
#     like_key_tweet(api, 'python', 2)


# if __name__ == "__main__":
#     main()
