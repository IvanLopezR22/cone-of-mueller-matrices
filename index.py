from matrix_norm import *
from mueller_matrix_aproximation import mueller_aproximation
from utils.ask_for_matrix import ask_for_matrix_interface
from utils.matrix_formatter import formatter_matrix
from vandermee_criteria import vandermee_criteria
from compain_method import compain_method
from k_irreducible import k_irreducible
from k_strongly_irreducible import k_strongly_irreducible


print("Se le solicitará una matriz para trabajar en cualquiera de las opciones.")
main_matrix = ask_for_matrix_interface("M")
main_matrix_np = formatter_matrix(main_matrix)

print("La matriz introducida es: \n", main_matrix_np)

menu_options = {
    1: 'Norma de matriz',
    2: 'Aproximación por matriz de Mueller',
    3: 'Validación de Mueller (Criterio de Mueller)',
    4: 'Método de Compain',
    5: 'Saber si la matriz es K-irreducible',
    6: 'Saber si la matriz es K-fuertemente irreducible',
    7: 'Limpiar matriz (Insertar una nueva)',
    8: 'Salir',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    matrix_norm_result = matrix_norm(main_matrix)
    print("-----------------------------------")
    print("El resultado de la norma de matriz es:", matrix_norm_result)
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option2():
    mueller_aproximation_matrix = mueller_aproximation(main_matrix)
    print("-----------------------------------")
    print("F=", formatter_matrix(mueller_aproximation_matrix))
    print("Es una aproximación de main_matrix por una matriz de Mueller invertible.")
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option3():
    print("-----------------------------------")
    vandermee_criteria(main_matrix)
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option4():
    print("-----------------------------------")
    compain_method(main_matrix)
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option5():
    print("-----------------------------------")
    k_irreducible(main_matrix)
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option6():
    print("-----------------------------------")
    k_strongly_irreducible(main_matrix)
    print("-----------------------------------")
    print('Presiona enter para volver al menú')
    input()


def option7():
    global main_matrix
    main_matrix = ask_for_matrix_interface("M")
    main_matrix_np = formatter_matrix(main_matrix)
    print("La matriz introducida es: \n", main_matrix_np)
    print('Presiona enter para volver al menú')
    input()


if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('¿Que deseas hacer con tu matriz?: '))
        except:
            print('Opcion incorrecta. Ingresa una opción valida.')
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
            print("Thanks")
            exit()
        else:
            print('Opción invalida. Ingrese un número entre 1 y 7.')
