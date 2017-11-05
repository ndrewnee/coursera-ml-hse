"""Solution of 4th assignment (Select P-metric)"""

import os
import numpy
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import scale
from sklearn.datasets import load_boston


def write_to_file(file_name, data):
    """Helper to write information to file"""
    # path of file with first assignment
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    # opening assignment file
    with open(file_path, 'w') as opened_file:
        opened_file.write(data)


def main():
    """Main function of solution"""
    boston = load_boston()
    # getting class
    classes = boston.target
    # scaling attributes
    attributes = scale(X=boston.data)
    # creating K-Folds cross-validator
    k_fold = KFold(n_splits=5, shuffle=True, random_state=42)
    # splitting attributes by cross-validator
    k_fold.get_n_splits(attributes)
    # scores with parameter P
    p_scores = []
    # generating 200 steps from 1 to 10
    parameters = numpy.linspace(1, 10, num=200)
    for parameter in parameters:
        regressor = KNeighborsRegressor(n_neighbors=5, weights='distance')
        scores = cross_val_score(estimator=regressor, X=attributes, y=classes,
                                 cv=k_fold, scoring='neg_mean_squared_error')
        # calculating mean of scores
        mean_score = sum(scores) / max(len(scores), 1)
        # adding mean score with P to list of scores
        p_scores.append({
            'parameter': parameter,
            'score': mean_score,
        })
    # find max score from list of scores
    max_score = max(p_scores, key=lambda x: x['score'])
    print 'Parameter(p): {0}, Max Score: {1}'.format(max_score['parameter'], max_score['score'])
    # write parameter P with max score to file
    write_to_file('assignment_4.txt', str(round(max_score['parameter'], 1)))


if __name__ == '__main__':
    main()
