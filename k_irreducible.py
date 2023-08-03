from sympy import *
from sympy import Abs
import numpy as np


def k_irreducible(m):
    # eigen_m is a list with triples that have the form (eigenvalue, algebraic multiplicity, eigenvectors).
    # The eigenvalues, algebraic multiplicity and eigenvectors are calculated exactly.
    eigen_m = m.eigenvects()

    # Here we separate eigenvalues, algebraic multiplicity and eigenvectors into different lists,
    # related by the indices.
    eigenvalues = []
    for element in eigen_m:
        eigenvalues.append((element[0]))

    mult_alg = []
    for element in eigen_m:
        mult_alg.append(element[1])

    eigenvectors = []
    for element in eigen_m:
        eigenvectors.append(element[2:])

    # We have to calculate the spectral radius of M.
    # Now, let's approximate the exact eigenvalues numerically.
    num_eigenvalues = []
    for i in range(len(eigenvalues)):
        num_eigenvalues.append(N(eigenvalues[i], 10))

    # When the eigenvalues are approximated numerically, the numerical approximations generate small imaginary parts
    # in the real eigenvalues. Then we filter that error into the following list, using the fact that in the case of
    # polynomials with real coefficients, if a complex number is a root, so is its conjugate.
    eigenvalues_without_error = []
    for i in num_eigenvalues:
        conj = i.conjugate()
        z = conj in num_eigenvalues
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

    # The spectral radius ro_m is the maximum in the list norm_eigenvalue.
    ro_m = max(norm_eigenvalues)

    # Now we ask if ro_m is in the list of eigenvalues_without_error.
    if ro_m in eigenvalues_without_error:
        print(f"The spectral radius, {ro_m}, is an eigenvalue of M.")
        ind_ro_m = eigenvalues_without_error.index(ro_m)
    else:
        print(f"The spectral radius, {ro_m}, is not an eigenvalue of M.")
        print(f"Therefore, the matrix M is NOT K-irreducible.")
        return

    # We need to know if the spectral radius is a simple eigenvalue. That is, we need to know if the algebraic
    # multiplicity of the spectral radius is 1.
    mul_alg_ro_m = mult_alg[ind_ro_m]
    if mul_alg_ro_m != 1:
        print(f"The spectral radius, {ro_m}, has algebraic multiplicity {mul_alg_ro_m}. "
              f"Then, is not a simple eigenvalue.")
        print(f"Therefore the matrix is NOT K-irreducible.")
        return
    else:
        print(f"The spectral radius, {ro_m}, is a simple eigenvalue.")

    # We look for another eigenvalue with the same norm as the spectral radius and
    # then check if they are simple eigenvalues.

    index_1 = []
    for y in range(len(norm_eigenvalues)):
        if norm_eigenvalues[y] == ro_m:
            index_1.append(y)
        else:
            continue

    for element in index_1:
        if mult_alg[element] != 1:
            print(f"There is another eigenvalue, {eigenvalues_without_error[element]}, with norm {ro_m}")
            print(f"and algebraic multiplicity {mult_alg[element]}. Then, is not a simple eigenvalue.")
            print("Therefore, the matrix is NOT K-irreducible.")
            return
        else:
            continue
    print(f"All eigenvalues with norm {ro_m} are simples.")

    # Remains to check if the only eigenvector v (or -v) associated with the spectral radius is in the light cone.
    V = eigenvectors[ind_ro_m][0][0]
    U = Matrix([[re(N((V[0, 0]), 10))], [re(N((V[1, 0]), 10))], [re(N((V[2, 0]), 10))], [re(N((V[3, 0]), 10))]])
    print('The eigenvector associated to the spectral radius is:\n', np.array(U).astype(np.float64))
    if U[0, 0] < 0:
        W = (-1) * U
        if ((W[3, 0]) ** 2) + ((W[2, 0]) ** 2) + ((W[1, 0]) ** 2) <= ((W[0, 0]) ** 2):
            print(f"The eigenvector corresponding to the spectral radius is in the light cone, "
                  f"therefore M is K-irreducible.")
        else:
            print(f"The eigenvector corresponding to the spectral radius is NOT in the light cone, "
                  f"therefore M is NOT K-irreducible. ")
    else:
        if ((U[3, 0]) ** 2) + ((U[2, 0]) ** 2) + ((U[1, 0]) ** 2) <= ((U[0, 0]) ** 2):
            print(f"The eigenvector corresponding to the spectral radius is in the light light cone, "
                  f"therefore M is K-irreducible.")
        else:
            print(f"The eigenvector corresponding to the spectral radius is NOT in the light cone, "
                  f"therefore M is NOT K-irreducible. ")
