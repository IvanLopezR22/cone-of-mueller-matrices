import numpy as np
from matrix_norm import *
from sympy import *
from utils.request_matrix import request_matrix_interface
from utils.format_print_matrix import format_print_matrix
from van_der_mee_theorem import van_der_mee_theorem
from appr_invertible_mueller_matrix import appr_invert_mueller_matrix
from ecm import ecm
from k_irreducible import k_irreducible
from appr_invertible_matrix import make_invertible
from appr_mueller_matrix import appr_mueller_matrix
import matplotlib.pyplot as plt
import ctypes


LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]


font_info = CONSOLE_FONT_INFOEX()
font_info.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font_info.nFont = 0
font_info.dwFontSize.X = 0
font_info.dwFontSize.Y = 22  # Increase font size
font_info.FontFamily = 54  # Set font family (use Monospace)

ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE), False, ctypes.pointer(font_info)
)


np.set_printoptions(precision=15, suppress=True, linewidth=2000)

print("Enter the matrix you want to work with.")
main_matrix = request_matrix_interface("M")
print(f"The introduced matrix M is:\n{format_print_matrix(main_matrix)}")
print("-------------------------------------------------------------------------------")
e_1 = Matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

menu_options = {
    1: 'Matrix norm.',
    2: 'Van Der Mee quadratic form.',
    3: 'Know if the matrix is K-irreducible.',
    4: 'Approximation by an invertible matrix.',
    5: 'Approximation by a Mueller matrix.',
    6: 'Approximation by an invertible Mueller matrix.',
    7: 'Eigenvalue Calibration Method (ECM).',
    8: 'Enter a new matrix.',
    9: 'Exit.',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print("-----------------------------------")
    print(f'The norm of the introduced matrix M is: {matrix_norm(main_matrix)}')
    print("-----------------------------------")
    print('Press enter to return to the menu.')
    input()


def option2():
    plt.close("all")
    np.set_printoptions(precision=10, suppress=True, linewidth=2000)
    qm_0, mi_qm_0, minimum_qm_0, proy1_m_0, mi_proy1_m_0, minimum_proy1_m_0, fig_0 = \
        van_der_mee_theorem(main_matrix)
    if minimum_qm_0 >= 0 and minimum_proy1_m_0 >= 0:
        result = f"The minimum of the functions qM and proy1(M) of the matrix M are " \
                 f"{minimum_qm_0} and {minimum_proy1_m_0} respectively.\nTherefore M is a Mueller matrix."
        fig_0.text(0.5, 0.02, result, ha='center', fontsize=12)
    else:
        result = f"The minimum of the functions qM and proy1(M) of the matrix M are " \
                 f"{minimum_qm_0} and {minimum_proy1_m_0} respectively.\nTherefore M is NOT a Mueller matrix."
        fig_0.text(0.5, 0.02, result, ha='center', fontsize=12)
    print(f"-------------------------------------------------------------------------------")
    print(f"The function qm of the matrix M is:\nqm= {qm_0}.")
    print(f"A minimum point on the graph of qm is: {mi_qm_0}.")
    print(f"The minimum value of the function qm is {minimum_qm_0}, therefore:")
    print(f"-------------------------------------------------------------------------------")
    print(f"The function proy1(M) of the matrix M is:\nproy1(M)= {proy1_m_0}.")
    print(f"A minimum point on the graph of proy1(M) is: {mi_proy1_m_0}.")
    print(f"The minimum value of the function proy1(M) is {minimum_proy1_m_0}, therefore:")
    print(f"------------------------------------------")
    if minimum_qm_0 < 0 or minimum_proy1_m_0 < 0:
        print('The matrix M is NOT a Mueller matrix.')
    else:
        print('The matrix M is a Mueller matrix.')

    print("If you want to return to the menu, close the graph window.")
    plt.show()
    print('Press enter to return to the menu.')
    input()


def option3():
    print("------------------------------------------------------------------------------------")
    k_irreducible(main_matrix)
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option4():
    print("------------------------------------------------------------------------------------")
    invertible_main_matrix, det_main_matrix = make_invertible("M", main_matrix)
    if det_main_matrix != 0:
        print(f"Then, M(inv)=M is: \n{np.array(invertible_main_matrix).astype(np.float64)}")
    else:
        print(f"The matrix M(inv) is: \n{np.array(invertible_main_matrix).astype(np.float64)}")
        print(f"The determinant of M(inv) is {invertible_main_matrix.det()}.")
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option5():
    global main_matrix
    print("------------------------------------------------------------------------------------")
    norm_m = matrix_norm(main_matrix)
    m_appr, name, is_mueller = appr_mueller_matrix("M", main_matrix)
    if is_mueller:
        print(f"The matrix M=M(mu) is: \n{np.array(main_matrix).astype(np.float64)}.")
    else:
        m_appr = ((2 * norm_m) * e_1) + main_matrix
        qm_1, mi_qm_1, minimum_qm_1, proy1_m_1, mi_proy1_m_1, minimum_proy1_m_1, fig_1 \
            = van_der_mee_theorem(m_appr)
        print("------------------------------------------------------------------------------------")
        print(f"The approximation M(mu) of M by a Mueller matrix is:"
              f"\n{np.array(m_appr).astype(np.float64)}")
        print(f"The minimum of the functions qM(mu) and proy1(M(mu)) of M(mu) are "
              f"{minimum_qm_1} and {minimum_proy1_m_1} respectively.")
        print(f"Therefore, M(mu) is a Mueller matrix.")
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option6():
    print("------------------------------------------------------------------------------------")
    appr_invert_mueller_matrix("M", main_matrix)
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option7():
    print("------------------------------------------------------------------------------------")
    ecm(main_matrix)
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option8():
    global main_matrix
    main_matrix = request_matrix_interface("M")
    print(f"The input matrix M is:\n{format_print_matrix(main_matrix)}")


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Insert the number of the operation you want to perform in the matrix: '))
            print("------------------------------------------------------------------------------------")
        except:
            print('Invalid option. enter a number from 1 to 9.')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            option8()
        elif option == 9:
            print("Thanks.")
            exit()
        else:
            print("-----------------------------------------------")
            print('Invalid option. enter a number from 1 to 9.')
            print("-----------------------------------------------")
