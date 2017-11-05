"""Submission for second assignment (decision trees)"""

import os
import pandas
import numpy
from sklearn.tree import DecisionTreeClassifier


def main():
    """Main function load titanic.csv and build decision tree"""
    # file path with data
    titanic_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
    # loading this file
    data = pandas.read_csv(titanic_path, index_col='PassengerId')
    # removing from sample rows with no information about age
    data = data.drop(data[numpy.isnan(data['Age'])].index)
    # leaving only needed features (from task)
    features = ['Pclass', 'Fare', 'Age', 'Sex']
    # filtering dataframe by features
    sample = data.filter(items=features)
    # replacing male/female to 1/0 because classifier can work
    # only with numbers
    sample['Sex'] = sample['Sex'].map({'male': 1, 'female': 0})
    print 'Given sample:\n', sample
    # creating decision tree classifier. 241 is from task
    clf = DecisionTreeClassifier(random_state=241)
    # training our classifier on our samples
    clf.fit(sample, data['Survived'])
    # get all feature importances
    importances = clf.feature_importances_
    print 'Feature importances: ', importances
    # getting indexes of two important features
    top_2_feature_indexes = sorted(
        range(len(importances)), key=lambda i: importances[i], reverse=True)[:2]
    print 'Indexes of two most important features: ', top_2_feature_indexes
    # getting names of two most important features
    top_2_feature_names = str.format('{0} {1}', features[top_2_feature_indexes[0]],
                                     features[top_2_feature_indexes[1]])
    print 'Names of two most important features: ', top_2_feature_names
    # path of file with assignment
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_2.txt')
    # opening assignment file
    with open(file_path, 'w') as opened_file:
        opened_file.write(top_2_feature_names)


if __name__ == '__main__':
    main()
