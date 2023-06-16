#programa para saber si una matriz es de Meuller#

import numpy as np

matriz=[]
G=[[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]
for raw_position in range(4):
    raw=[]
    for element in range(4):
        raw.append(float(input(f"introduce el elemento {raw_position+1}, {element+1}: ")))
    matriz.append(raw)
M=np.array(matriz)
MT=M.transpose()
print(MT)
B=np.matmul(G,M)
C=np.matmul(G,MT)
A=np.matmul(C,B)
print(A)

print(w)
t=np.iscomplex(w)
x=0
for element in t:
    if element==False:
        x=x+1
if x<4:
    print("La matriz no es de Meuller")
elif x==4:
    print("La matriz es de Meuller")

