import csv
import json
import os
from Code.Scripts.GetUnique import get_unique_elements
from Code.Scripts.preprocess import cleanTweets

# objective for the module is to:
# 1.read the tweets stored in json files
# 2.extract time, tweet text, tweet id
# 3.find unique tweets
# 4.store it in an csv file.


class StageData:

    def __init__(self):
        self.list_of_files = []
        self.tweets = []
        self.no_of_tweets = 0
        self.clean_tweets = []
        self.clean_unique_tweets = []
        self.unique_tweets = []
        self.input_file_path = ""
        self.output_file_path = ""
        print("---------Data Staging Module Initialised---------")

    def get_tweet_file_names(self) -> None:
        """
        To get all the file names of the json files in a directory
        and store it in list_of_files
        :return:None
        """
        self.list_of_files = os.listdir(self.input_file_path)
        no_of_files = len(self.list_of_files)
        for iterator in range(0, no_of_files):
            self.list_of_files[iterator] = self.input_file_path + "\\" + self.list_of_files[iterator]
        print("no of json files ",no_of_files)

    def read_tweets(self)-> None:
        """
        Walks through the directory and fetching tweet data from each file
        :return: None
        """
        self.no_of_tweets = len(self.list_of_files)
        for i in range(0, self.no_of_tweets):
        # for i in range(0,10): # running a small loop for testing purpose
            try:
                with open(self.list_of_files[i]) as json_file:
                    file = json.load(json_file)
                tweet = {'id': file['id']}
                try:
                    tweet['created_time'] = file['retweeted_status']['created_at']
                    tweet['text'] = file['retweeted_status']['full_text']
                except:
                    tweet['created_time'] = file['created_at']
                    tweet['text'] = file['full_text']
                self.tweets.append(tweet)
            except:
                print("Error for ",self.list_of_files[i])
            if i%1000 == 0:
                print(str(round(i/self.no_of_tweets,2)*100),"% read")
        print("All Tweets read into memory")

    def write_to_file_ann(self) -> None:
        """
        Function to store all the tweets to a csv file.
        :return: None
        """
        with open(self.output_file_path, mode='w', newline='') as csv_file:
            tweet = ['id', 'created_time', 'text']
            writer = csv.DictWriter(csv_file, fieldnames=tweet)
            writer.writeheader()
            for tweet in self.unique_tweets:
                try:
                    writer.writerow(tweet)
                except:
                    pass
        print("Tweets written to a file")

    def write_to_file(self) -> None:
        """
        Function to store all the tweets to a csv file.
        :return: None
        """
        with open(self.output_file_path, mode='w', newline='') as csv_file:
            tweet = ['id', 'created_time', 'text']
            writer = csv.DictWriter(csv_file, fieldnames=tweet)
            writer.writeheader()
            for tweet in self.clean_unique_tweets:
                try:
                    writer.writerow(tweet)
                except:
                    pass
        print("Tweets written to a file")


if __name__ == "__main__":
    path_to_files = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query rahul gandhi"
    output_file_path = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Pre Processed Tweets\\rahul gandhi.csv"
    output_for_annotation_path = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\query rahul gandhi.csv"

    objectStageData = StageData()
    # reading the tweets into RAM
    objectStageData.input_file_path = path_to_files
    objectStageData.get_tweet_file_names()
    objectStageData.read_tweets()
    # Staging the tweets for annotation
    objectStageData.unique_tweets = get_unique_elements(objectStageData.tweets,'text')  # ready for annotation
    objectStageData.output_file_path = output_for_annotation_path
    objectStageData.write_to_file_ann()
    # Stating the tweets for training
    objectStageData.clean_tweets = cleanTweets(objectStageData.tweets)
    objectStageData.clean_unique_tweets =get_unique_elements(objectStageData.clean_tweets, 'text')  # ready for training
    objectStageData.output_file_path = output_file_path
    objectStageData.write_to_file()
