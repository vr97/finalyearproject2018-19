"""Authors:Animesh Yadav
          :Yash Tibrewal
Date: 7/1/19
Name: training.py
Version: 2.0
Function: This module is used for defining, training
and testing the SVM classifier and then dumping it as a pickle
file which can be reused for sentiment prediction.
Input: The training datasets from various sources.
Output: The result of tesing(recall,precision, F1-score etc) and
the trained classifier dumped in svmClassifier.pkl
"""

# Import required libraries

import csv
import sklearn.metrics
import xlrd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from Code.Scripts.stem import stem
from Code.Scripts.preprocess import stop_words
from sklearn.model_selection import train_test_split


# Generating the Training and testing vectors
def getTrainingAndTestData():
    X = []
    y = []
    classes = [-1, 1]
    # Training data 1: Sentiment 140
    loc = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Training Data\\Training Data Set - Copy.xls'
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(0,1921):
        # print(sheet.cell_value(i,0)," ",sheet.cell_value(i,1))
        X.append(str(sheet.cell_value(i,0)))
        y.append(int(sheet.cell_value(i,1)))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)
    return X_train, X_test, y_train, y_test


# Process Tweets (Stemming)
def processTweets(X_train, X_test):
    X_train = [stem(tweet) for tweet in X_train]
    X_test = [stem(tweet) for tweet in X_test]
    return X_train, X_test


# SVM classifier
def classifier(X_train, y_train):
    # min_df: setting a minimum threshold for the words (words having smaller value will be omitted)
    # max_df: setting a maximum threshold for the words (words having higher value will be omitted)
    vec = TfidfVectorizer(min_df=50, max_df=0.95, sublinear_tf=True, use_idf=True, analyzer="word",
                          stop_words = stop_words)
    # The lower the C the bigger the Gutter.
    svm_clf = svm.LinearSVC(C=0.9)
    vec_clf = Pipeline([('vectorizer', vec), ('pac', svm_clf)])
    vec_clf.fit(X_train, y_train)
    joblib.dump(vec_clf,
                'D:\\Users\\yashk\\Campaign-Assistant\\Code\\Classifier\\Classifier_word_fds.pkl',
                compress=3)
    return vec_clf


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = getTrainingAndTestData()
    X_train, X_test = processTweets(X_train, X_test)
    vec_clf = classifier(X_train, y_train)
    y_pred = vec_clf.predict(X_test)
    print(sklearn.metrics.classification_report(y_test, y_pred))

