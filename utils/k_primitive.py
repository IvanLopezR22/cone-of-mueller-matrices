from sympy import *
from sympy import Abs
from utils.request_matrix import request_matrix


def know_k_primitive(m):
    # This funtion use the same theory as k_primitive, the difference is that this return True if the introduced matrix
    # is K-primitive and False if not. For more details see the file k_primitive.
    eigen_m = m.eigenvects()

    eigenvalues = []
    for element in eigen_m:
        eigenvalues.append((element[0]))

    mult_alg = []
    for element in eigen_m:
        mult_alg.append(element[1])

    eigenvectors = []
    for element in eigen_m:
        eigenvectors.append(element[2:])

    num_eigenvalues = []
    for i in range(len(eigenvalues)):
        num_eigenvalues.append(N(eigenvalues[i], 10))

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

    norm_eigenvalues = []
    for i in range(len(eigenvalues_without_error)):
        norm_eigenvalues.append(Abs(eigenvalues_without_error[i]))

    ro_m = max(norm_eigenvalues)

    if ro_m in eigenvalues_without_error:
        ind_ro_m = eigenvalues_without_error.index(ro_m)
    else:
        ask_k_primitive= False
        return ask_k_primitive

    mul_alg_ro_m = mult_alg[ind_ro_m]
    if mul_alg_ro_m != 1:
        ask_k_primitive = False
        return ask_k_primitive

    index_1 = []
    for y in range(len(norm_eigenvalues)):
        if norm_eigenvalues[y] == ro_m:
            index_1.append(y)
        else:
            continue

    if len(index_1) > 1:
        ask_k_primitive = False
        return ask_k_primitive

    V = eigenvectors[ind_ro_m][0][0]
    U = Matrix([[re(N((V[0, 0]), 10))], [re(N((V[1, 0]), 10))], [re(N((V[2, 0]), 10))], [re(N((V[3, 0]), 10))]])

    if U[0, 0] < 0:
        W = (-1) * U
        if ((W[3, 0]) ** 2) + ((W[2, 0]) ** 2) + ((W[1, 0]) ** 2) <= ((W[0, 0]) ** 2):
            ask_k_primitive = True
            return ask_k_primitive
        else:
            ask_k_primitive = False
            return ask_k_primitive
    else:
        if ((U[3, 0]) ** 2) + ((U[2, 0]) ** 2) + ((U[1, 0]) ** 2) <= ((U[0, 0]) ** 2):
            ask_k_primitive = True
            return ask_k_primitive
        else:
            ask_k_primitive = False
            return ask_k_primitive

