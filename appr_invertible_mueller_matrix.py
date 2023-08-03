import numpy as np
from appr_mueller_matrix import appr_mueller_matrix
from appr_invertible_matrix import make_invertible
from van_der_mee_theorem import van_der_mee_theorem

np.set_printoptions(precision=10, suppress=True, linewidth=2000)


def appr_invert_mueller_matrix(w, main_matrix):
    # We call M(mu-inv) to the approximation of M by an invertible Mueller matrix.
    # Based on the functions make_invertible(M), appr_mueller_matrix(M) and the notation of the comments from the file
    # approximation_by_mueller_matrix we have 3 cases:
    # Case 1: The matrix M is an invertible Mueller matrix, then M=M(mu-inv).
    # Case 2: The matrix M is a Mueller matrix but is not invertible, then M(mu-inv)=M(inv).
    # Case 3: The matrix M is not a Mueller, then M(mu-inv)=M(mu)(inv).
    m_mue_appr, name, is_mueller = appr_mueller_matrix(w, main_matrix)
    m_mue_inv, det_main_matrix = make_invertible(name, m_mue_appr)
    qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig = van_der_mee_theorem(m_mue_inv)
    print(f"Due to the previous data, the approximation {w}(mu-inv) of {w} by an invertible Mueller matrix is: "
          f"\n{np.array(m_mue_inv).astype(np.float64)}")
    print(f"The minimum of the functions q{w}(mu-inv) and proy1({w}(mu-inv)) of {w}(mu-inv) are "
          f"{minimum_qm} and {minimum_proy1_m} respectively.")
    print(f"The determinant of {w}(mu-inv) is {m_mue_inv.det()}. Therefore, {w}(mu-inv) is "
          f"an invertible Mueller matrix.")

    return m_mue_inv
