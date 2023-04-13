import math

# Putting up Vector class from the previous assignment for Matrix * Vector multiplication
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

        return vector_product # Returning the scalar-vector multiplication
    
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation