import numpy as np



# python from what I remember lets you overload pretty much everything.
# including +, -, and ==
# differs from 
def test_multiply():
    arr1 = np.array([[1, 2],
                    [3, 4]])
    arr2 = np.array([[5, 6],
                    [7, 8]])
    arr_result = np.multiply(arr1, arr2)

    expected_result = np.array([[5, 12],
                                [21, 32]])


    # assert arr_result.all(expected_result)
    # assert arr_result.any(expected_result)
    # assert arr_result
    # assert arr_result == expected_result
    #https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
    assert np.array_equal(arr_result, expected_result)

def test_matrix_multiply():
    arr1 = np.array([[1, 2],
                    [3, 4]])
    arr2 = np.array([[5, 6],
                    [7, 8]])
    
    expected_result = np.array([[19, 22],
                                [43, 50]])
    #https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
    assert np.array_equal(np.matmul(arr1,arr2),np.dot(arr1,arr2))
    assert np.array_equal(np.matmul(arr1,arr2),np.array(expected_result))

    
def test_matrix_transpose():
    arr1 = np.array([[1, 2],
                    [3, 4]])
    # transpose of a matrix is obtained by interchanging its rows and columns.
    arr2 = arr1.transpose()

    assert np.array_equal(arr2,arr1.transpose())
    assert np.array_equal(arr2.transpose(),arr1)

    #original array is not modified
    assert np.array_equal(arr1,np.array([[1, 2],[3, 4]]))


def test_matrix_addition():
    arr1 = np.array([[1, 2],
                    [3, 4]])
    arr3 = arr1 + arr1

    print(arr3)

    assert np.array_equal(arr3,np.array([[2, 4],
                                        [6, 8]])
                                        )




#https://www.youtube.com/watch?v=JnTa9XtvmfI

#https://www.math.uni-bielefeld.de/~grigor/kurosh-higher-algebra.pdf

#https://www.reddit.com/r/learnmath/comments/suxqvc/looking_for_linear_algebra_practice_problems_and/

#https://solverer.com/library/stephen_friedberg/linear_algebra

#https://www.math.ucdavis.edu/~linear/linear-guest.pdf

#https://en.wikipedia.org/wiki/Dot_product



#https://www.salfordphysics.com/gsmcdonald/H-Tutorials/Scalar-product-of-vectors.pdf


#https://stackoverflow.com/questions/5919530/what-is-the-pythonic-way-to-calculate-dot-product

#The name "dot product" is derived from the dot operator " ⋅ " that is often used to designate this operation;[1] the alternative name "scalar product" emphasizes that the result is a scalar, rather than a vector (as with the vector product in three-dimensional space).

#linear algebra
#https://numpy.org/doc/2.1/reference/generated/numpy.dot.html#


def test_dot_product():

    vector1 = np.array([1,2])
    vector2 = np.array([5,6])
    matrix3 = np.array([[5],[6]])

    print(vector1.dot(vector2))
    print(np.dot(vector1, vector2))
    print(np.matmul(vector1, vector2))


    print(np.matmul(vector1, matrix3))

    #print(vector1.dot(vector3))






#https://en.wikipedia.org/wiki/Dot_product
# test dot product
# def test_dot_product():
#     arr1 = np.array([1, 2])
#     arr2 = np.array([3, 4])
#     # dot product of two vectors
#     result = np.dot(arr1, arr2)
#     expected_result = 1 * 3 + 2 * 4 
#     assert result == expected_result








# arr1 = np.array([[1, 2],
#                  [3, 4]])
# arr2 = np.array([[5, 6],
#                  [7, 8]])

# # 2 x 3 matrix
# # arr3 = np.dot(arr1, arr2)

# arr1 = np.array([[1, 2],
#                  [3, 4]])
# arr2 = np.array([[5, 6],
#                  [7, 8]])
# arr_result = np.multiply(arr1, arr2)

# print(arr_result)

# print(np.matmul(arr1, arr2))

# print(np.matmul(arr2, arr1))

# print(np.dot(arr1, arr2))

# print(np.dot(arr2, arr1))


# multiply two matrices


# https://www.digitalocean.com/community/tutorials/numpy-matrix-multiplication


#Vectors are represented as matrices. But a matrix is just a rectangular array of numbers and nothing else.

#https://math.stackexchange.com/questions/2354047/dot-product-vs-matrix-multiplication-is-the-later-a-special-case-of-the-first


#https://math.stackexchange.com/questions/271927/why-historically-do-we-multiply-matrices-as-we-do

