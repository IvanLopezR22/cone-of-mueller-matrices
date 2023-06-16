
from sympy import *
from sympy import Abs, Symbol, S, I
import sys
import numpy as np
from utils.matrix_formatter import formatter_matrix

def k_strongly_irreducible(M):
    M_np=formatter_matrix(M) #imprimimos la version numpy de la matriz M (se imprime por culumnas a diferencia de las de sympy)
    print('La matriz M introducida por el usuario es la siguiente')
    print(M_np)

    EV=M.eigenvects() #aquí estamos calculando los eigenvectores, eigenvalores y sus multiplicidades#
    #sympy nos calcula ternas en el orden (eigenvector, multiplicidad, eigenvector)
    #Lo siguiente es guardar los eigenvectores, eigenvalores y multiplicidad en listas diferentes
    eigenval=[]
    for element in EV:
        eigenval.append((element[0]))
    print(eigenval)

    mult_alg=[]
    for element in EV:
        mult_alg.append(element[1])
    print(mult_alg)

    eigenvec=[]
    for element in EV:
        eigenvec.append(element[2:])
    print(eigenvec)
    
    #Tenemos que encontrar el radio espectral de M

    num_eigenval=[]# calculamos los eigenvalores numéricamente.
    for i in range(len(eigenval)):
        num_eigenval.append(N(eigenval[i],10))
    print(num_eigenval)

    norm_eigenval=[]#Calculamos la norma de cada uno de los eigenvalores
    for i in range(len(eigenval)):
        norm_eigenval.append(Abs(N(eigenval[i],10)))
    print(norm_eigenval)

    for element in num_eigenval:
        print(simplify(element).is_real)

    ro_M=max(norm_eigenval)         # este es el radio espectral, ya que estamos tomando el maximo de lso eigenvectores
    ind_ro_M=norm_eigenval.index(ro_M) #indice del valor espectral en la lista de eigenvalores#
    print(ind_ro_M)
    print(ro_M)

    print(simplify(norm_eigenval[ind_ro_M]).is_real)

    con_ro_M=num_eigenval[ind_ro_M].conjugate() #con ese indice regresamos a la lista de eigenvalores numericos#
    print(con_ro_M)
    z=con_ro_M in num_eigenval                   #vemos si tiene conjungado para saber si es real#
    print(z)
    #Lo siguiente lo hacemos ya que las aproximaciones numéricas pueden aproximarnos un número real
    #con una parte muy pequeña imaginaria, por lo que buscamos el conjugado para comprobar que no sea real.
    if simplify(num_eigenval[ind_ro_M]).is_real==True:
        print('El radio espectral',ro_M,'es valor propio de M')
    elif simplify(num_eigenval[ind_ro_M]).is_real==False and z==False and re(num_eigenval[ind_ro_M])>0:
        print('El radio espectral',ro_M,'es valor propio de M')
    else:
        print('El radio espectral',ro_M,'NO es valor propio de M')
        print('Por lo tanto la matriz M no es K-fuertemente irreducible')
        sys.exit()

    # En este punto sabemos que el radio espectral es eigenvalor y queremos ver si es valor propio simple
    #Tenemos que encontrar si el radio espectral es valor propio simple (multiplicidad algebráica 1)

    print("La multiplicidad algebráica del radio espectral es")
    mul_alg_ro_M=mult_alg[ind_ro_M]
    print(mul_alg_ro_M)
    if mul_alg_ro_M!=1:
        print("El radio espectral no es valor propio simple, por lo que la matriz no es K-irreducible")
        sys.exit()
    else:
        print("El radio espectral es valor propio simple")

    #En este punto sabemos que el radio espectral es valor propio y es simple
    #Buscaremos valores propios cuyo valor absoluto sea igual al radio espectral

    index_1=[]
    for y in range(len(norm_eigenval)):
        if norm_eigenval[y]==ro_M:
            index_1.append(y)
        else:
            continue
    print(index_1)

    if index_1!=[]:
        print("Existe otro eigenvector cuyo valor absolto es igual al radio espectral ")
        print("Por lo tanto la matriz M no es K-fuertemente irreducible")
        return None
    else:
        print("No existe otro valor propio cuyo valor absoluto sea igual al del radio espectral")

    #En este punto sabemos que el radio espectral es eigenvalor simple y todos los valores propios con
    #valor absoluto igual al radio espectral son simples

    #Queda comprobar si el valor propio asociado al radio espectral está conenido dentro del cono
    #para ello usamos el vector propio único v asociado al radio espectral y vemos si vo -v está en el cono

    V=eigenvec[ind_ro_M] #esto es de la forma ([Matrix([]])
    print(V)
    U=V[0] #Extraemos el único elemento de la lista y obtenemos ahora la matriz [Matrix([])]
    print(U)
    W=U[0] #extramos de nuevo el único elemento de la lista y obtenemos ahora la matrix Matrix([])
    print(W)
    print(W[0,0])
    print(W[1,0])
    print(W[2,0])
    print(W[3,0])

    #Comprobamos que el único valor propio asociado a ro_M esté contenido en el cono

    print("---------------------------------")
    if Abs(N((W[3,0])**2,10))+Abs(N((W[2,0])**2,10))+Abs(N((W[1,0])**2,10))<=Abs(N((W[0,0])**2,10)):
        print("EL eigenvector asociado al radio espectral pertenece al cono K, por lo tanto M es K-fuertemente irreducible")
    else:
        print("El vector propio asociado al radio espectral no está en el cono, por lo que la matriz no es K-fuertemente irreducible")
    print("---------------------------------")