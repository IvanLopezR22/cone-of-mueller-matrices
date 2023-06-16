
from sympy import *
from sympy import Abs
from utils.matrix_formatter import formatter_matrix

def k_irreducible(M):
    #eigen is a list of triples of the form (eigenvalue, algebraic multiplicity, eigenvectors)
    eigen_M=M.eigenvects()

    #Here we separate eigenvalues, algebraic multiplicity and eigenvectors on different lists, related with the same index.
    #On the next lists, the eigenvalues, eigenvalues and algebraic multiplicity, eigenvectors are calculated excatly
    eigenval=[]
    for element in eigen_M:
        eigenval.append((element[0]))
    #print(eigenval)

    mult_alg=[]
    for element in eigen_M:
        mult_alg.append(element[1])
    print(mult_alg)

    eigenvec=[]
    for element in eigen_M:
        eigenvec.append(element[2:])
    #print(eigenvec)
    #We have to calculate the spectral radius of M
    #Now approximate the exact eigenvalues numerically.
    num_eigenval=[]
    for i in range(len(eigenval)):
        num_eigenval.append(N(eigenval[i],10))
    print('Los valores propios de la matriz son: ',num_eigenval)

    #When we calculate eigenvalues, the numerical approximation generate tiny imaginary parts on real eigenvalues
    #so we filtered that error in the next list, using the fact that in this case imaginary roots comes with their conjugate
    eigenvals_without_error=[]
    for i in num_eigenval:
        conj=i.conjugate()
        z=conj in num_eigenval
        if simplify(i).is_real == True:
            eigenvals_without_error.append(i)
        elif simplify(i).is_real == False and z == False:
            eigenvals_without_error.append(re(i))
        else:
            eigenvals_without_error.append(i)
    print('valores propios sin error',eigenvals_without_error)

    #Now we calculate the norm of the eigenvalues, so we can find the spectral radius
    norm_eigenval=[]
    for i in range(len(eigenvals_without_error)):
        norm_eigenval.append(Abs(eigenvals_without_error[i]))
    print('Calculamos la norma de los valores proios: ',norm_eigenval)

    #the spectral radius ro_M is the maximum on the list norm_eigenvalue
    ro_M=max(norm_eigenval)

    #Now we ask if ro_M is in the list of eigenvalues without error
    if (ro_M in eigenvals_without_error)==True:
        print('The spectral radius',ro_M,'is an eigenvalue of M')
        ind_ro_M = eigenvals_without_error.index(ro_M)
        print(ind_ro_M)
    else:
        print('The spectral radius',ro_M,'is NOT an eigenvalue of M')
        print('Therefore the matrix M is not K-irreducible')
        return


    #Now we find the algebraic multiplicity of the spectral radius
    mul_alg_ro_M=mult_alg[ind_ro_M]
    print(mul_alg_ro_M)
    if mul_alg_ro_M!=1:
        print('The spectral radius has algebraic multiplicity ',mul_alg_ro_M)
        print('Then, the spectral radius is not a simple eigenvalue. Therefore the matrix is NOT K-irreducible')
        return
    else:
        print('The spectral radius ',ro_M,' is a simple eigenvalue')

    #At this point we know the spectral radius is a simple eigenvalue of M
    #Now we search for eigenvals with absolute value equal ro_M (the spectral radius)
    index_1=[]
    for y in range(len(norm_eigenval)):
        if norm_eigenval[y]==ro_M:
            index_1.append(y)
        else:
            continue
    print(index_1)
    print('Los índices de losvalores propios con valor absoluto igual al radio espectral son ')
    for element in index_1:
        if mult_alg[element]!=1:
            print('Existe otro eigenvector ',eigenvals_without_error[element],' cuyo valor absolto es el radio espectral')
            print('tal que su multiplicidad algebráica es ', mult_alg[element] ,'por lo que no es valor propio simple')
            print("Por lo tanto la matriz M no es K-irreducible")
            return
        else:
            continue
    print("Todos los valores propios con valor absoluto igual al radio espectral son simples")

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
    #TODO: falta hacer la prueba con el inverso aditivo
    print("----------------------------------")
    if Abs(N((W[3,0])**2,10))+Abs(N((W[2,0])**2,10))+Abs(N((W[1,0])**2,10))<=Abs(N((W[0,0])**2,10)):
        print("EL eigenvector asociado al radio espectral pertenece al cono, por lo tanto M es K-irreducible")
    else:
        print("El vector propio asociado al radio espectral no está en el cono, por lo que la matriz no es K-irreducible")
    print("----------------------------------")



