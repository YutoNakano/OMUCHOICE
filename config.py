import os

from dotenv import load_dotenv

print(load_dotenv())

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
ACCESS_KEY=os.getenv("ACCESS_KEY")

 


def getConsumerKey():
    return CONSUMER_KEY


def getConsumerSecret():
    return CONSUMER_SECRET


def getAccessToken():
    return ACCESS_TOKEN


def getAccessSecret():
    return ACCESS_TOKEN_SECRET