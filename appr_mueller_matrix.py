import numpy as np
from sympy import *
from matrix_norm import matrix_norm
from van_der_mee_theorem import van_der_mee_theorem

np.set_printoptions(precision=10, suppress=True, linewidth=2000)


# Given a matrix M we can generate an approximation M(mu) of M by a Mueller matrix.
# We call M(mu) the approximation of M by a Mueller matrix.
def appr_mueller_matrix(w, m):
    # The matrix e_1 in the code is called E_{11} in the comments.
    e_1 = Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    norm_m = matrix_norm(m)
    qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig = van_der_mee_theorem(m)

    # In the first case we have that M is already a Mueller matrix. Then we do nothing to M.
    if minimum_qm >= 0 and minimum_proy1_m >= 0:
        m_appr = m
        print(f"The minimum of the functions q{w} and proy1({w}) of the matrix {w} are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"Therefore, the matrix {w} is a Mueller matrix. Then {w} need not to be "
              f"approximated by a Mueller matrix.")
        if __name__ == '__main__':
            print(f"The matrix {w}={w}(mu) is: \n{np.array(m).astype(np.float64)}.")
        name = str(w)
        is_mueller = True
        return m_appr, name, is_mueller

    # Now, for the case in which the input matrix M is not a Mueller matrix we have an approximation M(mu)
    # defined by ((2*||M||)*E_{11})+M.
    else:
        m_appr = ((2*norm_m)*e_1)+m

        print(f"The minimum of the functions q{w} and proy1({w}) of the matrix {w} are "
              f"{minimum_qm} and {minimum_proy1_m} respectively.")
        print(f"Therefore, the matrix {w} is not a Mueller matrix. Then we approximate {w} to {w}(mu).")
        name = str(w)+"(mu)"
        is_mueller = False

        return m_appr, name, is_mueller
