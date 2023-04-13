# %% [markdown]
# # CECS 229 Programming Assignment #4
# 
# #### Due Date: 
# 
# Sunday, 3/19 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment, you must submit to CodePost this file converted to a Python script named `pa4.py`
# 
# #### Objectives:
# 
# 1. Apply vector operations to translate, scale, and rotate a set of points representing an image.
# 2. Perform various operations with or on vectors: addition, subtraction, dot product, norm.
# 
# 
# --------------------------------------------------------
# 
# #### Needed Import Statements

# %%
# MAKE SURE TO RUN THIS CELL BEFORE RUNNING ANY TESTER CELLS
"""
In order for the import statements below to work, you must download and save 
the plotting.py and image.py files to the same folder where this file is located.
""" 
import cmath
import math
from plotting import plot
import image

# %% [markdown]
# #### Problem 1:
# 
# Create a function `translate(S, z0)` that translates the points in the input set $S$ by $z_0 = a_0 + b_0 i$.  The function should satisfy the following:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `z0` - complex number
# 2. OUTPUT:
#     * a set consisting of points in S translated by $z_0$

# %%
# Writing a function to translate a set of complex numbers in the form of z_0 = a_0 + b_0i 
def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * a set consisting of points in S translated by z0
    """
    # Checks if the input 'z0' is a complex number
    if type(z0) != complex:
        raise TypeError("the 'z0' input has to a complex number")
    else: # Runs the code below once the basic requirements are met
        # Creating a list to store the translated complex numbers
        complex_number_list = []
        # Iterating through the set 'S'
        for i in S:
            # "Translating" each complex number in the set 'S' by 'z0' thru addition
            translation_sum = i + z0
            # Appending the translated complex number to the list
            complex_number_list.append(translation_sum)

        # Converting the list to a set
        translated_set = set(complex_number_list)

    return translated_set # Returning the translated set

# %%
"""
TESTER CELL #1 FOR translate()
"""
'''
S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}


print("ORIGINAL VALUES:", S)

plot([(S, 'black')], 10, title = "Original Values") # original values will be plotted in black

T1 = translate(S, -3-2j)  # values translated by -3-2i will be plotted in red
T2 = translate(S, 3-2j)   # values translated by 3-2i will be plotted in green
T3 = translate(S, -3+2j)  # values translated by -3+2i will be plotted in orange
T4 = translate(S, 3+2j)   # values translated by 3+2i will be plotted in blue

print("SHIFT LEFT 3, DOWN 2:", T1)
print("Expected: {0j, (-0.25-1j), (-1+0j), -1j, (-1-1j), (-1.25-1j), (-0.75-1j), (0.25-1j), (-0.5-1j)}\n")
print("\nSHIFT RIGHT 3, DOWN 2:", T2)
print("Expected: {(6-1j), (6.25-1j), (5+0j), (6+0j), (5-1j), (5.75-1j), (5.5-1j), (4.75-1j), (5.25-1j)}\n")
print("\nSHIFT LEFT 3, UP 2:", T3)
print("Expected: {(-1+3j), (-1.25+3j), (-0.75+3j), (-1+4j), (-0.5+3j), 4j, (-0.25+3j), 3j, (0.25+3j)}\n")
print("\nSHIFT RIGHT 3, UP 2:", T4)
print("Expected: {(4.75+3j), (5.5+3j), (5.25+3j), (5+3j), (5+4j), (6+4j), (5.75+3j), (6+3j), (6.25+3j)}\n")

# plotting original values against translated values
plot([(S, 'black'), (T1, 'red'), (T2, 'green'), (T3, 'orange'), (T4, 'blue')], 10, title = "Original + Shifted Values")
'''

# %%
"""
TESTER CELL #2 FOR translate()
"""
'''
img = image.file2image('img01.png')
gray_img = image.color2gray(img)
complex_img = image.gray2complex(gray_img)
translated_img = translate(complex_img, -200 + 0j)
plot([(complex_img, 'black')], 200, title = "Original Image")
plot([(translated_img, 'black')], 200, title = "Translated Image")
'''

# %% [markdown]
# ------------
# 
# #### Problem 2:
# 
# Create a function `scale(S, k)` that scales the points in the input set $S$ by a factor of $k$:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `k` - positive float, raises ValueError if k $\leq$ 0.
# 2. OUTPUT:
#     * a set consisting of points in S scaled by $k$.

# %%
# Writing a function to scale a set of complex numbers in the form of z_0 = a_0 + b_0i
def scale(S, k: float):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    # Conditional statement to check if k is a positive float
    if k <= 0:
        raise ValueError("K is less than or equal to 0; K has to be greater than 0")
    else: # Runs the following code once the basic requirements are met
        # Creating a list to store the scaled complex numbers
        complex_number_list = []
        # Iterating through the set 'S'
        for i in S:
            # "Scaling" each complex number in the set 'S' by 'k' thru multiplication
            scaled_number = i * k
            # Appending the scaled complex number to the list
            complex_number_list.append(scaled_number)
        
        # Converting the list to a set
        scaled_set = set(complex_number_list)

    return scaled_set # Returning the scaled set

# %%
"""
TESTER CELL #1 FOR scale()
"""
'''
S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
T1 = translate(S, -3-2j)  # values translated by -3-2i will be plotted in red
T2 = translate(S, 3-2j)   # values translated by 3-2i will be plotted in green
T3 = translate(S, -3+2j)  # values translated by -3+2i will be plotted in orange
T4 = translate(S, 3+2j)   # values translated by 3+2i will be plotted in blue
sets = [S, T1, T2, T3, T4]
scaled_sets = [scale(A, 2) for A in sets]
for i in range(len(scaled_sets)):
    print("Original Set:", sets[i])
    print("After Scaling by 2:", scaled_sets[i], "\n")

plot([(S, 'black')], 10, title = "Original Values")
plot_data = list(zip(scaled_sets, ['black', 'red', 'green', 'orange', 'blue']))
plot(plot_data, 10, title = "Scaled by 2") #second parameter affects window size
'''

# %%
"""
TESTER CELL #2 FOR scale()
"""
'''
img = image.file2image('img01.png')
gray_img = image.color2gray(img)
complex_img = image.gray2complex(gray_img)
scaled_img = scale(complex_img, 1.5)
plot([(complex_img, 'black')], 200, title = "Original Image")
plot([(scaled_img, 'black')], 200, title = "Image Scaled 1.5x")
'''

# %% [markdown]
# -----------------------------------
# 
# #### Problem 3:
# 
# Create a function `rotate(S, theta)` that rotates the points in the input set $S$ by $\theta$ radians:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `theta` - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
# 2. OUT:
#     * a set consisting of points in S rotated by $\theta$

# %%
# Writing a function that rotates a set of complex numbers by 'theta' radians
def rotate(S, theta: float):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * a set consisting of points in S rotated by theta radians
        
    """
    # Creating a list to store the rotated complex numbers
    complex_number_list = [] 
    # Conditional statement to lead outcomes based on the value of 'theta'
    if theta < 0 or theta > 0: # if theta is negative/positive, the rotation is clockwise/counterclockwise
        # Going through each complex number in the set 'S'
        for i in S:
            # Finding the polar form of each complex number in the set 'S'
            i = abs(i) * cmath.exp((cmath.phase(i)) * 1j) # i = r * e^(θj), where r = abs(i) and θ = cmath.phase(i)
            # Rotating each complex number in the set 'S' by 'theta' radians
            rotated_complex_number = i * cmath.exp(theta * 1j) # rotated_number = i * e^(θj), where θ = theta(number of radians to rotate by)
            # Rounding the real and imaginary parts of the rotated complex number to five decimal places
            rotated_complex_number = round(rotated_complex_number.real, 5) + round(rotated_complex_number.imag, 5) * 1j
            # Appending the rotated complex number to the list
            complex_number_list.append(rotated_complex_number)
    else: # If theta is zero, no rotation is done
        # Going through each complex number in the set 'S'
        for i in S:
            # Appending the complex number to the list as it is
            complex_number_list.append(i)
    
    # Converting the list to a set
    rotated_set = set(complex_number_list)

    return rotated_set # Returning the rotated set

# %%
"""
TESTER CELL #1 FOR rotate()
"""
'''
S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
T1 = translate(S, -3-2j)  # values translated by -3-2i will be plotted in red
T2 = translate(S, 3-2j)   # values translated by 3-2i will be plotted in green
T3 = translate(S, -3+2j)  # values translated by -3+2i will be plotted in orange
T4 = translate(S, 3+2j)   # values translated by 3+2i will be plotted in blue
sets = [S, T1, T2, T3, T4]

rotated_sets = [rotate(A, math.pi/2) for A in sets]
for i in range(len(rotated_sets)):
    print("Original Set:", sets[i])
    print("After Scaling by 2:", rotated_sets[i], "\n")

plot_data_rot = list(zip(rotated_sets, ['black', 'red', 'green', 'orange', 'blue']))
plot(plot_data_rot, 10, title = "Rotated by 90 degrees") #second parameter affects window size

rotated_sets_2 = [rotate(A, -1*math.pi/2) for A in sets]
for i in range(len(rotated_sets_2)):
    print("Original Set:", sets[i])
    print("After Scaling by 2:", rotated_sets_2[i], "\n")
    

plot([(S, 'black'), (T1, 'red'), (T2, 'green'), (T3, 'orange'), (T4, 'blue')], 10, title = "Original Values")

plot_data_rot_2 = list(zip(rotated_sets_2, ['black', 'red', 'green', 'orange', 'blue']))
plot(plot_data_rot_2, 10, title = "Rotated by -90 degrees") #second parameter affects window size
'''

# %%
"""
TESTER CELL #2 FOR rotate()
"""
'''
img = image.file2image('img01.png')
gray_img = image.color2gray(img)
complex_img = image.gray2complex(gray_img)
rotated_img = rotate(complex_img, -1 * math.pi/2)
plot([(complex_img, 'black')], 200, title = "Original Image")
plot([(rotated_img, 'black')], 200, title = "Image Rotated by -90 degrees")
'''

# %%
"""
Full image transformation = rotation + scaling + translation
"""
'''
img = image.file2image('img01.png')
gray_img = image.color2gray(img)
complex_img = image.gray2complex(gray_img)

rotated_img = rotate(complex_img, -1*math.pi/2)
scaled_img = scale(rotated_img, 1.5)
translated_img = translate(scaled_img, -125 + 150j)

plot([(complex_img, 'black')], 200, title = "Original Image")
plot([(translated_img, 'black')], 200, title = "Transformed Image")
'''


# %% [markdown]
# --------------------
# #### Problem 4:
# 
# Finish the implementation of class `Vec` which instantiates row-vector objects with defined operations of addition, subtraction, scalar multiplication, and dot product.  In addition, `Vec` class overloads the Python built-in function `abs()` so that when it is called on a `Vec` object, it returns the Euclidean norm of the vector.
# 
# 
# 

# %%
class Vec:
    def __init__(self, contents = []):
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

        return magnitude_vector # Returning the magnitude of the vector
        

    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        # Conditional Statement to check whether vectors are of same length
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be same length")
        else: # Run the following code once the condition is satisfied
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

        return vector_sum # Returning the sum of the vectors
    

    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        # Conditional Statement to check whether vectors are of same length
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be same length")
        else: # Run the following code once the condition is satisfied
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

        return vector_difference # Returning the difference of the vectors
    

    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            # Conditional Statement to check whether vectors are of same length
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must be same length")
            else: # Run the following code once the condition is satisfied
                # Variable to store the dot product of the vectors
                dot_product = 0
                # Running through all the elements in the vector
                for element in range(len(self.elements)):
                    # Multiplying the elements of the vectors each other
                    product_result = self.elements[element] * other.elements[element]
                    # Adding the product of the elements to the variable
                    dot_product += product_result
                
                return dot_product # Returning the dot product
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
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

            return vector_product # Returning the scalar-vector multiplication


    def __rmul__(self, other):
        """Overloads the * operation to support 
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

        return vector_product # Returning the scalar-vector multiplication
    
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation

# %%
"""----------------------TESTER CELL----------------------"""
'''
u = Vec([1, 2, 3])
w = Vec([0, 1, -1])
v = Vec([0, -3])
print("u = ", u)
print("w = ", w)
print("\nEuclidean norm of u:", abs(u))
print("Expected:", math.sqrt(sum([ui**2 for ui in u.elements])))
print("\nEuclidean norm of v:", abs(v))
print("Expected: 3.0")
print("\nu left scalar multiplication by 2:", 2*u)
print("Expected: [2, 4, 6]")
print("\nw right scalar multiplication by -1:", w * -1)
print("Expected: [0, -1, 1]")
print("\nVector addition:", u + w)
print("Expected: [1, 3, 2]")
print("\nVector addition:", u - w)
print("Expected: [1, 1, 4]")
print("\nDot product:", w*u)
print("Expected: -1")
'''

'''
try:
    print("\nDot product:", v*u)
    print("If this line prints, you forgot to raise a ValueError for taking the dot product of vectors of different lengths")
except:
    print("If this line prints, an error was correctly raised.")
'''


