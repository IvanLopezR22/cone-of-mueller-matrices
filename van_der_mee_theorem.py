import sympy as sym
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from sympy import *
import warnings
matplotlib.use('TkAgg')
backend = 'TkAgg'
matplotlib.use(backend)  # not detected
matplotlib.use('TkAgg', force=False)  # not detected
warnings.filterwarnings("ignore", category=RuntimeWarning)


def van_der_mee_theorem(main_matrix):
    G = Matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    x, y = sym.symbols('x,y')
    s = main_matrix * Matrix([1, x, y, sqrt(1 - x ** 2 - y ** 2)])
    t = G * (main_matrix * Matrix([1, x, y, sqrt(1 - x ** 2 - y ** 2)]))

    # For a 4x4 matrix M, the function qM is the quadratic form of the Van Der Mee Theorem and proy1(M)
    # the projection on the first coordinate, which in the code are called qm and proy1_m respectively.
    # A matrix M in M_{4}(R) is a Mueller matrix if and only if qM>=0 and proy1(M)>=0.
    qm = s.dot(t)
    proy1_m = (main_matrix * Matrix([1, x, y, sqrt(1 - x ** 2 - y ** 2)]))[0]
    # Next we plot the function qm and proy1(M) using Matplotlib.
    z_lamb_1 = sym.lambdify((x, y), qm)
    z_lamb_2 = sym.lambdify((x, y), proy1_m)
    a = 1
    b = 1
    xdata = np.linspace(-(b + .25), (b + .25), 1001)
    ydata = np.linspace(-(b + .25), (b + .25), 1001)
    X, Y = np.meshgrid(xdata, ydata)
    fig = plt.figure(figsize=(3.5 * 3.13, 1.5 * 3.13))
    ax_1 = fig.add_subplot(121, projection='3d')
    ax_2 = fig.add_subplot(122, projection='3d')
    R = (X ** 2 + Y ** 2 > a ** 2)
    expr_1 = sympify(qm)
    symbols_qm = expr_1.free_symbols
    expr_2 = sympify(proy1_m)
    symbols_m_1 = expr_2.free_symbols
    if not symbols_qm:
        K_1 = np.around(np.full((1001, 1001), qm).astype(np.float64), decimals=12)
    else:
        K_1 = np.around(z_lamb_1(X, Y), decimals=12)

    if not symbols_m_1:
        K_2 = np.around(np.full((1001, 1001), proy1_m).astype(np.float64), decimals=12)
    else:
        K_2 = np.around(z_lamb_2(X, Y), decimals=12)

    z_masked_1 = np.ma.masked_where(R, K_1)
    z_masked_2 = np.ma.masked_where(R, K_2)
    surf_1 = ax_1.plot_surface(X, Y, z_masked_1, cmap=cm.winter, linewidth=0, antialiased=False)
    fig.colorbar(surf_1, shrink=0.5, aspect=15,  location='left')
    ax_1.set_title(r'Graph of the function $q_{M}$')
    ax_1.set_xlabel('x-axis')
    ax_1.set_ylabel('y-axis')
    ax_1.set_zlabel('z-axis')

    surf_2 = ax_2.plot_surface(X, Y, z_masked_2,cmap=cm.autumn, linewidth=0, antialiased=False)
    fig.colorbar(surf_2, shrink=0.5, aspect=15, location='left')
    ax_2.set_title(r'Graph of the function $proy_{1}(M)$')
    ax_2.set_xlabel('x-axis')
    ax_2.set_ylabel('y-axis')
    ax_2.set_zlabel('z-axis')

    fig.suptitle('Van Der Mee Theorem', fontsize=16)

    # Now we find the minimum of the function qM and proy1(M).
    xmin_qm, ymin_qm = np.unravel_index(np.argmin(z_masked_1), z_masked_1.shape)
    mi_qm = (X[xmin_qm, ymin_qm], Y[xmin_qm, ymin_qm], z_masked_1.min())
    ax_1.scatter(X[xmin_qm, ymin_qm], Y[xmin_qm, ymin_qm], z_masked_1.min(), c='red', s=10)
    minimum_qm = z_masked_1.min()

    xmin_proy1_m, ymin_proy1_m = np.unravel_index(np.argmin(z_masked_2), z_masked_2.shape)
    mi_proy1_m = (X[xmin_proy1_m, ymin_proy1_m], Y[xmin_proy1_m, ymin_proy1_m], z_masked_2.min())
    ax_2.scatter(X[xmin_proy1_m, ymin_proy1_m], Y[xmin_proy1_m, ymin_proy1_m], z_masked_2.min(), c='blue', s=10)
    minimum_proy1_m = z_masked_2.min()

    return qm, mi_qm, minimum_qm, proy1_m, mi_proy1_m, minimum_proy1_m, fig
