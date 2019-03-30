import os
import csv

"""
    1. Find the number of tweets collected
    2. Find the number of unique tweets among the collected tweets
    3. Find the number of positive tweets and negative tweets.
"""

path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\"
path_to_unique_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\"


def count_tweets()->int:
    """
    traversing the directories in the given path and finding the number of json files in it
    :return: count of total files
    """
    directories = [item for item in os.listdir(path_to_tweets)]
    for i in range(0,len(directories)):
        directories[i] = path_to_tweets+directories[i]
    total_count = sum(len(os.listdir(directory)) for directory in directories)
    return total_count


def count_unique_tweets()->int:
    """
    reading the csv files and finding the number of rows in the given path
    :return: count total of rows in all files
    """
    files = [file for file in os.listdir(path_to_unique_tweets)]
    for i in range(0,len(files)):
        files[i] = path_to_unique_tweets+files[i]
    fileobjectlist = []
    for i in range(0,len(files)):
        fileobjectlist.append(csv.reader(open(files[i],'r')))
    total_count = 0
    for i in range(0,len(files)):
        total_count += sum(1 for _ in fileobjectlist[i])
    return total_count


def count_positives()->int:
    """
        uses the path to the classified tweets and counts the number of positives i.e. +1
    :return: a count of +1
    """
    pass


def count_negatives()->int:
    """
        uses the path to the classified tweets and counts the number of negatives i.e. -1
    :return: a count of -1
    """
    pass


if __name__ == "__main__":
    print(count_tweets())
    print(count_unique_tweets())
