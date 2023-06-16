from sympy import *
import sympy as sym
import numpy as np
from numpy.linalg import eig
from utils.ask_for_matrix import ask_for_matrix_interface
from mueller_matrix_aproximation import mueller_aproximation
from utils.qm_graphic import qm_graphic
import matplotlib.pyplot as plt

E_1 = Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
Id = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

#TODO: Solamente aproximar la aw en caso que no sea invertible
def compain_method(M):
    print("Para esta funcion son requeridas 2 matrices más, por favor ingrese los valores a continuación.")
    aw_1 = ask_for_matrix_interface("aw")
    if aw_1.det() != 0:
        aw=aw_1
    else:
        aw=mueller_aproximation_util(aw_1)


    amw = ask_for_matrix_interface("amw")

    #Generate the canonical base of the M_{4}(R) (4x4 matrices on real numbers)
    canonical_base = []
    for i in range(4):
        for j in range(4):
            def f(s, t):
                if s == i and t == j:
                    return 1
                else:
                    return 0

            K = Matrix(4, 4, f)
            canonical_base.append(K)

    aw_inv = aw.inv()
    # we calculate the image of the canonical base under the function H

    image_base = []
    for element in canonical_base:
        W = M * (element) - (element * (aw_inv) * amw)
        image_base.append(W)

    # we use the image of the canonical base to construct H in matricial form
    # the image of e_{i} is the the column i of H
    H_matrix_colums = []
    for x in range(4):
        for y in range(4):
            row = []
            for element in image_base:
                row.append(element[x, y])
            H_matrix_colums.append(row)

    # Matriz_H is the matrixcial form of H on canonical base
    Matriz_H = Matrix(H_matrix_colums)
    Matriz_H_np = np.array(Matriz_H).astype(np.float64)
    print(Matriz_H_np)
    null_space_Mat_H = Matriz_H.nullspace()

    if null_space_Mat_H != []:
        j = 0
        while j <= len(null_space_Mat_H) - 1 and Matrix(np.array(null_space_Mat_H[j].transpose()).astype(np.float64).reshape((4, 4))).det() == 0:
            j += 1
        else:
            if j == len(null_space_Mat_H):
                A = Matrix(np.array(null_space_Mat_H[0].transpose()).astype(
                    np.float64).reshape((4, 4)))
            else:
                A = Matrix(np.array(null_space_Mat_H[j].transpose()).astype(
                    np.float64).reshape((4, 4)))

        print('La matriz A=', A)
        W = mueller_aproximation(A)
        print("An aproximation by an invertibe Mueller matrix of the solution is.")
        print(W)

    else:
        print('La matriz H tiene espacio nulo  trivial')
        eigenvals_H, eigenvects_H = eig(Matriz_H_np)
        eigenvects_H_transpose = eigenvects_H.transpose()
        # We separete the eigenvalues of H in two list, one of real eigenvalues and another with complex eigenvalues
        real_eigenval = []
        complex_eigenval = []
        for i in eigenvals_H:
            if simplify(i).is_real == True:
                real_eigenval.append(Abs(i))
            else:
                i_conj = i.conjugate()
                i_z = i_conj in eigenvals_H
                if i_z == False:
                    real_eigenval.append(Abs(i))
                else:
                    complex_eigenval.append(i)
        # Here we have the case in which all eigenvalues are not real
        if real_eigenval == []:
            # Eigenvalues and eigenvectors of H^{T}H calculated with a numpy matrix
            HT_H = np.matmul(Matriz_H_np.transpose(), Matriz_H_np)
            eigenvals_HT_H, eigenvects_HT_H = eig(HT_H)
            print(eigenvals_HT_H)
            eigenvects_HT_H_transpose = eigenvects_HT_H.transpose()
            print(HT_H)
            # Absolute value of the real eigenvectors (symetric Matrix)
            abs_eigenvals_HT_H = []
            for i in eigenvals_HT_H:
                abs_eigenvals_HT_H.append(Abs(i))
            print(abs_eigenvals_HT_H)
            # In this part we take the minimum of the absolute value of the eigenvectors and take its asociated eigenvector
            W = np.array(eigenvects_HT_H_transpose[abs_eigenvals_HT_H.index(min(abs_eigenvals_HT_H))]).astype(
                np.float64)
            print(W)
        else:
            abs_Real_eigenvals = []
            for i in range(len(real_eigenval)):
                abs_Real_eigenvals.append(Abs(real_eigenval[i]))
            A = Matrix(np.array(eigenvects_H_transpose[:, abs_Real_eigenvals.index(
                min(abs_Real_eigenvals))]).reshape((4, 4)))
            print(A)
        # aquí vamos a aproximar la matrix por una de Mueller invertible
        W = mueller_aproximation(A)
        print(W)
        print("Es una aproximación de A por una matriz de Mueller invertible.")

    qm_graphic(W)
    plt.show()
