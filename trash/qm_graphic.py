from sympy import *
import sympy as sp

def qm_graphic():
   G=Matrix([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])
   M=Matrix([[1,2,3,0],[0,-1,5,7],[0,-1,0,9],[1,2,3,4]])

   N=Transpose(M)
   H=N*G*M

   x, y ,z, lam= sp.symbols('x,y,z,lam',real=True);
   f = Matrix([1,x,y,z]).dot(H*(Matrix([1,x,y,z])))
   g = x**2 + y**2 +z**2- 1
   print(f)
   #lam = sp.symbols('lambda', real = True)
   L = f - lam* g
   gradL = [sp.diff(L,c) for c in [x,y,z]] # gradient of Lagrangian w.r.t. (x,y)
   print(gradL)
   KKT_eqs = gradL + [g]
   print(KKT_eqs)
   stationary_points =nonlinsolve(KKT_eqs, [x, y, z, lam], dict=True) # solve the KKT equations
   print(stationary_points)

