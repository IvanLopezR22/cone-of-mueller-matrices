from sympy import *
from sympy import Abs
import numpy as np
from numpy.linalg import eig
from van_der_mee_theorem import van_der_mee_theorem


def k_irreducible(m):
    # First we need to know if the matrix is Mueller.
    qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig = van_der_mee_theorem(m)
    if minimum_qm >= 0 and minimum_proy1_m >= 0:
        print(f"The minimum of the functions qM and proy1(M) of the matrix M are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"Therefore, the matrix M is a Mueller matrix.")
    else:
        print(f"The minimum of the functions qM and proy1(M) of the matrix M are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"The matrix M is not a Mueller matrix, therefore is not K-irreducible.")
        return

    # eigenvalues is the list of Eigenvalues of M and eigenvectors is a matrix of Eigenvectors (in the columns) of M.
    m_1 = np.array(m).astype(np.float64)
    eigenvalues, eigenvectors = eig(m_1)
    # For convenience, we use the transpose of the matrix eigenvectors to have the eigenvectors in the rows. Then the
    # associated eigenvector to the first eigenvalue is the first row and so on.
    eigenvectors_transpose = eigenvectors.transpose()

    # We have to calculate the spectral radius of M.
    # When the eigenvalues are approximated numerically, the numerical approximations generate small imaginary parts
    # in the real eigenvalues. Then we filter that error into the following list, using the fact that in the case of
    # polynomials with real coefficients, If a complex number is a root, then its conjugate is too.
    eigenvalues_without_error = []
    for i in eigenvalues:
        conj = i.conjugate()
        z = conj in eigenvalues
        if simplify(i).is_real == True:
            eigenvalues_without_error.append(i)
        elif simplify(i).is_real == False and z == False:
            eigenvalues_without_error.append(re(i))
        else:
            eigenvalues_without_error.append(i)
    print(f"The eigenvalues of the matrix M are: {eigenvalues_without_error}.")

    # norm_eigenvalues is the list of eigenvalue norms.
    norm_eigenvalues = []
    for i in range(len(eigenvalues_without_error)):
        norm_eigenvalues.append(Abs(eigenvalues_without_error[i]))
    print(f"The norms of the eigenvalues of M are: {norm_eigenvalues}.")
    print(f"The eigenvectors of the matrix M (ordered in the rows) are:")
    print(eigenvectors_transpose)

    # The spectral radius ro_m is the maximum in the list norm_eigenvalue.
    ro_m = max(norm_eigenvalues)
    print(f"The spectral radius is {ro_m}.")

    # index_spectral and index_non_spectral are the list of the index in the list of eigenvalues, corresponding to the
    # spectral radius and values different to the spectral radius respectively.
    index_spectral = []
    for y in range(len(norm_eigenvalues)):
        if eigenvalues_without_error[y] == ro_m:
            index_spectral.append(y)
        else:
            continue

    index_non_spectral = []
    for z in range(len(norm_eigenvalues)):
        if eigenvalues_without_error[z] != ro_m:
            index_non_spectral.append(z)
        else:
            continue

    # Now, for the indices corresponding the spectral radius in the list of eigenvalues we find the associated
    # eigenvectors and calculate if they are in the light cone. If one of them is not in the light cone, then the matrix
    # is not K-irreducible.
    for s in index_spectral:
        V = eigenvectors_transpose[s]
        U = np.array([re(V[0]), re(V[1]), re(V[2]), re(V[3])])
        if U[0] < 0:
            W = U * (-1)
        else:
            W = U
        if ((W[3]) ** 2) + ((W[2]) ** 2) + ((W[1]) ** 2) < ((W[0]) ** 2):
            continue
        else:
            print(f"The eigenvector \n{np.array(W).astype(np.float64).transpose()}\nassociated to the "
                  f"spectral radius, is not in the light cone. Therefore, the matrix M is not K-irreducible.")
            return

    print("All eigenvectors associated with the spectral radius are in the light cone.")

    # For the indices corresponding the values different from spectral radius in the list of eigenvalues we find
    # the associated eigenvectors and calculate if they are in the light cone. If one of them is in the light cone,
    # then the matrix is not K-irreducible.
    for s in index_non_spectral:
        if simplify(eigenvalues_without_error[s]).is_real == True:
            V = eigenvectors_transpose[s]
            U = np.array([re(V[0]), re(V[1]), re(V[2]), re(V[3])])
            if U[0] < 0:
                W = U * (-1)
            else:
                W = U
            if ((W[3]) ** 2) + ((W[2]) ** 2) + ((W[1]) ** 2) > ((W[0]) ** 2):
                continue
            else:
                print(f"The eigenvector {np.array(W).astype(np.float64).transpose()} associated to the eigenvalue "
                      f"{eigenvalues[s]} in the light cone. Therefore, the matrix M is not K-irreducible.")
                return
        else:
            continue
    print(f"For all eigenvalues other than the spectral radius, the corresponding eigenvectors are not "
          f"in the light cone.")

    print("Therefore, the matrix is K-irreducible.")
