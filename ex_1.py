import numpy

# Task 1.
# Generating random matrix.
MATRIX = numpy.random.normal(loc=1, scale=10, size=(1000, 50))
print 'Matrix:\n', MATRIX

# Task 2.
# Compute the arithmetic mean of matrix along it's column.
MEAN = numpy.mean(MATRIX, axis=0)
# Compute standart deviation of matrix along it's column.
STANDART_DEVIATION = numpy.std(MATRIX, axis=0)
# Normalizing matrix.
NORMALIZED_MATRIX = ((MATRIX - MEAN) / STANDART_DEVIATION)
print 'Normalized Matrix:\n', NORMALIZED_MATRIX

# Task 3.
# Compute sum of elements in each row of matrix.
SUM_OF_ELEMS_IN_ROW = numpy.sum(NORMALIZED_MATRIX, axis=1)
# For each element in matrix will be applied this condition.
# So result will be matrix with booleans.
# in cells will be True if condition is right or False if it is not.
# numpy.nonzero gets indexes of elements where value is True.
ROWS_WHERE_SUM_GREATHER_THAN_10 = numpy.nonzero(SUM_OF_ELEMS_IN_ROW > 10)
print 'Rows where sum of elements is greather than 10:\n', ROWS_WHERE_SUM_GREATHER_THAN_10

# Task 4.
# Generating two identity matrixes
IDENTITY_MATRIX_A = numpy.eye(3)
IDENTITY_MATRIX_B = numpy.eye(3)
print 'Identity Matrix A:\n', IDENTITY_MATRIX_A
print 'Identity Matrix B:\n', IDENTITY_MATRIX_B
# Stacking vertically two identity matrixes
STACKED_MATRIX = numpy.vstack((IDENTITY_MATRIX_A, IDENTITY_MATRIX_B))
print 'Vertically stacked Matrix:\n', STACKED_MATRIX
