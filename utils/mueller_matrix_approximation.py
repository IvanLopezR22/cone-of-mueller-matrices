from sympy import *
from sympy import Abs
from matrix_norm import norm_of_matrix


def mueller_approximation_utils(main_matrix):
    e_1 = Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ident = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    # We find the norm of the matrix M.
    norm_main_matrix = norm_of_matrix(main_matrix)

    eigen_m = main_matrix.eigenvects()

    # Now we calculate the norm of the eigenvalues.
    norm_eigenvalues_m = []
    for i in range(len(eigen_m)):
        norm_eigenvalues_m.append(Abs(N(eigen_m[i][0], 10)))

    # Here we select the largest of the list of norms of eigenvalues.
    p = max(norm_eigenvalues_m)

    # Finally, an approximation of M by an invertible Mueller matrix is given by.
    #f = ((p + (1 / 10)) * ident) + (e_1 + ((1 / (2 * norm_main_matrix)) * main_matrix))
    f = (p*e_1) + ((1 / (2 * norm_main_matrix))*ident) + (e_1 + ((1 / (2 * norm_main_matrix)) * main_matrix))
    return f
