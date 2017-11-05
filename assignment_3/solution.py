"""Solution for third assignment (k-neighbours classifier)"""

import os
import pandas


def main():
    """Main function """
    # file path with data
    wine_path = os.path.join(os.path.dirname(__file__), 'wine.data')
    # loading this file
    data = pandas.read_csv(wine_path)
    classes = data.columns
    print classes


if __name__ == '__main__':
    main()
