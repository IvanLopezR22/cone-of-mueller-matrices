
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
$$x$$


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
  - [3.2] **Van Der Mee Theorem**: Deduce if a matrix is Mueller. Let $M$ be a $4\times 4-$real matrix and 
$q_{M}$ be the quadratic form defined by $M^{T}GM$. Then

$M$ is Mueller if and only if for all $\left( 
```math
begin{bmatrix}X\\Y\end{bmatrix}
```
