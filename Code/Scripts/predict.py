from sklearn.externals import joblib
from Code.Scripts.stem import stem
from Code.Scripts.preprocess import cleanTweet


def predict(tweet):
    classifier = joblib.load('C:\\Users\\Vivek Rao\\PycharmProjects\\Campaign-Assistant-master\\Code\\Classifier\\Classifier_word_2.pkl')
    tweet_processed = stem(cleanTweet(tweet))
    X = [tweet_processed]
    sentiment = classifier.predict(X)[0]
    return sentiment


if __name__ == '__main__':
    print(predict("modi"))
    print(predict("modiji"))
