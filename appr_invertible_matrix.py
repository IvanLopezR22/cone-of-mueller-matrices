import numpy as np
from sympy import *

np.set_printoptions(precision=10, suppress=True, linewidth=2000)


def make_invertible(name, main_matrix):
    # This function is defined for practical reasons.
    # In the approximations we need to force some matrices to be invertible. The way we do this is
    # by finding a positive epsilon value, such that it is not an eigenvalue and is less than 1/100.
    # Then we add epsilon*Id to our matrix, where Id is the identity matrix in M_{4}(R).
    # ident is the identity matrix of M_{4}(R).
    ident = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    # If M is a non-invertible matrix, then we call M(inv)=epsilon*Id+M.

    # Case 1: The matrix M is invertible, then we do nothing to M.
    det_main_matrix = round(main_matrix.det(), 12)
    if det_main_matrix != 0:
        invertible_main_matrix = main_matrix
        print(f"The determinant of the matrix {name} is {round(main_matrix.det(), 12)}. Therefore {name} "
              f"is an invertible matrix. ")

    # Case 2: The matrix M is not invertible. Then we calculate the epsilon mentioned above.
    else:
        # eigen_m is the list of eigenvalues, algebraic multiplicity and eigenvectors of the matrix M.
        eigen_m = main_matrix.eigenvects()
        eigenvalues = []
        for element in eigen_m:
            eigenvalues.append((element[0]))

        # Now we calculate the norm of the eigenvalues.
        norm_eigenvalues_m = []
        for i in range(len(eigen_m)):
            norm_eigenvalues_m.append(round(Abs(N(eigen_m[i][0], 10)), 15))

        # Here we filter the zero eigenvalues.
        norms_no_zero = [x for x in norm_eigenvalues_m if x != 0]
        if not norms_no_zero:
            norms_no_zero.append(2)
        # Using the list of norms of eigenvalues we find our epsilon.
        eps = min([1 / 100, (1 / 2) * min(norms_no_zero)])
        # Finally we add epsilon*ident to our input matrix.
        invertible_main_matrix = (eps * ident) + main_matrix
        print(f"The determinant of the matrix {name} is {round(main_matrix.det(), 12)}. "
              f"Therefore {name} is not an invertible matrix. ")

    return invertible_main_matrix, det_main_matrix
