from nltk.stem import PorterStemmer


def stem(tweet):
    stemmer = PorterStemmer()
    words = [word.lower() for word in tweet.split() if len(word) >= 3]
    words = [stemmer.stem(word) for word in words]
    tweet_stem = ' '.join(words)
    return tweet_stem


if __name__ == '__main__':
    print(stem("This is a stem function __file."))
