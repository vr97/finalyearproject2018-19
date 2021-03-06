from TwitterAPI import TwitterAPI
import json
import time
from Code.Scripts.get_tokens import creds

class FetchTweets:

    def __init__(self):
        self.api = None
        self.query = None
        self.since_id = None
        self.max_id = None
        self.count = None  # count to pass in the api call
        self.tweets = None  # tweets will be TwitterResponse type object.
        self.path_to_save = None
        self.total_tweets = 0

    # Yash's API key
    def api_init__(self):
        self.api = TwitterAPI(consumer_key=creds["yash"]["consumer_key"],
                              consumer_secret=creds["yash"]["consumer_secret"],
                              access_token_key=creds["yash"]["access_token_key"],
                              access_token_secret=creds["yash"]["access_token_secret"])

    def call_api(self):
        self.tweets = self.api.request('search/tweets',
                                       {'q': self.query, 'count': self.count, 'tweet_mode': 'extended', 'lang': 'en',
                                        'since_id': self.since_id
                                        ,'max_id':self.max_id
                                        })
        # since_id = tweets.json()['statuses'][0]['id']

    @staticmethod
    def get_tweet_id(file):
        # takes in the json file and returns the tweet id
        return file['id_str']

    def save_to_drive(self):
        # print(self.tweets.json()['statuses'])
        files = self.tweets.json()['statuses']
        for file in files:
            file_path = self.path_to_save + '\\' + self.get_tweet_id(file) + '.json'
            with open(file_path, 'w') as f:
                json.dump(file, f)

    def initiate_data_collection(self):
        self.api_init__()
        self.call_api()
        self.save_to_drive()
        tweets_fetched=len(self.tweets.json()['statuses'])
        self.total_tweets += tweets_fetched
        self.max_id = self.tweets.json()['statuses']\
                          [len(self.tweets.json()['statuses'])-1]\
                          ['id'] - 1
        # self.since_id = self.tweets.json()['statuses'][0]['id'] + 1

        # print(len(self.tweets.json()))
        print("Tweets Fetched",tweets_fetched)


if __name__ == "__main__":

    fetch_tweets_obj = FetchTweets()
    fetch_tweets_obj.max_id = 1105461929294721025
    fetch_tweets_obj.since_id = 1105455176939298816
    fetch_tweets_obj.count = 100
    fetch_tweets_obj.query = 'narendra modi'
    fetch_tweets_obj.path_to_save = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query narendra modi"
    while True:
        fetch_tweets_obj.initiate_data_collection()
        print("total tweets yet :",fetch_tweets_obj.total_tweets)
        print('timer triggered!!')
        time.sleep(60)  # timer for 1 minute/s
