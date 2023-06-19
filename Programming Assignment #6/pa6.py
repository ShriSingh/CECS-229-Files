# %% [markdown]
# # CECS 229 Programming Assignment #6
# 
# #### Due Date: 
# 
# Sunday, 4/30 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost a Python script named `pa6.py` with your work by the due date.
# 
# #### Objectives:
# 
# 1. Apply Gaussian Elimination to solve the system $A \overrightarrow{x} = \overrightarrow{b}$.
# 2. Use Lp -norm to calculate the error in a solution given by applying Gaussian elimination.
# 3. Use the REF of the augmented matrix for the system $A \overrightarrow{x} = \overrightarrow{b}$ to determine if it has one solution, no solution, or infinitely-many solutions.
# 4. Determine the number of free variables that the system $A \overrightarrow{x} = \overrightarrow{b}$ has if it has infinitely-many solutions.
# 5. Determine whether a set of column-vectors is linearly dependent by forming and solving a system of the form $A \overrightarrow{x} = \overrightarrow{0}$.
# -----------------------------------------
# 
# 

# %% [markdown]
# #### Problem 1
# 
# Copy-paste your implemented `Matrix` and `Vec` classes to the next cell.  Then, complete the following tasks:
# 
# 1. Add a method `norm(self, p)` to your `Vec` class so that if `u` is a `Vec` object, then `u.norm(p)` returns the $L_p$-norm of vector `u`.  Recall that the $L_p$-norm of an $n$-dimensional vector $\overrightarrow{u}$ is given by, $||u||_p = \left( \sum_{i = 1}^{n} |u_i|^p\right)^{1/p}$.  Input `p` should be of the type `int`.  The output norm should be of the type `float`.
# 2. Add a method `ref(self)` that applies Gaussian Elimination to create and return the Row Echelon Form of the current matrix.  The output must be of the type `Matrix`.  The method should ***NOT*** modify the contents of `self.rowsp` or `self.colsp`.  It should create and return a new `Matrix` object.
# 3. Add a method `rank(self)` to your `Matrix` class so that if `A` is a `Matrix` object, then `A.rank()` returns the rank of `A`.

# %%
import math
 
# Putting up Vector class from the previous assignment
class Vec:
    def __init__(self, contents=[]):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return
 
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        # Variable to store the magnitude of the vector
        magnitude_vector = 0
        # Variable to store the sum of the squares of the elements in the vector
        vector_squares = []
        # Running through all the elements in the vector
        for element in self.elements:
            # Squaring the elements of the vector
            sum_of_squares = element ** 2
            # Appending the sum of the squares to the list
            vector_squares.append(sum_of_squares)
 
        # Square root of the sum of the squares of the elements in the vector
        magnitude_vector = math.sqrt(sum(vector_squares))
 
        return magnitude_vector  # Returning the magnitude of the vector
 
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
        raises ValueError if vectors are not same length
        """
        # Conditional Statement to check whether vectors are of same length
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be same length")
        else:  # Run the following code once the condition is satisfied
            # Variable to store the sum of the vectors
            vector_sum = []
            # Running through all the elements in the vector
            for element in range(len(self.elements)):
                # Adding the elements of the vectors together
                sum_result = self.elements[element] + other.elements[element]
                # Appending the sum of the elements to the list
                vector_sum.append(sum_result)
 
        # Converting the list to a vector
        vector_sum = Vec(vector_sum)
 
        return vector_sum  # Returning the sum of the vectors
 
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        # Conditional Statement to check whether vectors are of same length
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be same length")
        else:  # Run the following code once the condition is satisfied
            # Variable to store the difference of the vectors
            vector_difference = []
            # Running through all the elements in the vector
            for element in range(len(self.elements)):
                # Subtracting the elements of the vectors together
                difference_result = self.elements[element] - other.elements[element]
                # Appending the difference of the elements to the list
                vector_difference.append(difference_result)
 
        # Converting the list to a vector
        vector_difference = Vec(vector_difference)
 
        return vector_difference  # Returning the difference of the vectors
 
    def __mul__(self, other):
        """Overloads the * operator to support
        - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
        - Vec * float (component-wise product)
        - Vec * int (component-wise product)
        """
        if type(other) == Vec:  # define dot product
            # Conditional Statement to check whether vectors are of same length
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must be same length")
            else:  # Run the following code once the condition is satisfied
                # Variable to store the dot product of the vectors
                dot_product = 0
                # Running through all the elements in the vector
                for element in range(len(self.elements)):
                    # Multiplying the elements of the vectors each other
                    product_result = self.elements[element] * other.elements[element]
                    # Adding the product of the elements to the variable
                    dot_product += product_result
 
                return dot_product  # Returning the dot product
        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            # Variable to store the result of scalar-vector multiplication
            vector_product = []
            # Running a loop through all the elements in the vector
            for element in range(len(self.elements)):
                # Multiplying the each elements in the vector to the scalar value
                product_result = self.elements[element] * other
                # Appending the product of the elements to the list
                vector_product.append(product_result)
 
            # Converting the list to a vector
            vector_product = Vec(vector_product)
 
            return vector_product  # Returning the scalar-vector multiplication
 
    def __rmul__(self, other):
        """
        Overloads the * operation to support
            - float * Vec
            - int * Vec
        """
        # Variable to store another version of scalar-vector multiplication
        vector_product = []
        # Running a loop through all the elements in the vector
        for element in range(len(self.elements)):
            # Multiplying the each elements in the vector to the scalar value
            product_result = self.elements[element] * other
            # Appending the product of the elements to the list
            vector_product.append(product_result)
 
        # Converting the list to a vector
        vector_product = Vec(vector_product)
 
        return vector_product  # Returning the scalar-vector multiplication
 
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)  # does NOT need further implementation
    
    """Implementing norm(self, p) method"""
    # Writing a method that returns the Lp-norm of the vector
    def norm(self, p: int):
        # Storing the result of sum of powers
        sum_of_powers = 0
        # Iterating through each element in the vector
        for element in self.elements:
            # Adding the sum of the powers of each element
            sum_of_powers += abs(element) ** p # -> Summation of |x_i|^p
        # Sotring the final result
        lp_norm = sum_of_powers ** (1/p) # -> (Summation of |x_i|^p)^(1/p)
        # Returning the final result
        return lp_norm
            
            
# Putting up Matrix class from the previous assignment
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
            # Iterating through the row spaces
            for i in range(len(self.rowsp)):
                # Storing each reduced row in a list
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
            # Iterating through the row spaces
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
            for final_matrix_row in self.rowsp:
                # Storing the each scaled row in a list
                scaled_row = []
                # Going through each element in the row
                for element in final_matrix_row:
                    scaled_element = element * other # Mulitplying each element with the scalar value
                    scaled_row.append(scaled_element) # Appending the scaled product into the scaled row
                # Appending the scaled rows to the scaled matrix
                scalar_mult_matrix.append(scaled_row)
            return Matrix(scalar_mult_matrix) # Returning a scaled matrix as a Matrix object
        elif type(other) == Matrix: # --> If the other object is a matrix
            # Checking if dimensions of the matrices match or not
            if len(self.rowsp[0]) != len(other.rowsp):
                raise ValueError("Dimension mismatch for multiplication.")
            else: 
                # Array to store the product of the matrices
                product_of_matrices = []
                # Iterating through the rows of the first matrix
                for num in range(len(self.rowsp)):
                    # Storing the product of each row of the first matrix with the columns of the second matrix
                    final_matrix_row = []
                    # Iterating through the columns of the other matrix
                    for column in range(len(other.colsp)):
                        # Storing the sum of the product of each row 
                        matrix_sum = 0
                        # Iterating through the first index of the other matrix's column
                        for l in range(len(other.colsp[0])):
                            self_matrix_mul = self.rowsp[num][l] # Storing the multiplication of first matrix
                            other_matrix_mul = other.rowsp[l][column] # Storing the multiplication of the second matrix
                            matrix_sum += self_matrix_mul * other_matrix_mul # Adding the products of the two matrices' rows
                        # Appending the matrix sum to final matrix row
                        final_matrix_row.append(matrix_sum)
                    # Appending the final matrix rows to the final matrix product
                    product_of_matrices.append(final_matrix_row)
                return Matrix(product_of_matrices) # Returning the product of matrices as a Matrix object
        elif type(other) == Vec: # If the other object is a vector 
            # Storing the product of matrix-vector in a list
            matrix_vector_product = []
            # Iterating through the rows of the matrix
            for matrix_row in range(len(self.rowsp)):
                # Storing the sum of the product of each row
                mat_vec_product = 0
                # Iterating through each number in the matrix row
                for num in range(len(self.rowsp[matrix_row])):
                    # Adding the products of the matrix row and the vector
                    mat_vec_product += self.rowsp[matrix_row][num] * other.elements[num]
                matrix_vector_product.append(mat_vec_product) # Appending the matrix-vector product to the list
            return Vec(matrix_vector_product) # Returning the matrix-vector product as a Vec object
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
    
    """Implementing ref(self) method"""
    # Writing a method that returns the reduced row echelon form of the matrix
    def ref(self):
        # Creating a copy of the matrix 
        matrix_copy = []
        # Iterating through each row in the matrix
        for row in self.rowsp:
            # An temporary list to store the elements of the row
            new_row = []
            # Iterating through each element in the row
            for element in row:
                # Appending the element to the new row
                new_row.append(element)
            # Appending the new row to the matrix copy variable
            matrix_copy.append(new_row)

        # Storing the total number of rows and columns in the matrix
        num_rows = len(matrix_copy)
        num_cols = len(matrix_copy[0])

        # Making non-square matrices square by adding zero rows or columns as needed
        if num_rows != num_cols:
            # Checks if the number of rows < the number of columns
            if num_rows < num_cols:
                # Iterating through the number of columns - number of rows
                for i in range(num_cols, num_rows):
                    # Creating a zero row
                    zero_row = [0] * num_cols
                    # Appending the zero row to the matrix copy
                    matrix_copy.append(zero_row)
            else: # --> If the number of rows > the number of columns
                # Iterating through the number of rows - number of columns
                for i in range(num_cols, num_rows):
                    # Creating a zero column
                    zero_col = [0] * num_rows
                    # Iterating through the number of rows
                    for j in range(num_rows):
                        # Appending the zero column to the matrix copy
                        matrix_copy[j].append(zero_col[j])

        # Creating a variable to store the pivot column
        row_pivot = 0

        # Iterating through each column in the matrix
        for j in range(num_cols):
            # Finding the 1st non-zero entry in the j-th column below the pivot row
            for i in range(row_pivot, num_rows):
                # Checking if the entry is non-zero
                if matrix_copy[i][j] != 0:
                    # Swapping the rows if the entry is zero
                    matrix_copy[row_pivot], matrix_copy[i] = matrix_copy[i], matrix_copy[row_pivot]
                    break
            # Making of all the entries bwlow the pivot row zero
            for i in range(row_pivot + 1, num_rows):
                # Checking if the entry is non-zero
                if matrix_copy[i][j] != 0:
                    # Creating a variable to store the factor value
                    factor = matrix_copy[i][j] / matrix_copy[row_pivot][j]
                    # Iterating through each element in the row
                    # Alternative -> matrix_copy[i] = [matrix_copy[i][k] - scalar * matrix_copy[row_pivot][k] for k in range(num_cols)]
                    new_row = []
                    for k in range(num_cols):
                        new_element = matrix_copy[i][k] - (factor * matrix_copy[row_pivot][k])
                        new_row.append(new_element)
                    # Replacing the row with the new row
                    matrix_copy[i] = new_row
            # Moving to the next pivot row
            row_pivot += 1
            # Checking if the pivot row is the last row
            if row_pivot == num_rows:
                break
        # Returning the reduced row echelon form of a matrix
        return Matrix(matrix_copy)        

    """Implementing rank(self) method"""
    # Writing the method that returns the rank of the matrix
    def rank(self):
        # Converting input Matrix into reduced row echelon form
        ref_matrix = self.ref()
        # Creating a variable to store the rank of the matrix
        rank = 0
        # Storing total number of non-zero rows and columns in the matrix
        non_zero_rows = 0
        non_zero_cols = 0
        # Writing non_zero_rows = sum([any(row) for row in ref_matrix.rowsp]) in a different way
        # Iterating through each row in the matrix
        for row in ref_matrix.rowsp:
            # Checking if the row has any non-zero entries
            if any(row):
                # Incrementing the non_zero_rows variable
                non_zero_rows += 1
        # Writing non_zero_cols = sum([any(col) for col in ref_matrix.colsp]) in a different way
        # Iterating through each column in the matrix
        for col in ref_matrix.colsp:
            # Checking if the column has any non-zero entries
            if any(col):
                # Incrementing the non_zero_cols variable
                non_zero_cols += 1
        
        # Checking if the number of non-zero rows > the number of non-zero columns
        if non_zero_rows < non_zero_cols:
            rank = non_zero_rows
        elif non_zero_rows > non_zero_cols: # --> If the number of non-zero rows > the number of non-zero columns
            rank = non_zero_cols
        else:
            rank = non_zero_rows
        
        # Returning the rank of the matrix
        return rank
        


# %%
'''
m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = Matrix([[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]])
o = Matrix([[1, 2], [3, 4]])
p = Matrix([[-24, 60, 56, -28, 24, 80], [-6, 15, 14, -7, 6, 20], [-36, 20, 24, 36, -8, -34], [-16, 9, -5, -2, -9, 9], [-18, 10, 12, 18, -4, -17]])
q = Matrix([[13, -8, -13, 1, -19, 1, 7], [11, 6, -109, 122, 26, 125, -3], [11, 17, 10, -9, -9, -6, -11], [11, -1, 18, -18, -9, -8, 18], [16, 7, 6, 7, 15, -4, 19], [0, -1, 13, -20, -5, -19, 3], [14, -7, -15, -10, 6, -18, 13]])

print(m.ref())
# Output: [[1, 2, 3], [0, -3, -6], [0, 0, 0]]
print(n.ref())
# Output: [[1, 3, 5, 9], [0, -9, -11, -29], [0, 0, -4, -2], [0, 0, 0, 94/9]]
print(o.ref())
# Output: [[1, 2], [0, -2]]
print(p.ref())
# Output: [[1, 0, 0, 0, 0.638066, -1.64437], [0, 1, 0, 0, 0.3287, -1.74054], [0, 0, 1, 0, 0.3498, 1.33333], [0, 0, 0, 1, 0, -2.510744], [0, 0, 0, 0, 0, 0]]
print(q.ref())
'''

# %%
"""RANK TESTER CELL
A = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(A)
print("Rank:", A.rank(), "\nExpected: 2\n")

B = Matrix([[1, 2], [-1, -2]])
print(B)
print("Rank:", B.rank(), "\nExpected: 1\n")

C = Matrix([[0, -1, 5], [2, 4, -6], [1, 1, 5]])
print(C)
print("Rank:", C.rank(), "\nExpected: 3\n")

D = Matrix([[5, 3, 0], [1, 2, -4], [-2, -4, 8]])
print(D)
print("Rank:", D.rank(), "\nExpected: 2\n")

E = Matrix([[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]])
print(E)
print("Rank:", E.rank(), "\nExpected: 2")
"""

# %% [markdown]
# #### Problem 2
# 
# Implement the function `gauss_solve(A, b)` that solves the system $A \overrightarrow{x} = \overrightarrow{b}$.  The input `A` is of the type `Matrix` and `b` is of the type `Vec`.
#    - If the system has a unique solution, it returns the solution as a `Vec` object.  
#    - If the system has no solution, it returns `None`. 
#    - If the system has infinitely many solutions, it returns the number of free variables (`int`) in the solution.

# %%
# Writing the gauss_solve(A, b) function to solve the system of linear equations
def gauss_solve(A, b):
    # Iterating through the rows of the matrix
    for i in range(len(A.rowsp)):
        # Appending the vector b to the matrix
        A.rowsp[i].append(b.elements[i])
    
    # Converting the augmented matrix into reduced row echelon form
    row_echelon_matrix = A.ref()

    # Checking if the system of linear equations has no solution
    for i in range(len(row_echelon_matrix.rowsp)):
        all_zeroes = all([x == 0 for x in row_echelon_matrix.rowsp[i][:-1]])
        # Checking if the last entry in the row is not zero
        if row_echelon_matrix.rowsp[i][-1] != 0:
            # Returning None if the system of linear equations has no solution
            return None
        
    # Checking if the system of linear equations has infinite solutions
    num_free_vars = 0
    for i in range(len(row_echelon_matrix.rowsp)):
        all_zeroes = all([x == 0 for x in row_echelon_matrix.rowsp[i][:-1]])
        # Checking if the last entry in the row is zero
        if all_zeroes and row_echelon_matrix.rowsp[i][-1] == 0:
                num_free_vars += 1

    if num_free_vars > 0:
        # Returning the free variables for infinite solutions
        return num_free_vars
    
    # Back-substitution 
    solution = [0] * len(A.rowsp)
    for i in range(len(A.rowsp) - 1, -1, -1):
        pivot_row_index = None
        for j in range(len(row_echelon_matrix.rowsp)):
            if row_echelon_matrix.rowsp[j][i] != 0:
                pivot_row_index = j
                break
        if pivot_row_index is not None:
            solution[i] -= row_echelon_matrix.rowsp[pivot_row_index][-1]
            for j in range(i + 1, len(A.colsp)):
                solution[i] -= row_echelon_matrix.rowsp[i][i]  * solution[j]
            solution[i] /= row_echelon_matrix.rowsp[pivot_row_index][i]
        else:
            solution[i] = 0
    
    # Returning the solution as a Vector
    return Vec(solution)


# %%
"""TESTER CELL #1 FOR GAUSSIAN ELIMINATION
A = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
b = Vec([9, 10, 11])
sol = gauss_solve(A, b)
print("Result:", sol)
print("Expected: 1")
"""

# %%
"""TESTER CELL #2 FOR GAUSSIAN ELIMINATION
A = Matrix([[1, 0, 5], [0, 1, 2], [3, 2, 0]])
b = Vec([6, 3, 5])
sol = gauss_solve(A, b)
print("Returned:", sol)
print("Expected: [1.0, 1.0, 1.0]")
"""

# %%
"""TESTER CELL #3 FOR GAUSSIAN ELIMINATION
A = Matrix([[1, 1, 5], [2, 2, 10]])
b = Vec([6, 3])
sol = gauss_solve(A, b)
print("Returned:", sol)
print("Expected: None")
"""

# %% [markdown]
# 
# ------------------------------------------------
# 
# #### Problem 3
# 
# Implement the function `is_independent(S)` that returns `True` if the set `S` of `Vec` objects is linearly **independent**, otherwise returns `False`.

# %%
# Writing a function that returns true/false based on whether 
# the given set of vectors is linearly independent or not
def is_independent(S):
    # Two arrays for storing the matrix and vector
    A = []
    B = []
    # Iterating through the vector space
    for x in S:
        # Storing the elements of the matrix
        A_new = []
        # Iterating through the elements of the vector
        for y in range(len(x.elements)):
            # Appending the elements of the vector to the matrix
            A_new.append(x.elements[y])
        # Appending the elements of the vector to the matrix
        B.append(0)
        # Appending the matrix to the list
        A.append(A_new)

    # Converting the matrix and vector into Matrix and Vec objects
    A_matrix = Matrix(A)
    B_vector = Vec(B)

    # Running the gauss_solve() function to solve the system of linear equations
    gauss_solution = gauss_solve(A_matrix, B_vector)

    # Checking if the system of linear equations has no solution
    if type(gauss_solution) == Vec:
        # Iterating through the elements of the vector
        for i in gauss_solution.elements:
            # Checking if the element is not zero
            if i != 0:
                break
            # Returning true, indicating that the vectors are linearly independent
            return True
    # Returning false, indicating that the vectors are linearly dependent
    return False

# %%
"""IS-INDEPENDENT TESTER CELL

S1 = {Vec([1, 2]), Vec([2, 3]), Vec([3, 4])}

print("S1 is Independent:", is_independent(S1))
print("Expected: False")

S2 = {Vec([1, 1, 1]), Vec([1, 2, 3]), Vec([1, 3, 6])}

print("S2 is Independent:", is_independent(S2))
print("Expected: True")
"""

# %% [markdown]
# #### Problem 4
# 
# Implement the function `gram_schmidt(S)` that applies the Gram-Schmidt process to create an orthonormal set of vectors from the vectors in `S`.  The function raises a `ValueError` if the set `S` is NOT linearly independent.
# 
# INPUT:
#  - `S` a set of `Vec` objects
# 
# OUTPUT:
#  - a set of `Vec` objects representing orthonormal vectors.
#  
# HINT:  
# 
# If $S = \{\overrightarrow{x_1}, \overrightarrow{x_2}, \dots ,\overrightarrow{x_n}\}$ is a set of linearly independent vectors, then Gram-Schmidt process returns the set $\{\overrightarrow{u_1}, \overrightarrow{u_2}, \dots ,\overrightarrow{u_n}\}$
# where,
# - $\overrightarrow{u_i} = \frac{1}{||\overrightarrow{w_i}||_2}\overrightarrow{w_i} \hspace{1cm}$ for $i = 1, 2, \dots n$, 
# 
# and
# 
# - $\overrightarrow{w_1} = \overrightarrow{x_1}$
# - $\overrightarrow{w_i} = \overrightarrow{x_i} - \sum_{j = 1}^{i-1} proj_{\overrightarrow{w_j}}(\overrightarrow{x_i}) \hspace{1cm} $ for $i = 2, 3, \dots n$ 

# %%
'''
def gram_schmidt(S):
    if is_independent(S) == False:
        raise ValueError("The vectors in S are not linearly independent.")
    else:
        # Finding the dimensions of the vector space
        n, k = len(S), len(S[0])
        # Creating a list 0-filled array based on dimensions of S
        U = [[0 for _ in range(k)] for _ in range(n)]
        # Normalizing the first column of S and storing it in U
        U[:, 0] = S[:, 0] / Vec(S[:, 0]).norm(2)

        # Iterating through the columns of S
        for i in range(1, k):
            U[:, i] = S[:, i]
            # Iterating through the columns of U
            for j in range(i):
                
            
    # Returning the orthonormal basis of S
    return U
'''

# %%
"""TESTER CELL #1 FOR GRAM SCHMIDT
S = {Vec(1, -1), Vec(0, 2)}
T = gram_schmidt(S)

str_T = "{"
for v in T:
    str_T += str(v) + 'T '
str_T += "}"

print(strT)
print("Expected: {[0.707106, -0.707106]T, [0.707106, 0.707106]T}")
"""

# %%
"""TESTER CELL #2 FOR GRAM SCHMIDT
S = {Vec(1, -2), Vec(-4, 8)}
try:
    T = gram_schmidt(S)
    print("INCORRECT: ValueError was not raised.")
except ValueError:
    print("CORRECT: ValueError was raised.")
except:
    error = traceback.format_exc()
    print("INCORRECT: The following unexpected error occurred:\n\n" + str(error))
"""


