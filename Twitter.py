import datetime
import requests
import tweepy
import os
import config
# apiを取得
auth = tweepy.OAuthHandler(config.getConsumerKey(), config.getConsumerSecret())
auth.set_access_token(config.getAccessToken(), config.getAccessSecret())
api = tweepy.API(auth)


def tweet_search(location, restaurant_name):
    tweet_list = []
    searchWord = [location, restaurant_name]  # 検索ワード複数
    print(location)
    print(restaurant_name)
    for status in api.search(q=searchWord, lang='ja', result_type='recent', count=8): # result_type は recent or popular or mixed
        
        userID = "ユーザーID:" + status.user.name  # userIDを表示
        userName = "ユーザー名:" + status.user.screen_name  # ユーザー名を表示
        time = status.created_at + datetime.timedelta(hours=9)
        tweet_Time = "投稿日時:" + str(status.created_at +
                                   datetime.timedelta(hours=30))  # 投稿日時を表示
        tweet = status.text  # ツイートを表示
        tweet_dic = {"userID": userID, "userName": userName,
                     "time": tweet_Time, "tweet_Time": tweet_Time, "tweet": tweet}
        tweet_list.append(tweet_dic)
    print(tweet_list)
    return tweet_list


