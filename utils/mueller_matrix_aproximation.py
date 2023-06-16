from sympy import *
from sympy import Abs
from matrix_norm import matrix_norm

def mueller_aproximation_util(main_matrix):
    E_1=Matrix([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    Id=Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

    norm_main_matrix= matrix_norm(main_matrix)
    print("La norma matricial de main_matrix es", norm_main_matrix)

    # Aquí estamos calculando los eigenvectores, eigenvalores y sus multiplicidades#
    eigen_M=main_matrix.eigenvects()

    norm_eigenvals_M=[]
    for i in range(len(eigen_M)):
        norm_eigenvals_M.append(Abs(N(eigen_M[i][0],10)))
    print(norm_eigenvals_M)

        
    p=max(norm_eigenvals_M)
    print(norm_eigenvals_M)

    F=(((p*E_1)+(1/(2*norm_main_matrix))*main_matrix)*Id)+((E_1)+(1/(2*norm_main_matrix))*main_matrix)
    return F
