# Feyza Özen 150190014
import numpy

def get_normal(vector):
    vector_n = vector / vector.max()
    return vector_n

def get_lambda(vector):
    lmd = abs(vector).max()
    return lmd

def iteration(n,eigenvector,matrix,vector_num):
    for i in range(n):
        print("Iteration", i + 1)
        eigenvector = numpy.dot(matrix, eigenvector)
        lambda_x = get_lambda(eigenvector)
        eigenvector = get_normal(eigenvector)
        print("Eigenvalue",vector_num, ":", lambda_x)
        print("Eigenvector",vector_num, ":", eigenvector, "\n")



mtx = numpy.array([[-2, 1, 4],
                   [1,1,1],
                   [4,1,-2]])


# V0 = [1,2,-1]T
eigen_vector1 = numpy.array([1, 2, -1])
iteration(5,eigen_vector1,mtx,1)

print("\n")

# V0 = [1,2,1]T
eigen_vector2 = numpy.array([1, 2, 1])
iteration(5,eigen_vector2,mtx,2)


