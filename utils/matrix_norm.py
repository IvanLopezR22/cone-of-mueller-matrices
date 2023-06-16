from sympy import *
from sympy import Abs

def norm_of_matrix(main_matrix):
    mult_transpose_main=(main_matrix.T)*main_matrix

    # Aquí estamos calculando los eigenvectores, eigenvalores y sus multiplicidades#
    eigenvects_mult_transpose_main=mult_transpose_main.eigenvects()
    eigenval_mtm=[]
    for element in eigenvects_mult_transpose_main:
        eigenval_mtm.append((element[0]))

    #Calculamos la norma de los eigenvectores y las aproximamos numericamente#
    norm_eigenval_mtm=[]
    for i in range(len(eigenval_mtm)):
        norm_eigenval_mtm.append(Abs(N(sqrt(re(eigenval_mtm[i])**2+im(eigenval_mtm[i])**2),10)))

    num_eigenval_mtm=[]
    for i in range(len(eigenval_mtm)):
        #Tenemos que hacer este doble proceso por la forma que aproxima los números
        num_eigenval_mtm.append(N(norm_eigenval_mtm[i]))


    s=sqrt(max(norm_eigenval_mtm))
    return s

