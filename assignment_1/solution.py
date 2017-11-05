"""First assignment in machine learing coursera courses """

from collections import Counter
import os
import pandas


def calc_count_by_sex(data):
    """Finds how many male and female people was on Titanic"""
    grouped_by_sex = data['Sex'].value_counts()
    male = grouped_by_sex['male']
    female = grouped_by_sex['female']
    print 'Male: {0}, Female: {1}'.format(male, female)
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_1_1.txt')
    with open(file_path, 'w') as opened_file:
        opened_file.write(str.format('{0} {1}', male, female))


def calc_survived_in_percents(data):
    """Calculates percent of survived people"""
    grouped_by_survived = data['Survived'].value_counts()
    total = data.shape[0]
    survived = grouped_by_survived[1]
    survived_in_percents = round(100 * survived / float(total), 2)
    print 'Survived (in percents): ', survived_in_percents
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_1_2.txt')
    with open(file_path, 'w') as opened_file:
        opened_file.write(str.format('{0}', survived_in_percents))


def calc_first_class_in_percents(data):
    """Calculates percent of first class people"""
    grouped_by_pclass = data['Pclass'].value_counts()
    first_class = grouped_by_pclass[1]
    total = data.shape[0]
    first_class_in_percents = round(100 * first_class / float(total), 2)
    print 'First class (in percents): ', first_class_in_percents
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_1_3.txt')
    with open(file_path, 'w') as opened_file:
        opened_file.write(str.format('{0}', first_class_in_percents))


def calc_mean_and_median_age(data):
    """Calculates mean and median age of people"""
    mean = round(data['Age'].mean(), 2)
    median = data['Age'].median()
    print 'Mean age: {0}, Median age: {1}'.format(mean, median)
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_1_4.txt')
    with open(file_path, 'w') as opened_file:
        opened_file.write(str.format('{0} {1}', mean, median))


def calc_corr_between_sibsp_parch(data):
    """Calculates Pearson correlation between siblings/spouses and parents/children"""
    pearson_corr = round(data['SibSp'].corr(data['Parch']), 2)
    print 'Pearson correlation between siblings/spouses and parents/children: ', pearson_corr
    file_path = os.path.join(os.path.dirname(__file__), 'assignment_1_5.txt')
    with open(file_path, 'w') as opened_file:
        opened_file.write(str.format('{0}', pearson_corr))


def find_most_popular_female_name(data):
    """Finds most popular female name on the ship"""
    females = data[data['Sex'] == 'female']
    names = (
        females['Name'].str.cat(sep=' ').split()
    )
    result = pandas.DataFrame(Counter(names).most_common(10), columns=[
        'Name', 'Frequency']).set_index('Name')
    print 'Females: \n', result
    # TODO Filter trash, get top and write to file


def main():
    """Main function to calc all assignments and save them to files"""
    titanic_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
    data = pandas.read_csv(titanic_path, index_col='PassengerId')
    calc_count_by_sex(data)
    calc_survived_in_percents(data)
    calc_first_class_in_percents(data)
    calc_mean_and_median_age(data)
    calc_corr_between_sibsp_parch(data)
    find_most_popular_female_name(data)


if __name__ == '__main__':
    main()
