# The cone of Mueller Matrices 


## Table of Contents

  1. [General instructions for the code in the article](#general-instructions-for-the-code-in-the-article)
  2. [Program execution](#program-execution)
  3. [Documentation](#documentation)

## General instructions for the code in the article

  <a name="General instructions for the code in the article--General information"></a><a name="1.1"></a>
  - [1.1] **General information**:
    - `The program is made in the Python version 3.11.2. `
    - `To download the project, click on "code" and then on download zip.`
    - `To use the code in the article, it is recommended to use Pycharm to compile it.`
        <br />https://www.jetbrains.com/es-es/pycharm/download/?section=windows
  <a name="General instructions for the code in the article--installation"></a><a name="1.2"></a>
  - [1.2] **Installation**:To install the libraries in the version of the code in the 
  article, download the file requirements and move it on your project. Then run the following command: pip install -r requirements.txt



## Program execution
   
  <a name="Program execution--Running without development tools"></a><a name="2.1"></a>
  - [2.1] **Running without development tools**:
    - `Access the dist/index folder and run the file index.exe`
   <a name="Program execution--Running with development tools"></a><a name="2.2"></a>
  - [2.1] **Running with development tools**:
    - `Run index.py as entry point.`
    
## Documentation

  <a name="Documentation-Matrix norm"></a><a name="3.1"></a>
  - [3.1] **Matrix norm**: This program is based on the Rayleigh-Ritz Theorem. Which assures us that the norm of the matrix 
$M$ is the square root of the largest eigenvalue of the matrix $M^{T}M$.<br />
  - [3.2] **Van Der Mee quadratic form**: Deduce if a matrix is Mueller. Let $M$ be a $4\times 4-$ real matrix,
$q_{M}$ be the quadratic form defined by $M^{T}GM$ and $proy_{1}(M)$ the projection on the first coordinate.
Then $M$ is a Mueller matrix if and only if for all  $x\in K$ (where $K$ is the light cone) $q_{M}(x)\geq 0$ and $proy_{1}(M)(x)\geq 0$.<br />
  - [3.3] **Know if the matrix is K-irreducible**: Using the Birkhoff-Vandergraft Theorem, a matrix $M\in \mathbb{M}_{4}(\mathbb{R})$
is $K$-irreducible if and only if the following is true:
    - For all $v\in K$ such that $Mv=\rho_{M}v$ then $v\in int_{\mathbb{R}}(K)$.
    - For all $\lambda \not= \rho_{M}$ eigenvalue of $M$ and for all $w$ eigenvector of $\lambda$ it is truth that $w\not\in K$.<br />
  - [3.4] **Approximation by an invertible matrix**: If the introduced matrix M is invertible then the program leaves the matrix
unchanged. If the matrix $M$ is not invertible then the program modify $M$ to be invertible using the following:<br />
Let $M\in \mathbb{M}\_{4}(\mathbb{R})$ and $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{4}$
the eigenvalues of $M$, then we can find a number $\varepsilon\in (0,1/100]$ with $\varepsilon\not=\alpha_{i}$, $i=1,2,3,4$. 
Let $Id_{4}$ the identity of $\mathbb{M}_{4}(\mathbb{R})$, then $\varepsilon Id+M$ is an invertible matrix. <br />
We denote  as $M(inv)$ the approximation of $M$ by an invertible matrix.
  - [3.5] **Approximation by a Mueller matrix**: Use 3.2 to calculate if the introduce matrix $M$ is Mueller. If the matrix $M$ is
already a Mueller matrix then the program leaves the matrix unchanged. If the matrix $M$ is not Mueller then use the following to 
modify M to be a Mueller matrix: <br /> 
The matrix $E_{11}\in int_{\mathbb{M}\_{4}(\mathbb{R})}(\tilde{K})$ (the matrix $E\_{11}$ is the matrix with 1 in element 11 and zero in any other) 
and $E_{11}+(1/2*||M||)M \in \mathbb{B}\_{1}(E_{11}):=\\{A\in \mathbb{M}\_{4}(\mathbb{R})\vert ||E_{11}-A||\leq 1\\}$, therefore
$2||M||E_{11}+M\in \tilde{K}$.<br />
We denote as $M(mu)$ the approximation of $M$ by a Mueller matrix.
  - [3.6] **Approximation by an invertible Mueller matrix**: We use 3.5 to modify the introduced matrix $M$ to a Mueller matrix $M(mu)$, 
then we use 3.4 to modify the matrix $M(mu)$ to an invertible matrix.<br />
We denote as $M(mu-inv)$ the approximation of $M$ by an invertible Mueller matrix.
  - [3.7] **Eigenvalue Calibration Method (ECM)**: Calibration of polarization-state generators PSG's, polarimeters, and Mueller-matrix
ellipsometers MME's is an important factor in the practical use of these instruments. In the ECM, the PSG and the polarimeter 
are described by two 4×4 matrices $W$ and $A$, and their 32 coefficients are determined from three or four measurements performed on reference samples.<br />
The user enters the matrices $M$, $aw$ and $amw$ and the program does the following:<br />
    - The program 3.4 is used in aw to ensure that it is invertible.
    - Calculate the matrix form in canonical base of the linear funtion $H:\mathbb{M}\_{4}(\mathbb{R}) \rightarrow \mathbb{M}_{4}(\mathbb{R})$
    defined by $H(X)=MX-X(aw^{-1})(amw)$.
    - Calculate the null space of H.<br />
    **Case 1**: The null space of $H$ is non-trivial: The program search for an invertible matrix in the null space, if there 
    are none then select the first one it finds and that matrix is named $W$.<br />
    **Case 2.1.**: The null space of $H$ is trivial and $H$ have real eigenvalues: The program calculate the norm of real 
    eigenvalues and selects an eigenvector associated to the real eigenvalue with minimum norm, that matrix is named $W$.<br />
    **Case 2.2.** The null space of $H$ is trivial and $H$ has no real eigenvalues: The program calculate the eigenvalues of the 
    matrix $H^{T}H$, which are all non-negative. Then select an eigenvector associated to the smallest eigenvalue of $H^{T}H$.
    That matrix is named $W$.
  - Using 3.4 in $W$ we ensure that our $W$ is invertible.
  - Calculate the new $M$ as $W(aw^{-1})amw(W^{-1})$.
  - Finally, the program uses 3.6 to approximate the new M by an invertible Mueller matrix. This is our final matrix.
    
    
    
