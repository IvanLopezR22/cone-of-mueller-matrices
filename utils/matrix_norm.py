from sympy import *
from sympy import Abs


def norm_of_matrix(main_matrix):
    # To calculate the norm of a matrix M we use a corollary of the Rayleigh-Ritz Theorem. Which assures us that
    # the norm of the matrix M is the square root of the largest eigenvalue of the matrix M^{T}*M.

    mult_transpose_main = main_matrix.T * main_matrix

    # Now we calculate the exact eigenvalues of M^{T}*M, which are non-negative.
    eigenvectors_mtm = mult_transpose_main.eigenvects()
    eigenvalues_mtm = []
    for element in eigenvectors_mtm:
        eigenvalues_mtm.append((element[0]))

    # Finally, we generate a numerical approximation of the exact eigenvalues and then select the largest.
    # We do this because the numerical approximations generate little imaginary parts that we need to filter out.
    norm_eigenvalues_mtm = []
    for i in range(len(eigenvalues_mtm)):
        norm_eigenvalues_mtm.append(Abs(N(sqrt(re(eigenvalues_mtm[i])), 10)))

    s = max(norm_eigenvalues_mtm)
    return s
