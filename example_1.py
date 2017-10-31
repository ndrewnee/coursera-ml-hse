"""First example with 4 tasks in machine learning course"""

import numpy


def main():
    """Main function with tasks for first example"""
    # Task 1.
    # Generating random matrix.
    matrix = numpy.random.normal(loc=1, scale=10, size=(1000, 50))
    print 'Matrix:\n', matrix

    # Task 2.
    # Compute the arithmetic mean of matrix along it's column.
    mean = numpy.mean(matrix, axis=0)
    # Compute standart deviation of matrix along it's column.
    standart_deviation = numpy.std(matrix, axis=0)
    # Normalizing matrix.
    normalized_matrix = ((matrix - mean) / standart_deviation)
    print 'Normalized Matrix:\n', normalized_matrix

    # Task 3.
    # Compute sum of elements in each row of matrix.
    sum_of_elems_in_row = numpy.sum(normalized_matrix, axis=1)
    # For each element in matrix will be applied this condition.
    # So result will be matrix with booleans.
    # in cells will be True if condition is right or False if it is not.
    # numpy.nonzero gets indexes of elements where value is True.
    rows_where_sum_greather_than_10 = numpy.nonzero(sum_of_elems_in_row > 10)
    print 'Rows where sum of elements is greather than 10:\n', rows_where_sum_greather_than_10

    # Task 4.
    # Generating two identity matrixes
    identity_matrix_a = numpy.eye(3)
    identity_matrix_b = numpy.eye(3)
    print 'Identity Matrix A:\n', identity_matrix_a
    print 'Identity Matrix B:\n', identity_matrix_b
    # Stacking vertically two identity matrixes
    stacked_matrix = numpy.vstack((identity_matrix_a, identity_matrix_b))
    print 'Vertically stacked Matrix:\n', stacked_matrix


if __name__ == '__main__':
    main()
