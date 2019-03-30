import re
import nltk
import csv

# nltk.download('stopwords')


stop_words = set(nltk.corpus.stopwords.words('english'))
stop_words.add("amp")


def cleanTweet(tweet):
    tweet = tweet.lower()

    # Convert www.* or https?://* to nothing
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)
    tweet = re.sub('((www\.[^\s]+)|(http?://[^\s]+))', '', tweet)

    # Convert @username to nothing
    tweet = re.sub('@[^\s]+', '', tweet)

    tweet_words = tweet.split(' ')
    # removing stop words
    for i in range(0, len(tweet_words)):
        if tweet_words[i] in stop_words:
            tweet_words[i] = ''
    tweet = ' '.join(tweet_words)

    # Removing unnecessary characters like . ?
    tweet = re.sub('''[“”\.\n?!@#$%^&*(){}<>'"|[\],‘;/\-:_]''', ' ', tweet)
    tweet = re.sub(" s "," ",tweet)

    # Repeating words like happyyyyyyyy
    rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
    tweet = rpt_regex.sub(r"\1\1", tweet)

    # Emoticons
    emoticons = [
            ('__positive__', [':-)', ':)', '(:', '(-:',':-D', ':D', 'X-D', 'XD', 'xD',
                              '<3', ':\*', ';-)', ';)', ';-D', ';D', '(;', '(-;', ]),
            ('__negative__', [':-(', ':(', '(:', '(-:', ':,(',':\'(', ':"(', ':((', ]),]

    def replace_parenth(arr):
        return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

    def regex_join(arr):
        return '(' + '|'.join(arr) + ')'

    emoticons_regex = [(repl, re.compile(regex_join(replace_parenth(regx)))) \
                       for (repl, regx) in emoticons]

    for (repl, regx) in emoticons_regex:
        tweet = re.sub(regx, ' ' + repl + ' ', tweet)

    tweet = re.sub(" "*3," ",tweet)
    tweet = re.sub(" "*2," ",tweet)

    # trim
    tweet = tweet.lstrip(" ")
    tweet = tweet.rstrip(" ")

    return tweet


def cleanTweets(tweets):
    """
    Function to perform pre processing on every tweet in the list.
    :param tweets: list of tweets
    :return: list of pre processed tweets
    """
    preprocessed_tweets = []
    for tweet in tweets:  # tweet is a dict object
        tweet['text'] = cleanTweet(tweet['text'])
        preprocessed_tweets.append(tweet)
    return preprocessed_tweets


if __name__ == '__main__':
    input_file = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\Annotated_MODI_2000.csv"
    output_file = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\pp Annotated_MODI_2000.csv"
    with open(input_file, mode='r', newline="") as in_f:
        file_reader = csv.reader(in_f)
        rows = []
        for row in file_reader:
            rows.append(row)
        with open(output_file, mode='w+', newline='') as out_f:
            file_writer = csv.writer(out_f)
            for row in rows:
                output_row = []
                output_row.append(cleanTweet(row[1]))
                output_row.append(row[2])
                file_writer.writerow(output_row)
    # print(cleanTweet("""
    # congress  president rahul gandhi used figures of declining investments to  taunt the modi government over its 'make in india' initiative, terming  the numbers an update on the "fake in india programme".
    # """))
    # print(cleanTweet(" solider captured prime moron narendra modi done nothing 5 years impress voters amp using indian armed forces hide failures amp win 2019 general election abhinanden saynotowar bringbackabhinandan "))
    # print(" abv".lstrip(" "))
