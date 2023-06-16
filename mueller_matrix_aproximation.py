from sympy import *
from sympy import Abs
from utils.mueller_matrix_aproximation import mueller_aproximation_util

def mueller_aproximation(main_matrix):
    F = mueller_aproximation_util(main_matrix)
    return F
