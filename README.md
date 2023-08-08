# Cone of Mueller Matrices 


## Table of Contents

  1. [General instructions for the code in the article](#general-instructions-for-the-code-in-the-article)
  2. [Program execution](#program-execution)
  3. [Documentation](#documentation)

## General instructions for the code in the article

  <a name="General instructions for the code in the article--General information"></a><a name="1.1"></a>
  - [1.1] **General information**:
    - `The program is made in the Python version 3.14.4. `
    - `To download the project, click on "code" and then on download zip.`
    - `To use the code in the article, it is recommended to use Pycharm to compile it.`
        <br />https://www.jetbrains.com/es-es/pycharm/download/?section=windows
  <a name="General instructions for the code in the article--installation"></a><a name="1.2"></a>
  - [1.2] **Installation**:To install the libraries in the version of the code in the <br />
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
  - [3.1] **Matrix norm**: This program is based on the Rayleigh-Ritz Theorem.
  - Which assures us that the norm of the matrix M is the square root of the largest eigenvalue of the matrix $M^{T}M$.
  - [3.2] **Van Der Mee Theorem**: Deduce if a matrix is Mueller. Let $M$ be a $4\times 4-$ real matrix and 
$q_{M}$ be the quadratic form defined by $M^{T}GM$. Then $M$ is a Mueller matrix if and only if for all  $x\in K$ ($where
$K$ is the light cone) $q_{M}(x)\geq 0$ and $proy_{1}(M)(x)\geq $.
  - [3.3] **Know if the matrix is K-irreducible**: Using the Birkhoff-Vandergraft Theorem, a matrix $M\in \mathbb{M}_{4}(\mathbb{R})$
is $K$-irreducible if and only if the following is true:
  - The spectral radius $\rho(M)$ is an eigenvalue of $M$.
  - The spectral radius is a simple eigenvalue of $M$.
  - If there is another eigenvalue $r$ with norm $\rho(M)$, then $r$ is a simple eigenvalue of $M$.
  - If $v$ is the only eigenvalue associated to the spectral radius, then $v$ or $-v$ is in the light cone $K$.
  - [3.4] **Know if the matrix is K-primitive**: Using the Birkhoff-Vandergraft Theorem, a matrix $M\in \mathbb{M}_{4}(\mathbb{R})$
is $K$-primitive if and only if the following is true: 
    -  The spectral radius $\rho(M)$ is an eigenvalue of $M$.
    - The spectral radius is a simple eigenvalue of $M$.
    - There are no other eigenvalues $r$ with norm $\rho(M)$.
    - If $v$ is the only eigenvalue associated to the spectral radius, then $v$ or $-v$ is in the light cone $K$.
    - [3.4] **Approximation by invertible matrix**: If the introduced matrix M is invertible then the program leaves the matrix
unchanged. If the matrix M is not invertible then the program modify M to be invertible using the following:<br />
Let $M\in \mathbb{M}\_{4}(\mathbb{R})$ and $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{4}$
the eigenvalues of $M$, then we can find a number $\varepsilon\in (0,1/100]$ with $\varepsilon\not=\alpha_{i}$, $i=1,2,3,4$. 
Let $Id_{4}$ the identity of $\mathbb{M}_{4}(\mathbb{R})$, then $\varepsilon Id+M$ is an invertible matrix. 
  - [3.5] **Approximation by a Mueller matrix**: Use 3.2 to calculate if the introduce matrix $M$ is Mueller, if the matrix $M$ is
already a Mueller matrix then the program leaves the matrix unchanged. If the matrix $M$ is not Mueller then use the following to 
modify M to be a Mueller matrix: 
  - The matrix $E_{11}\in int_{\mathbb{M}\_{4}(\mathbb{R})}(\tilde{K})$ (the matrix $E\_{11}$ is the matrix with 1 in element 11 and zero in any other) 
and $E_{11}+(1/2*||M||)M \in \mathbb{B}\_{1}(E_{11}):=\{A\in \mathbb{M}\_{4}(\mathbb{R})\vert ||E_{11}-A||\leq 1\}$, therefore
$2||M||E_{11}+M\in \tilde{K}$.
  - [3.6] **Approximation by an invertible Mueller matrix**: We use 3.5 to modify the introduced matrix M to a Mueller matrix M(mu), 
then we use 3.4 to modify the matrix M(mu) to an invertible matrix. 
  - [3.7] **Approximation by a K-primitive matrix**: The program uses 3.5 to approximate the introduced matrix M to a Mueller matrix
M(mu) and then use the following to aproximate M(mu) to a K-primitive matrix:<br />
If a $M\in \mathbb{M}\_{4}(\mathbb{R})$ is a Mueller matrix then $ (1/100)E_{11}} + M\in int_{\mathbb{M}_{4}(\mathbb{R})}(\tilde{K})$. 
  - [3.8] **Eigenvalue Calibration Method (ECM)**: Calibration of polarization-state generators PSG's, polarimeters, and Mueller-matrix
ellipsometers MME's is an important factor in the practical use of these instruments. In the ECM, the PSG and the polarimeter 
are described by two 4×4 matrices $W$ and $A$, and their 32 coefficients are determined from three or four measurements performed on reference samples.<br />

    
