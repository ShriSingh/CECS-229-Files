# %% [markdown]
# # CECS 229 Programming Assignment #5
# 
# #### Due Date: 
# 
# Sunday, 4/9 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the to CodePost a file named `pa5.py` by the due date:
# 
# 
# #### Objectives:
# 
# 1. Define a matrix data structure with relevant matrix operations.
# 2. Understand the role of matrices in simple image processing applications. 
# 
# 
# 

# %% [markdown]
# --------------------------------------------------------
# 
# #### Problem 1.
# 
# 
# Implement a class `Matrix` that creates matrix objects with attributes
# 1. `colsp` -column space of the `Matrix` object, as a list of columns (also lists)
# 2. `rowsp` -row space of the `Matrix` object, as a list of rows (also lists)
# 
# The constructor takes a list of rows as an argument, and constructs the column space from this rowspace.  If a list is not provided, the parameter defaults to an empty list.
# 
# You must implement the following methods in the `Matrix` class:
# 
# ***Setters***
# * `set_col(self, j, u)` - changes the j-th column to be the list `u`.  If `u` is not the same length as the existing columns, then the method raises a `ValueError` with the message `Incompatible column length.`
# * `set_row(self,i, v)` - changes the i-th row to be the list `v`.  If `v` is not the same length as the existing rows, then method raises a `ValueError` with the message `Incompatible row length.`
# * `set_entry(self,i, j, x)` - changes the existing $a_{ij}$ entry in the matrix to `x`.
# 
# ***Getters***
# * `get_col(self, j)` - returns the j-th column as a list.  
# * `get_row(self, i)` - returns the i-th row as a list `v`. 
# * `get_entry(self, i, j)` - returns the existing $a_{ij}$ entry in the matrix.
# * `col_space(self)` - returns the *list* of vectors that make up the column space of the matrix object
# * `row_space(self)` - returns the *list* of vectors that make up the row space of the matrix object
# * `get_diag(self, k)` - returns the $k$-th diagonal of a matrix where $k =0$ returns the main diagonal,
# $k > 0$ returns the diagonal beginning at $a_{1(k+1)}$, and $k < 0$ returns the diagonal beginning at $a_{(-k+1)1}$.  e.g. `get_diag(1)` for an $n \times n$ matrix returns [$a_{12}, a_{23}, a_{34}, \dots, a_{(n-1)n}$]
# * `__str__(self)` - returns a formatted string representing the matrix entries as 
# 
# $\hspace{10cm} \begin{array} {c} a_{11} & a_{12} & \dots & a_{1m} \\ a_{21} & a_{22} & \dots & a_{2m} \\ \vdots & \vdots & \ddots & \vdots \\a_{m1} & a_{m2} & \dots & a_{mn} \end{array}$
# 
# ***Overloaded operators***
# 
# In addition to the methods above, the `Matrix` class must also overload the `+`, `-`, and `*` operators to support:
# 
# 1. `Matrix + Matrix` addition
# 2. `Matrix - Matrix` subtraction
# 3. `Matrix * scalar` multiplication
# 4. `Matrix * Matrix` multiplication
# 5. `Matrix * Vec` multiplication
# 6. `scalar * Matrix` multiplication

# %%
# Importing the Vector class(created in the previous assignment) from the vector.py file
# from Vector import Vec

# Writing a Matrix class to create matrix objects with rows and columns with overloaded operators
class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)

    # Constructing columns based on the number of row space
    def _construct_cols(self, rowsp):
        # Intializing column space as an empty list
        colsp = []
        # Setting Column number the same as the number of rows in the row space
        cols_num = len(rowsp[0])
        # Creating a list of empty lists for each column space
        for _ in range(cols_num):
            colsp.append([])
        
        # Iterating through each row in the row space
        for row in rowsp:
            # Iterating through each entry in the row
            for i, entry in enumerate(row):
                # Appending the entry to the column space list
                colsp[i].append(entry)
        return colsp

    def set_col(self, j, u):
        '''
        Changes the j-th column to be the list `u`.  If `u` is not the same length 
        as the existing columns, then the method raises a `ValueError` with the 
        message `Incompatible column length.`
        '''
        # Conditional statement to check u = length of the existing columns
        if len(u) != len(self.colsp[0]):
            # Raising ValueError if condition is not met
            raise ValueError("Incompatible column length.")
        else: # Running the code below if the condition is met
            # Updating the first column space with the new column
            self.colsp[j - 1] = u # -> j-1 because the index starts from 0
            # Iterating through the row space
            for i in range(len(self.rowsp)):
                # Updating the row space with the new column
                self.rowsp[i][j - 1] = u[i]

    def set_row(self, i, v):
        '''
        Changes the i-th row to be the list `v`.  If `v` is not the same length 
        as the existing rows, then method raises a `ValueError` with the 
        message `Incompatible row length.`
        '''
        # Conditional statement to check v = length of the existing rows
        if len(v) != len(self.rowsp[0]): # Starting from 0 because the index starts from 0
            # Raising ValueError if condition is not met
            raise ValueError("Incompatible row length.")
        else: # Running the code below if the condition is met
            # Updating the row space with the new row
            self.rowsp[i - 1] = v
            # Reconstructing the column space of the matrix
            self.colsp = self._construct_cols(self.rowsp)

    def set_entry(self, i, j, x):
        '''
        Changes the existing a_ij entry in the matrix to 'x'.
        '''
        # Replacing the j-th entry in the row with x
        self.rowsp[i - 1][j - 1] = x # -> i-1, j-1 because the index starts from 0
        # Replacing the i-th entry in the column with x
        self.colsp[j - 1][i - 1] = x # -> i-1, j-1 because the index starts from 0

    # Returns the j-th column as a list
    def get_col(self, j):
        return self.colsp[j - 1] # -> j-1 because the index starts from 0
    
    # Returns the i-th row as a list v
    def get_row(self, i):
        return self.rowsp[i - 1] # -> i-1 because the index starts from 0
    
    # Returns the a_ij entry in the matrix
    def get_entry(self, i, j):
        return self.rowsp[i - 1][j - 1]
    
    # Returns the list of vectors that make up the column space of the matrix object
    def row_space(self):
        return self.rowsp
    
    # Returns the list of vectors that make up the row space of the matrix object
    def col_space(self):
        return self.colsp
    
    def get_diag(self, k):
        '''
        Returns the k-th diagonal of the matrix as a list, where:
        -> k = 0 returns the main diagonal
        -> k > 0 returns the diagonal beginning at a_1(k+1)
        -> k < 0 returns the diagonal beginning at a_-(k+1)1
        '''
        if k > 0:
            # Storing diagonal entries beginning at a_1(k+1)
            diag_3 = []
            # Iterating through the row spaces from a_1(k+1)
            for i in range(len(self.rowsp) - k):
                # Appending the values based on the given kth value
                diag_3.append(self.rowsp[i][i + k]) # -> 1(k+1) => (1)(k+1) => [i][i+k]
            # Returning the diagonal values from a_1(k+1)
            return diag_3
        elif k < 0:
            # Storing diagonal entries beginning at a_-(k+1)1 
            diag_2 = []
            # Iterating through the row spaces from a_-(k+1)1
            for i in range(len(self.rowsp) + k):
                # Appending the values based on the given kth value
                diag_2.append(self.rowsp[i - k][i]) # -> -(k+1)1 => (1-k)(1) => [i-k][i]
            # Returning the diagonal values from a_-(k+1)1
            return diag_2
        else:
            # Storing the main diagonal entries           
            main_diag = []
            # Iterating through the row spaces 
            for i in range(len(self.rowsp)):
                # Appending the values of the main diagonal
                main_diag.append(self.rowsp[i][i])
            # Returning the values of the main diagonal
            return main_diag

    def __add__(self, other):
        if len(self.rowsp) != len(other.rowsp) or len(self.colsp) != len(other.colsp):
            raise ValueError("Incompatible matrix dimensions for addition.")
        else:
            # Creating a list of empty lists for the sum of the matrices
            matrix_sum = []
            for i in range(len(self.rowsp)):
                row_sum = []
                for j in range(len(self.colsp)):
                    # Appending the sum of the corresponding entries to row sum
                    row_sum.append(self.rowsp[i][j] + other.rowsp[i][j])
                # Appending the row sum to the matrix sum
                matrix_sum.append(row_sum)
            # Returning the matrix sum as a Matrix object
            return Matrix(matrix_sum)

    def __sub__(self, other):
        if len(self.rowsp) != len(other.rowsp) or len(self.colsp) != len(other.colsp):
            raise ValueError("Incompatible matrix dimensions for subtraction.")
        else:
            # Creating a list of empty lists for the difference of the matrices
            matrix_diff = []
            for i in range(len(self.rowsp)):
                # Storing each reduced row in a list
                row_diff = []
                for j in range(len(self.colsp)):
                    # Appending the difference of the corresponding entries to row difference
                    row_diff.append(self.rowsp[i][j] - other.rowsp[i][j])
                # Appending the row difference to the matrix difference
                matrix_diff.append(row_diff)
            # Returning the reduced matrix as a Matrix object
            return Matrix(matrix_diff)
        
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            # Storing the product of matrix-scalar multiplication
            scalar_mult_matrix = []
            # Iterating through each row in the row space
            for matrix_row in self.rowsp:
                # Storing the each scaled row in a list
                scaled_row = []
                # Going through each element in the row
                for element in matrix_row:
                    # Mulitplying each element with the scalar value
                    scaled_element = element * other
                    # Appending the scaled product into the scaled row
                    scaled_row.append(scaled_element)
                # Appending the scaled rows to the scaled matrix
                scalar_mult_matrix.append(scaled_row)
            # Returning a scaled matrix as a Matrix object
            return Matrix(scalar_mult_matrix)
        elif type(other) == Matrix: # If the other object is a matrix
            # Checking if dimensions of the matrices match or not
            if len(self.rowsp[0]) != len(other.rowsp):
                raise ValueError("Dimension mismatch for multiplication.")
            else: # Running the code below if the dimensions are fine
                # Array to store the product of the matrices
                product_of_matrices = []
                for i in range(len(self.rowsp)):
                    matrix_row = []
                    for j in range(len(other.rowsp)):
                        matrix_sum = 0
                        for l in range(len(other.colsp[0])):
                            self_matrix_mul = self.rowsp[i][l]
                            other_matrix_mul = other.rowsp[l][j]
                            matrix_sum += self_matrix_mul * other_matrix_mul
                        matrix_row.append(matrix_sum)
                    product_of_matrices.append(matrix_row)
                '''
                # Creating a 2D array of zeros for the product of the matrices
                for i in range(len(self.rowsp)):
                    # Storing each row in a list
                    row = []
                    # Iterating through each row
                    for j in range(len(other.rowsp[0])):
                        # Appending a zero to the row
                        row.append(0)
                    # Appending the rows to the product of matrices
                    product_of_matrices.append(row)

                # Multiplying the matrices
                for i in range(len(self.rowsp)):
                    # Iterating through each row of the other matrix
                    for j in range(len(other.rowsp[0])):
                        # Variable to store the dot product of the two rows
                        dot_product = 0
                        # Iterating through each element in the row
                        for k in range(len(other.rowsp[0])):
                            # Adding the dot product of the two rows
                            dot_product += self.rowsp[i][k] * other.rowsp[k][j]
                        # Storing the dot product in the product of matrices
                        product_of_matrices[i][j] = dot_product
                '''
                # Returning the product of matrices as a Matrix object
                return Matrix(product_of_matrices)
        elif type(other) == Vec.Vec: # If the other object is a vector
            matrix_vector_product = []
            for matrix_row in self.rowsp:
                mat_vec_product = 0
                for i in range(len(matrix_row)):
                    mat_vec_product += matrix_row[i] * Vec.Vec(other)
                matrix_vector_product.append(mat_vec_product)
            return Vec.Vec(matrix_vector_product)
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float or type(other) == int:
            return self.__mul__(other)
        else:
            print("ERROR: Unsupported Type.")
        return
    
    # Returns a formatted string representing the matrix entries as
    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rowsp:
            mat_str += str(row) + "\n"
        return mat_str
                
    def __eq__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def __req__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()
    

# %%
'''
B = Matrix([ [1, 2, 3, 4], [0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 2, 3]])
A = Matrix([ [2, 0], [0, 2], [0, 0], [0, 0]])

print("Matrix A:")
print(A)
print()

print("Matrix B:")
print(B)
'''

# %% [markdown]
# -------------------------------------------
# 
# #### Tester Cell for `get_diag()`

# %%
"""All Works
B = Matrix([ [1, 2, 3, 4], [0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 2, 3]])
print("Matrix:")
print(B)

print("Main diagonal:",B.get_diag(0))
print("Expected: [1, 1, 1, 3]")
print()
print("Diagonal at k = -1:", B.get_diag(-1))
print("Expected: [0, 0, 2]")
print()
print("Diagonal at k = -2:", B.get_diag(-2))
print("Expected: [-1, -1]")
print()
print("Diagonal at k = -3:", B.get_diag(-3))
print("Expected: [-2]")
print()
print("Diagonal at k = 1:", B.get_diag(1))
print("Expected: [2, 2, 2]")
print()
print("Diagonal at k = 2:", B.get_diag(2))
print("Expected: [3, 3]")
print()
print("Diagonal at k = 3:", B.get_diag(3))
print("Expected: [4]")
"""

# %% [markdown]
# ---------------------------
# #### Tester Cell for 
# * `row_space()`
# * `col_space()`
# * `get_row()`
# * `get_col()`
# * `set_row()`
# * `set_col()`

# %%
'''All Works
A = Matrix([[1, 2, 3], [4, 5, 6]])
print("Original Row Space:", A.row_space())
print("Original Column Space:", A.col_space())
print("Original Matrix:")
print(A)
print()


A.set_row(1, [10, 20, 30])
print("Modification #1")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_col(2, [20, 50])
print("Modification #2")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_row(2, [40, 50, 6])
print("Modification #3")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_entry(2, 3, 60)
print("Modification #4")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()


print("The 2nd row is:", A.get_row(2))
print("The 3rd column is:", A.get_col(3))
print()


print("Modification #5")
A.set_row(2, [40, 50])
A.set_col(2, [30, 4, 1])
print(A)
'''

# %% [markdown]
# **Expected Output**
# 
#     Original Row Space: [[1, 2, 3], [4, 5, 6]]
#     Original Column Space: [[1, 4], [2, 5], [3, 6]]
#     Original Matrix:
#     [1, 2, 3]
#     [4, 5, 6]
# 
# 
#     Modification #1
#     Row Space after modification: [[10, 20, 30], [4, 5, 6]]
#     Column Space after modification: [[10, 4], [20, 5], [30, 6]]
#     Modified Matrix: Set row 1 to [10, 20, 30]
#     [10, 20, 30]
#     [4, 5, 6]
# 
# 
#     Modification #2
#     Row Space after modification: [[10, 20, 30], [4, 50, 6]]
#     Column Space after modification: [[10, 4], [20, 50], [30, 6]]
#     Modified Matrix: Set col 2 to [20, 50]
#     [10, 20, 30]
#     [4, 50, 6]
# 
# 
#     Modification #3
#     Row Space after modification: [[10, 20, 30], [40, 50, 6]]
#     Column Space after modification: [[10, 40], [20, 50], [30, 6]]
#     Modified Matrix: Set row 2 to [40, 50, 6]
#     [10, 20, 30]
#     [40, 50, 6]
# 
# 
#     Modification #4
#     Row Space after modification: [[10, 20, 30], [40, 50, 60]]
#     Column Space after modification: [[10, 40], [20, 50], [30, 60]]
#     Modified Matrix: Set row 2 col 3 to 60
#     [10, 20, 30]
#     [40, 50, 60]
# 
# 
#     The 2nd row is: [40, 50, 60]
#     The 3rd column is: [30, 60]
# 
#     Modification #5
#     ---------------------------------------------------------------------------
#     ValueError                                Traceback (most recent call last)
#     ~\AppData\Local\Temp/ipykernel_9756/1966277524.py in <module>
#          48 #--------- MODIFICATION 5 ---------------#
#          49 print("Modification #5")
#     ---> 50 A.setRow(2, [40, 50])
#          51 A.setCol(2, [30, 4, 1])
#          52 print("Modified Matrix: Set row 2 to [40, 50] and col 2 to [30, 4, 1]")
# 
#     ~\AppData\Local\Temp/ipykernel_9756/2205165582.py in setRow(self, i, v)
#         159         """Sets the i-th row to be the list v"""
#         160         if len(v) != len(self.Rowsp[0]):
#     --> 161             raise ValueError("ERROR: Incompatible row length.")
#         162         else:
#         163             self.Rowsp[i-1] = v  # Updating the row
# 
#     ValueError: ERROR: Incompatible row length.`

# %% [markdown]
# ------------------------------------------------------------
# #### Tester cell for +, -, *

# %%
"""-----------------------------------TESTER CELL-------------------------------------------------
"TESTING OPERATOR + "

A = Matrix([[1, 2],[3, 4],[5, 6]])
B = Matrix([[1, 2],[1, 2]])
C = Matrix([[10, 20],[30, 40],[50, 60]])

# P = A + B # dimension mismatch --> Check successful
Q = A + C
R = A - C

print("Matrix A")           
print(A)
print()

print("Matrix C")           
print(C)
print()

'''Works'''
print("Matrix Q = A + C")         
print(Q)
print()

'''Works'''
print("Matrix R = A - C")
print(R)
print()

"TESTING OPERATOR * "
# TESTING SCALAR-MATRIX MULTIPLICATION
T = -0.5 * B     
print("Matrix B")
print(B)
print()

'''Works'''
print("Matrix T = -0.5 * B") 
print(T)
print()


# TESTING MATRIX-MATRIX MULTIPLICATION
U = A * B
print("Matrix U = A * B")
print(U)
print()


# TESTING MATRIX-VECTOR MULTIPLICATION
x = Vec([0, 1])  # Vec object
b = A * x   # b is a Vec data type
print("Vector b = A * x")
print(b) 
"""

# %% [markdown]
# $\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \cdot 0 + 2 \cdot 1 \\ 3 \cdot 0 + 4 \cdot 1 \\ 5 \cdot 0 + 6 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$

# %% [markdown]
# **Expected Output:**
# 
#     Matrix A
#     [1, 2]
#     [3, 4]
#     [5, 6]
# 
# 
#     Matrix C
#     [10, 20]
#     [30, 40]
#     [50, 60]
# 
# 
#     Matrix Q = A + C
#     [11, 22]
#     [33, 44]
#     [55, 66]
# 
# 
#     Matrix R = A - C
#     [-9, -18]
#     [-27, -36]
#     [-45, -54]
# 
# 
#     Matrix B
#     [1, 2]
#     [1, 2]
# 
# 
#     Matrix T = -0.5 * B
#     [-0.5, -1.0]
#     [-0.5, -1.0]
# 
# 
#     Matrix A:
#     [1, 2]
#     [3, 4]
#     [5, 6]
# 
# 
#     Row-space of A:
#     [[1, 2], [3, 4], [5, 6]]
# 
#     Column-space of A:
#     [[1, 3, 5], [2, 4, 6]]
# 
#     Matrix B:
#     [1, 2]
#     [1, 2]
# 
# 
#     Row-space of B:
#     [[1, 2], [1, 2]]
# 
#     Column-space of B:
#     [[1, 1], [2, 2]]
# 
#     Matrix U = A * B
#     [3, 6]
#     [7, 14]
#     [11, 22]
# 
# 
#     Vector b = A * x
#     [0, -2, -4]

# %% [markdown]
# ----------------------------------------------------------
# 
# # Extra-Credit
# 
# 
# 
# * **Worth:** 5% extra-credit applied to midterm 
# 
# * **To Receive Credit You Must:**
#     1. Submit your work on this Jupyter NB to the appropriate Dropbox folder by Sunday, 4/9 @11:59 PM
#     2. Submit your completed video to the appropriate Dropbox folder by Sunday, 4/9 @11:59 PM
#     2. Demo your work to me during OH in order to receive the extra-credit.  The last day you may demo is Thursday, 4/20.
# * **No partial credit.  This is an all-or-nothing EC opportunity**
# 
# ---------------
# 
# ***Background:***
# 
# 
# One of my favorite bands is "Alt-J".  Take a look at the music video for their song, "Matilda" at https://www.youtube.com/watch?v=Q06wFUi5OM8.  The faces you see morphing into one another are the faces of the four members who were in the band at the time.  In this exercise you will explore how a simplified version of this "morphing effect" can be achieved.  In our simplified morphing effect, we will fade one face into another.
# 
# 
# First, keep in mind that a video is just a collection of several still images displayed with a speed fast enough to make the change from one image to another imperceptible to the human eye.  
# 
# To make the discussion simpler, suppose the images are grayscale pictures.  We can represent a grayscale picture with $m \times n$ pixels as a matrix $P_{m\times n}$ where each entry $p_{ij} \in \{0, 1, \dots, 255\}$ is the intensity value of the pixel at location $(i, j)$, [*The intensity values range from 0 (black) to 255 (white)*].  We are able to prove that the set of matrices $\mathbb{S} = \{P_{m \times n} | p_{ij} \in \mathbb{Z}_{256}\}$ is a vector space, under addition and scalar multiplication defined as below:
# 
# Let $P, Q \in \mathbb{S}$, and $\alpha \in \mathbb{R}, 0 \leq \alpha \leq 1$
# 
# * Addition: $P + Q = [ a_{ij} ] \text{ where } a_{ij} = \begin{cases}
#   p_{ij} + q_{ij}  & \text{ if the sum is 255 or less} \\
#   255 & \text{ otherwise}
# \end{cases}$
# * Scalar Multiplication: $\alpha P = [ a_{ij} ] \text{ where } a_{ij} = \begin{cases}
#   \alpha p_{ij}  & \text{ if the product is 255 or less} \\
#   255 & \text{ otherwise}
# \end{cases}$
# 
# Hence, given two "image-matrices"  $P_1, P_2 \in \mathbb{S}$, we can form convex combinations of these two elements with the confidence that the resulting matrices will be in $\mathbb{S}$, and thus, still represent images; i.e., if $\alpha_1, \alpha_2 \in \mathbb{R}$ such that $\alpha_1 + \alpha_2 = 1$, then
# 
# $\alpha_1 P_1 + \alpha_2 P_2 \in \mathbb{S}$ and represents a new image.
# 
# 
# 
# Think: what would the image corresponding to matrix $P$ look like if $P = 0.5 P_1 + 0.5 P_2$?  Since the images $P_1$ and $P_2$ make an equal contribution to the intensity of each pixel in $P$, we can expect the image to look like an equal mix of the two images. e.g. if the two images contain faces in more-or-less the same position, the resulting image should display a face that more-or-less looks like both faces.  
# 
# What if $P = 0.85 P_1 + 0.15 P_2$?  Then, since most of the intensity in each pixel of $P$ is being contributed by $P_1$, we can expect the resulting image $P$ to display something that looks more like the first image, $P_1$, vs the second image, $P_2$.
# 
# 
# 

# %% [markdown]
# --------------------------------------------------------
# ***Task 1:***
# 
# 1. Download the `png` and `image` modules.  The `image` module contains the methods
#  * `file2image()` - Reads an image into a list of lists of pixel values (triples with values representing the  three intensities in the RGB color channels). e.g. `[[(1, 2, 3), (1, 2, 3), (1, 2, 3)],[(1, 2, 3), (1, 2, 3), (1, 2, 3)],[(1, 2, 3), (1, 2, 3), (1, 2, 3)]]` would be representing an image with $3\times3$ pixels.
#  * `image2file()` - Writes an image in list of lists format to a file.
#  
# 2. Use the functions listed above to implement:
#  * `img2matrix(filename)` - creates and returns a `Matrix` object with the image data returned by `file2image()` from the module `image`. The parameter `filename` is a string data type specifying the location of the image you wish to use.  If the image is not grayscale, you must convert it to grayscale prior to creating the `Matrix` object.  You can do so using the functions `isgray()` and `color2gray()`, also found in the `image` module.
#  * `matrix2img(image_matrix, path)` - creates a png file out of a `Matrix` object.  You may want to use the function `image2file()` from the `image` module.

# %%
"""
import image
import png

def image2matrix(filename):
    takes a png file and returns a Matrix object of the pixels 
    INPUT: filename - the path and filename of the png file
    OUTPUT: a Matrix object with dimensions m x n, assuming the png file has width = n and height = m, 
    # Reading the image file into a triplet list of pixel values
    image_data = image.file2image(filename)
    # Conditional statement to check if the image is grayscale
    if not image.isgray(image_data):
        image_data = image.color2gray(image_data) 
    return Matrix(image_data)


def matrix2image(img_matrix, path):
    returns a png file created using the Matrix object, img_matrix
    INPUT: 
        * img_matrix - a Matrix object where img_matrix[i][j] is the intensity of the (i,j) pixel
        * path - the location and name under which to save the created png file 
    OUTPUT: 
        * a png file
    image_data = []
    for i in range(img_matrix.nrows()):
        row = []
        for j in range(img_matrix.ncols()):
            pixel_value = int(img_matrix[i][j])
            row.append(pixel_value)
        image_data.append(row)
    image.image2file(image_data, path)
"""


# %%
"""------------------TESTER FOR FUNCTIONS png2graymatrix() AND graymatrix2png()-------------------------"""
# M = image2matrix("img11.png")  # matrix for img11.png
# F = image2matrix("img02.png")  # matrix for img02.png
# C = (0.40 * M) + (0.60 * F)   # convex combo: first image contributes 40% of its intensity, second image contributes 60%

# matrix2image(C, "mixedfaces.png")  # converting the matrix to png named mixedfaces

# %% [markdown]
# -------------------------------------------------------------------------------
# 
# ***Task 2***
# 
# 1. Download and extract the zip folder `faces.zip`.  In it, you will find the images of 20 faces.  
# 2. Use the functions you implemented in Task 1 to implement a function called `mix(img1, img2)` that generates a set of 101 images.  These images must be the result of taking convex combinations of two given images.  In particular, you should begin by combining the two images so that the 1st/101 picture looks completely like `img1`.  Then, modify the scalars of the combination so that the mixed image is the sum of a percentage of the intensities for each image.  For example, the 2nd/101 picture would be a mixture of 99% of the first image's intensity mixed with 1% of the second image's intensity.  The 51th/100 picture will look like both images equally mixed together (50/50).  The 76th picture will looks like 25% of the first image's intensity mixed with 75% of the second image's intensity, and the 101st/101 picture looks like `img2` only. 
# 3. Call your `mix()` function on two images of your choice found in the `faces.zip` folder.  The resulting images should give the illusion that one face is morphing into the other.  

# %%
"""def mix(img1, img2):
    generates a set of 101 images that results from the convex mixing the given images
    INPUT: 
        - img1: string of path + name of first image 
        - img2: string of path + name of second image 
        
    OUTPUT: None (images are saved to the path given to matrix2image())

    image1_matrix = image2matrix(img1)
    image2_matrix = image2matrix(img2)

    for i in range(101):
        percentage_1 = (100 - i) / 100
        percentage_2 = i / 100

        mixed_image_matrix = (Matrix(image1_matrix) * percentage_1) + (Matrix(image2_matrix) * percentage_2)

        file_path = f"mixed_image/{i}.png"
        matrix2image(mixed_image_matrix, file_path)
"""

# %% [markdown]
# ---------------------------
# ***Task 3***
# 
# Use the function `make_video()` below to create a video out of the 101 images you generated in Task 2.  You will need to have installed the package `opencv` in order for the function to work.  I recommend that you complete this entire task in a separate IDE such as PyCharm, where it is easier to install packages.
# 

# %%
# import cv2
# import os

"""def make_video(images, outvid=None, fps=5, size=None, is_color=True, format="XVID"):
    Create a video from a list of images.

    @param      outvid      output video
    @param      images      list of images to use in the video
    @param      fps         frame per second
    @param      size        size of each frame
    @param      is_color    color
    @param      format      see http://www.fourcc.org/codecs.php
    @return                 see http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

    By default, the video will have the size of the first image.
    It will resize every image to this size before adding them to the video.

    fourcc = cv2.VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = cv2.imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = cv2.VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = cv2.resize(img, size)
        vid.write(img)
    vid.release()
    return vid
"""


# %% [markdown]
# **Sample Usage:**
# 
#     img_path = "C:\\Users\\kapiv\\Documents\\CECS 229\\CA #5\\faces\\"
#     vid_path = "C:\\Users\\kapiv\\Documents\\CECS 229\\CA #5\\male_faces.avi"
# 
#     images = []  # Initializing empty list of image paths
#     for i in range(15):  # adding images male00.png - male14.png to the list
#         if i < 10:
#             file = f"{img_path}male0{i}.png"
#         else:
#             file = f"{img_path}male{i}.png"
#         print("Adding:", file)
#         images.append(file)
# 
# 
#     make_video(images, vid_path, format = "mp4v")  # creating video

# %%



