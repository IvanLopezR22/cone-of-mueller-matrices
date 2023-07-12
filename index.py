import numpy as np
from matrix_norm import *
from tkinter import *
from mueller_matrix_approximation import mueller_approximation
from utils.ask_for_matrix import ask_for_matrix_interface
from utils.format_print_matrix import format_print_matrix
from van_der_mee_theorem import van_der_mee_theorem
from ecm import ecm
from k_irreducible import k_irreducible
from k_strongly_irreducible import k_strongly_irreducible

np.set_printoptions(precision=10, suppress=True, linewidth=2000)

print("Enter the matrix you want to work with.")
main_matrix = ask_for_matrix_interface("M")
print(f"The input matrix M is:\n{format_print_matrix(main_matrix)}")
print("-----------------------------------------------------------")


menu_options = {
    1: 'Matrix norm.',
    2: 'Invertible Mueller matrix approximation.',
    3: 'Van Der Mee Theorem.',
    4: 'Eigenvalue Calibration Method (ECM).',
    5: 'Know if the matrix is K-irreducible.',
    6: 'Know if the matrix is K-strongly irreducible.',
    7: 'Enter a new matrix.',
    8: 'Exit.',
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
    z_masked, ax, qm_1,plt, mi_1, minimum_qm_1 = van_der_mee_theorem(main_matrix)
    if minimum_qm_1 >= 0 and main_matrix.det() != 0:
        print(f"The matrix M is an invertible Mueller matrix. So we set M as: \n{np.array(main_matrix).astype(np.float64)}")
    else:
        m_apr = mueller_approximation(main_matrix)
        print(f"The input matrix M is not an invertible Mueller matrix.")
        print(f"An approximation of M by an invertible Mueller matrix is:\n{format_print_matrix(m_apr)}")
    print(minimum_qm_1)
    print('Press enter to return to the menu.')
    input()


def option3():
    z_masked, ax, qm, plt, mi, minimum_qm = van_der_mee_theorem(main_matrix)
    print(f"The function qm of the matrix M is:\n qm= {qm}.")
    print("------------------------------------------------------------------------------------")
    print(f"A minimum point on the graph of qm is: {mi}.\nSuch a minimum point is marked in red on the graph.")
    print(f"The minimum value of the function qm is {minimum_qm}, therefore:")

    if minimum_qm < 0:
        print('The matrix M is NOT a Mueller matrix.')
    else:
        print('The matrix M is a Mueller matrix.')

    print("Close the graph if you want to go to the menu.")
    plt.show()

    print('Press enter to return to the menu.')
    input()


def option4():
    ecm(main_matrix)
    print('Press enter to return to the menu.')
    input()


def option5():
    print("------------------------------------------------------------------------------------")
    k_irreducible(main_matrix)
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option6():
    print("------------------------------------------------------------------------------------")
    k_strongly_irreducible(main_matrix)
    print("------------------------------------------------------------------------------------")
    print('Press enter to return to the menu.')
    input()


def option7():
    global main_matrix
    main_matrix = ask_for_matrix_interface("M")
    print(f"The input matrix M is:\n{format_print_matrix(main_matrix)}")


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Insert the number of the operation you want to perform in the matrix: '))
            print("-----------------------------------------------------------------------------------------")
        except:
            print('Invalid option. enter a number from 1 to 7.')
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
            print("Thanks.")
            exit()
        else:
            print('Invalid option. enter a number from 1 to 7.')
