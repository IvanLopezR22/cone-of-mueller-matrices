import sympy as sym
import numpy as np
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import cm
from sympy import *

backend = 'TkAgg'
matplotlib.use(backend)  # not detected

matplotlib.use('TkAgg', force=False)  # not detected

def qm_graphic(main_matrix):
    G=Matrix([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])

    x,y=sym.symbols('x,y')
    S = main_matrix*Matrix([1,x,y,sqrt(1-x**2-y**2)])
    T=G*(main_matrix*Matrix([1,x,y,sqrt(1-x**2-y**2)]))
    z=S.dot(T)


    print('La función qm=',z)
    z_lamb=sym.lambdify((x,y),z)

    a=1
    b=1
    xdata=np.linspace(-(b+1),(b+1),1001)
    ydata=np.linspace(-(b+1),(b+1),1001)

    X,Y=np.meshgrid(xdata,ydata)

    fig=plt.figure()
    ax=fig.add_subplot(111, projection='3d')
    R=(X**2+Y**2>a**2)
    z_masked=np.ma.masked_where(R,z_lamb(X,Y))
    surf=ax.plot_surface(X,Y, z_masked,cmap=cm.winter,
                        linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return z_masked, ax, X, Y, plt