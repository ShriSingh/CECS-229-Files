# %% [markdown]
# # CECS 229: Programming Assignment #1
# 
# #### Due Date: 
# 
# Sunday, 2/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment, you must submit **to CodePost** this file converted to a Python script named `pa1.py`
# 
# #### Objectives:
# 
# 1. Compute the quotient and remainder of two numbers.
# 2. Apply numerical algorithms for computing the sum of two numbers in binary representation.
# 3. Apply numerical algorithms for computing the modular exponentiation of a positive integer.
# 
# 

# %% [markdown]
# --------------------------------
# 
# #### Problem 1:
# 
# Program a function `div_alg(a, d)` that computes the quotient and remainder of $$a \div d$$ according to the Division Algorithm (THM 4.1.2).   
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - an integer representing the dividend
#     * `d` - positive integer representing the divisor
# 
#     
# 2. OUTPUT:
#     * a dictionary of the form `{'quotient' : q, 'remainder' : r}` where `q` and `r` are the quotient and remainder values, respectively.  The remainder should satisfy, $0 \leq r < d$.
# 
#  
# EXAMPLE: 
# 
# `>> div_alg( 101 , 11 )`
# 
# `{'quotient' : 9, 'remainder' : 2}`

# %%
'''Problem 1 Solution:'''
# Writing a function to compute the quotient and remainder according to the Division Algorithm
def div_alg(a, d: int): # a -> dividend; d(a positive integer) -> divisor
    q = 0  # q -> quotient
    r = abs(a) # r -> remainder in absolute value
    # 
    while r >= d:
        r -= d
        q += 1
    if a < 0 and r > 0:
        r = d - r
        q = -(q + 1)
    return {'quotient': q, 'remainder': r} # {q = a div d is the quotient, r = a mod d is the remainder}

# %% [markdown]
# --------------------------------
# 
# #### Problem 2:
# 
# Program a function `binary_add(a, b)` that computes the sum of the binary numbers  $$a = (a_{i-1}, a_{i-2}, \dots, a_0)_2$$ and $$b = (b_{j-1}, b_{j-2}, \dots, b_0)_2$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  The function can not use built-in functions that already perform some kind of binary representation or addition of binary numbers.  For example, the function implementation can **not** use the functions `bin()` or `int(a, base=2)`.
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `a` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
#     * `b` - a string of the 0's and 1's that make up the first binary number.  The string *may* contain spaces.
# 
#     
# 2. OUTPUT:
#     * the string of 0's and 1's that is the result of computing $a + b$.  The string must be separated by spaces into blocks of 4 characters or less, beginning at the end of the string.
# 
#  
# EXAMPLE: 
# 
# `>> binary_add( '10 1011' , '11011')`
# 
# `'100 0110'`
# 
# 
# 

# %%
'''Problem 2 Solution:'''
# Writing a function to convert a string binary to numerical binary
def stringBin_to_numBin(bin):
    decimal = 0
    bin = bin[::-1] # Reverses the binary number string
    for i in range(len(bin)): # Iterates through the binary number string
        if bin[i] == '1': # Checks if the current digit is 1
            decimal += 2 ** i  # Computes the decimal value of the binary number
    return decimal # Returns the decimal value of the binary number

# Writing a function to compute the sum of two binary numbers with base-b expansions
def base_expansion(n, b): # n -> integer; b -> base(positive integers with b > 1)
    q = n # q -> dividend that is updated in each iteration
    k = 0 # k -> index of the current coefficient in the base expansion
    exp_result = [] # holds the list of coefficients
    while q != 0:
        a = q % b # a -> coefficient of the base b
        q = q // b # q -> dividend that is updated in each iteration
        exp_result.append(a) # adds coefficient to the list every iteration
        k += 1 # Updates the index of the coefficient
    return exp_result[::-1] # returns the list of coefficients in reverse order

# Writing a function to compute the sum of two binary numbers with base-2 expansions
def binary_add(a, b): # a and b are binary numbers
    # Removes the spaces in the binary numbers
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    # Converts the binary numbers to integers
    a = stringBin_to_numBin(a)
    b = stringBin_to_numBin(b)
    bin_num1 = base_expansion(a, 2) # bin_num1 -> binary number a
    bin_num2 = base_expansion(b, 2) # bin_num2 -> binary number b
    carry = 0 # c -> carry bit
    sum = '' # sum -> sum of the two binary numbers

    # Checks if the length of the binary numbers are equal
    # Adds 0s to the beginning of the shorter binary number
    if len(bin_num1) < len(bin_num2):
        bin_num1 = [0] * (len(bin_num2) - len(bin_num1)) + bin_num1 
    else:
        bin_num2 = [0] * (len(bin_num1) - len(bin_num2)) + bin_num2

    for i in range(0, max(len(bin_num1), len(bin_num2))):
        x = (bin_num1[len(bin_num1) - 1 - i] + bin_num2[len(bin_num2) - 1 - i] + carry) % 2 # Computes the sum of the two binary numbers
        y = (bin_num1[len(bin_num1) - 1 - i] + bin_num2[len(bin_num2) - 1 - i] + carry) // 2 # Computes the carry bit using quotient
        sum = str(x) + sum # Adds/Updates the sum to the sum string
        carry = y # Updates the carry bit
    if carry == 1:
        sum = str(carry) + sum # Adds the carry bit to the sum string if the carry bit is 1

    final_sum = '' # Holds the sum with spaces every 4 digits
    count = 0 # Holds the count of the digits
    for i in range(len(sum) -1, -1, -1): # Iterates through the sum in reverse order
        count += 1 # Increments the count 
        final_sum = str(sum[i]) + final_sum # Adds the current digit to the final sum
        if count % 4 == 0 and i != 0: # Check for the 4th digit 
            final_sum = ' ' + final_sum # Adds a space to the sum every 4 digits
        else: 
            final_sum = final_sum # Does not add a space to the sum

    return final_sum

# %% [markdown]
# --------------------------------
# 
# #### Problem 3:
# 
# Program a function `mod_exp(b, n, m)` that computes $$b^n \mod m$$ using the algorithm discussed in lecture.  No credit will be given to functions that employ any other implementation.  For example, if the function implementation simply consists of `b ** n % m`, no credit will be given.  
# 
# The function should satisfy the following:
# 
# 1. INPUT: 
#     * `b` - positive integer representing the base
#     * `n` - positive integer representing the exponent
#     * `m` - positive integer representing the modulo
# 
#     
# 2. OUTPUT:
#     * the computation of $b^n \mod m$ if b, n, m are positive integers, 0 otherwise.
# 
#  
# EXAMPLE: 
# 
# `>> mod_exp( 3 , 644, 645 )`
# 
# `36`
# 
# 
# 

# %%
'''Problem 3 Solution:'''
# Writing a function that computes the modular exponentiation of a number
def mod_exp(b, n, m): # b -> base; n -> exponent; m -> modulus (all positive integers)
    result = 1 # result -> the final result of the modular exponentiation
    if b < 0 or n < 0 or m < 0: # Checks if the base, exponent, and modulus are positive integers
        result = 0
        pass    
    k = bin(n)[2:] # k -> converting the exponent 'n' into binary form using 'bin' without the '0b'
    power = b % m # power -> base to the power of 2
    for i in range(len(k) -1, -1, -1): # Iterates through the binary form of the exponent in reverse order
        if k[i] == '1':
            result = (result * power) % m 
        power = (power * power) % m
    return result # result = b^n mod m
