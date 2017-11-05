"""Solution for third assignment (k-neighbours classifier)"""

import os
import pandas
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale


def get_sorted_k_scores(k_fold, classes, attributes):
    """Does K-neighbours classification.
    Returns sorted by score list of scores and K"""
    # generation range of K from 1 to 50
    k_scores = []
    k_range = xrange(1, 51)
    for k in k_range:
        # creating new classifier with provided K
        classifier = KNeighborsClassifier(n_neighbors=k)
        # computing score of each classifier
        scores = cross_val_score(estimator=classifier, X=attributes, y=classes,
                                 cv=k_fold, scoring='accuracy')
        # calculating mean of scores
        mean_score = sum(scores) / max(len(scores), 1)
        # adding mean score with k to list of scores
        k_scores.append({
            'k': k,
            'score': mean_score,
        })

    # sorting list of scores by score, descending
    k_scores.sort(key=lambda x: x['score'], reverse=True)
    return k_scores


def write_to_file(file_name, data):
    """Helper to write information to file"""
    # path of file with first assignment
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    # opening assignment file
    with open(file_path, 'w') as opened_file:
        opened_file.write(data)


def main():
    """Main function of solution"""
    # file path with data
    wine_path = os.path.join(os.path.dirname(__file__), 'wine.data')
    # loading this file
    data = pandas.read_csv(wine_path, header=None)
    # importing class from dataframe
    classes = data[0]
    # importing attributes from dataframe
    attributes = data.loc[:, 1:]
    # creating K-Folds cross-validator
    k_fold = KFold(n_splits=5, shuffle=True, random_state=42)
    # splitting attributes by cross-validator
    k_fold.get_n_splits(attributes)
    # find accuracy of scores
    k_scores = get_sorted_k_scores(k_fold, classes, attributes)
    # getting value with max score
    top_score = k_scores[0]
    print 'Normal. K: {0}, Score: {1}'.format(top_score['k'], top_score['score'])
    # writing answer for 1st question to file)
    write_to_file('assignment_3_1.txt', str(top_score['k']))
    # writing answer for 2nd question to file
    write_to_file('assignment_3_2.txt', str(top_score['score']))
    # scaling attributes
    scaled_attributes = scale(X=attributes)
    # find accuracy of scaled attributes
    scaled_k_scores = get_sorted_k_scores(
        k_fold, classes, scaled_attributes)
    # getting value with max score
    scaled_top_score = scaled_k_scores[0]
    print 'Scaled. K: {0}, Score: {1}'.format(scaled_top_score['k'], scaled_top_score['score'])
    # writing answer for 3rd question to file)
    write_to_file('assignment_3_3.txt', str(scaled_top_score['k']))
    # writing answer for 4rd question to file
    write_to_file('assignment_3_4.txt', str(scaled_top_score['score']))


if __name__ == '__main__':
    main()
