from sympy import *
import numpy as np
from numpy.linalg import eig
from van_der_mee_theorem import van_der_mee_theorem
from utils.request_matrix import request_matrix


def k_primitive(m):
    # First we need to know if the matrix is Mueller.
    qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig = van_der_mee_theorem(m)
    if minimum_qm >= 0 and minimum_proy1_m >= 0:
        print(f"The minimum of the functions qM and proy1(M) of the matrix M are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"Therefore, the matrix M is a Mueller matrix.")
    else:
        print(f"The minimum of the functions qM and proy1(M) of the matrix M are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"The matrix M is not a Mueller matrix, therefore is not K-primitive.")
        return

    m_0 = np.array(m).astype(np.float64)
    # "eigenvalues" is the list of eigenvalues of the matrix M.
    # "eigenvectors" is a matrix that contains the eigenvectors in the columns.
    # The list of eigenvalues and the matrix of eigenvectors are related by the index, that is, the element i of the
    # list of eigenvalues corresponds the column i of the matrix of eigenvectors.
    eigenvalues, eigenvectors = eig(m_0)

    # We have to calculate the spectral radius of M.

    # When the eigenvalues are approximated numerically, the numerical approximations generate small imaginary parts
    # in the real eigenvalues. Then we filter that error into the following list, using the fact that in the case of
    # polynomials with real coefficients, if a complex number is a root, so is its conjugate.
    eigenvalues_without_error = []
    for i in eigenvalues:
        conj = i.conjugate()
        z = conj in eigenvalues
        if simplify(i).is_real == True:
            eigenvalues_without_error.append(np.round(i, 12))
        elif simplify(i).is_real == False and z == False:
            eigenvalues_without_error.append(np.round(i.real, 12))
        else:
            eigenvalues_without_error.append(i)
    print(f"The eigenvalues of the matrix M are: {eigenvalues_without_error}.")
    print(f"The eigenvectors (ordered in the columns respectively) of the matrix M are:\n{eigenvectors}")

    # norm_eigenvalues is the list of the norms of the eigenvalues.
    norm_eigenvalues = (np.absolute(eigenvalues_without_error)).tolist()
    print(f"The norms of the eigenvalues of M are: {norm_eigenvalues}.")

    # The spectral radius ro_m is the maximum in the list norm_eigenvalue.
    rho_m = max(norm_eigenvalues)

    # Now we ask if ro_m is in the list of eigenvalues_without_error.
    if rho_m in eigenvalues_without_error:
        print(f"The spectral radius, {rho_m}, is an eigenvalue of M.")
        ind_rho_m = eigenvalues_without_error.index(rho_m)
    else:
        print(f"The spectral radius, {rho_m}, is not an eigenvalue of M.")
        print(f"Therefore, the matrix M is NOT K-primitive.")
        return

    # We need to know if the spectral radius is a simple eigenvalue. That is, we need to know if the algebraic
    # multiplicity of the spectral radius is 1.
    mult_alg_rho_m = eigenvalues_without_error.count(eigenvalues_without_error[ind_rho_m])
    if mult_alg_rho_m > 1:
        print(f"The spectral radius, {rho_m}, has algebraic multiplicity {mult_alg_rho_m}. "
              f"Then, is not a simple eigenvalue.")
        print(f"Therefore the matrix is NOT K-primitive.")
        return
    else:
        print(f"The spectral radius, {rho_m}, is a simple eigenvalue.")

    # We look for the eigenvalues with the same norm as the spectral radius and
    # then check if they are simple eigenvalues.

    index_norm_rho = []
    for y in range(len(norm_eigenvalues)):
        if norm_eigenvalues[y] == rho_m:
            index_norm_rho.append(y)
        else:
            continue

    for element in index_norm_rho:
        if eigenvalues_without_error.count(eigenvalues_without_error[element]) != 1:
            print(f"There is another eigenvalue, {eigenvalues_without_error[element]}, with norm {rho_m} "
                  f"and algebraic multiplicity {eigenvalues_without_error.count(eigenvalues[element])}.")
            print(f"Then, is not a simple eigenvalue. Therefore, the matrix M is NOT K-primitive.")
            return
        else:
            continue
    print(f"All eigenvalues with norm {rho_m} are simples.")

    # Now check if the only eigenvector v (or -v) associated with the spectral radius is in the interior of the
    # light cone.

    U = eigenvectors.transpose()[ind_rho_m].real
    print(f"The eigenvector associated to the spectral radius is:\n{(np.array(U)[np.newaxis]).T}")
    if U[0] < 0:
        W = (-1) * U
        if ((W[3]) ** 2) + ((W[2]) ** 2) + ((W[1]) ** 2) < ((W[0]) ** 2):
            print(f"The eigenvector corresponding to the spectral radius is in the interior of the light cone.")
        else:
            print(f"The eigenvector corresponding to the spectral radius is NOT in the interior of the light cone, "
                  f"therefore M is NOT K-primitive. ")
            return
    else:
        if ((U[3]) ** 2) + ((U[2]) ** 2) + ((U[1]) ** 2) < ((U[0]) ** 2):
            print(f"The eigenvector corresponding to the spectral radius is in the interior of the light light cone.")
        else:
            print(f"The eigenvector corresponding to the spectral radius is NOT in the interior of the light cone, "
                  f"therefore M is NOT K-primitive. ")
            return

    # Now we calculate if the eigenvectors corresponding eigenvalues with norm different to the spectral radius
    # are in the light cone. If there is one, then the matrix is not K-irreducible.
    for s in range(len(eigenvalues_without_error)):
        if simplify(eigenvalues_without_error[s]).is_real == True and eigenvalues_without_error[s] != rho_m:
            U = eigenvectors.transpose()[s].real
            if U[0] < 0:
                W = (-1) * U
                if ((W[3]) ** 2) + ((W[2]) ** 2) + ((W[1]) ** 2) <= ((W[0]) ** 2):
                    print(f"The eigenvector\n{np.array(W)[np.newaxis].T} \n"
                          f"does not correspond to the spectral radius and is in the light cone. "
                          f"Therefore M is NOT K-primitive.")
                    return
                else:
                    continue
            else:
                W = U
                if ((W[3]) ** 2) + ((W[2]) ** 2) + ((W[1]) ** 2) <= ((W[0]) ** 2):
                    print(f"There is an eigenvector,\n{np.array(W)[np.newaxis].T} \n"
                          f"not corresponding the spectral radius that is in the light cone. "
                          f"Therefore M is NOT K-primitive.")
                    return
                else:
                    continue

        else:
            continue
    print(f"All eigenvectors that do not correspond to the spectral radius are not in the light cone. "
          f"Therefore M is K-irreducible. ")

    # For a matrix to be K-primitive, it is necessary that there are no other eigenvalues that have norm equal to
    # the spectral radius.
    eigenvalues_norm_rho = []
    for i in index_norm_rho:
        eigenvalues_norm_rho.append(eigenvalues_without_error[i])

    if len(index_norm_rho) > 1:
        print(f"The eigenvalues with norm {rho_m} are: {eigenvalues_norm_rho}.")
        print(f"Therefore, the matrix M is not K-primitive")
    else:
        print(f"There are no other eigenvalues with norm equal to the spectral radius. Therefore M is K-primitive.")



