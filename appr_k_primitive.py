import numpy as np
from sympy import *
from matrix_norm import matrix_norm
from van_der_mee_theorem import van_der_mee_theorem
from utils.know_k_irreducible_k_primitive import k_irreducible_k_primitive


def appr_k_primitive(w, main_matrix):
    e_1 = Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    # In this function, we make an approximation of M by a primitive matrix, denoted as M(prim).
    # Case 1. The introduced matrix M is K-primitive, then M(prim)=M
    # Case 2. The introduced matrix M is a Mueller matrix but not K-primitive, then M(prim)=(1/100)E_{11}+M.
    # Case 3. The introduced matrix M is not a Mueller matrix, then M(prim)=(1/100)E_{11}+M(mu).
    norm_m = matrix_norm(main_matrix)
    qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig = van_der_mee_theorem(main_matrix)

    # Here we are applying to M the algorithm to know if a matrix is K-primitive.
    ask_primitive = k_irreducible_k_primitive(main_matrix)[1]

    # This is the case in which the matrix M is K-primitive, then we leave M unchanged.
    if ask_primitive:
        m_primitive = main_matrix
        print(f"The input matrix is K-primitive. Then the approximation is the same M:"
              f" \n{np.array(main_matrix).astype(np.float64)}")

        return m_primitive

    # The second case is when the matrix M is a Mueller matrix and is not K-primitive.
    # Then we have an approximation M(prim) that we call the approximation of M by a K-primitive matrix.
    elif ask_primitive == False and minimum_qm >= 0 and minimum_proy1_m >= 0:
        m_primitive = (1 / 100 * e_1) + main_matrix

        print(f"The matrix {w} is a Mueller matrix but is not K-primitive.")
        print(f"The approximation {w}(prim) of {w} by a K-primitive Mueller matrix is: "
              f"\n{np.array(m_primitive).astype(np.float64)}")
        print(f"The K-primitive algorithm applied to {w}(prim) gives as a result: "
              f"{k_irreducible_k_primitive(m_primitive)[1]}")
        print(f"Therefore {w}(prim) is K-primitive.")
        print(f"-----------------------------------------------------------------------------")

        return m_primitive

    else:
        # In the last case the matrix M is not a Mueller matrix, therefore is not K-primitive.
        # Then first we approximate M by a Mueller matrix and then we appy the K-primitive
        # approximation to M(mu).
        m_primitive = (((2 * norm_m) * e_1) + main_matrix) + (1 / 100 * e_1)
        print(f"The minimum of the functions q{w} and proy1({w}) of the matrix {w} are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"Therefore, M is not a Mueller matrix and in consequence is not K-primitive.")
        print(f"----------------------------------------------------------------------------")
        print(f"The approximation {w}(prim) of {w} by a K-primitive Mueller matrix is: "
              f"\n{np.array(m_primitive).astype(np.float64)}")
        print(f"The K-primitive algorithm applied to {w}(prim) gives as a result: "
              f"{k_irreducible_k_primitive(m_primitive)[1]}")
        print(f"Therefore {w}(prim) is K-primitive.")
        print(f"-----------------------------------------------------------------------------")

        return m_primitive
