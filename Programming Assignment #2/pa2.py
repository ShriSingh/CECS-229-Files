# %% [markdown]
# # CECS 229: Programming Assignment #2
# 
# #### Due Date: 
# 
# Tuesday, 2/21 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa2.py`
# 
# #### Objectives:
# 
# 1. Use the Sieve of Eratosthenes to find all primes in a given range.
# 2. Design a computational algorithm for finding the Bézout coefficients of two integers.
# 3. Use Bézout coefficients to calculate the GCD.
# 

# %% [markdown]
# -------------------------------------------------------
# #### Problem 1:
# 
# Create a function `primes(a, b)` that uses the Sieve of Eratosthenes to find all the primes $p$ satisfying $a \leq p \leq b$.  You may not use any built-in functions that perform entire or part of this algorithm.
# 
# 1. INPUT:
#   
#   * `a` - a positive integer greater than or equal to 1 (raise a `ValueError` if an integer less than 1 is given), that is the lower bound
#   * `b` - a positive integer greater than or equal to `a` (raise a `ValueError` if `b` < `a`)
#   
# 2. OUTPUT:
#     
#     * a set of all the primes $p$ satisfying `a` $\leq p \leq$ `b`
#     
# EXAMPLE:
# 
# `>> primes(1, 10)`
# 
# `{2, 3, 5, 7}`
# 
# `>> primes(50, 100)`
# 
# `{53, 59, 61, 67, 71, 73, 79, 83, 89, 97}`
# 
# Note: the order of the elements might be different in your output, and that is okay! As long as you have all the primes.

# %%
# Writing a function to find all the prime numbers between two numbers using Sieve of Eratosthenes
def primes(a, b):
    # Writing conditional statements to raise ValueErrors for certain types of inputs
    if a < 1:
        # Raising valueError for Lower Bound(a)
        raise ValueError("The lower bound must be greater than or equal to 1")
    elif b < a:
        # Raising valueError for Upper Bound(b)
        raise ValueError("The upper bound must be greater than or equal to the lower bound")
    else: # Continuing with the code if the inputs are valid
        # Preparing an boolean array of all primes up to the square root of b 
        upper_bound = int(b ** 0.5) # Generations for the boolean array    
        all_primes = [True] * (upper_bound + 1) # The Boolean Array
        # Setting values of 0 and 1 to False(they are not prime nor composite)
        all_primes[0] = all_primes[1] = False
        smallest_prime = 2 # The smallest prime number is 2
        # Finding all the primes up to the square root of b
        for i in range(smallest_prime, int(upper_bound) + 1):
            if all_primes[i] == True:
                for j in range(i * i, upper_bound + 1, i): # Marking all the multiples of i as False
                    all_primes[j] = False

        # Array to store actual values of the prime numbers between a and b
        prime_nums = []
        sieve_range = [True] * (b - a + 1) # Boolean array to store the prime numbers between a and b
        # Finding all the primes between a and b
        for i in range(2, upper_bound + 1):
            if all_primes[i]:
                # Starting point of sieve/root out multiples of i
                starting_point = max(i * i, ((a + i - 1) // i) * i)

                # Marking all the multiples of i as False
                for j in range(starting_point, b + 1, i):
                    sieve_range[j - a] = False
        
        # Converting "TRUE" primes to their actual values
        for i in range(len(sieve_range)):
            if sieve_range[i] and i + a > 1:
                prime_nums.append(i + a)

        return set(prime_nums) # Returning the prime numbers between a and b as a set

# %% [markdown]
# ----------------------------------------------
# 
# #### Problem 2:
# 
# Create a function `bezout_coeffs(a, b)` that computes the Bezout coefficients `s` and `t` of `a` and `b`.
# 
# 1. INPUT: 
#     * `a`,`b` - distinct integers
# 
# 2. OUTPUT: `{a: s, b: t}` - dictionary where keys are the input integers and values are their corresponding Bezout coefficients.
# 
# EXAMPLE:  
#  
# `>> bezout_coeffs(414, 662)` 
# 
# `{414 : 8, 662 : -5}`
# 
# 

# %% [markdown]
# #### HINT:
# 
# 
# To come up with an algorithm for the function `bezout_coeff(a,b)` consider the following example:
# 
# Suppose $a = 13,\;\; b = 21$.  We seek $s$ and $t$ such that gcd$(13, 21) = 13s + 21t$
# 
# Let's begin by defining $s_0 = 1, \;\; t_0 = 0, \;\; a_1 = 13,\;\; b_1 = 21$.  At every round in attempting to attain the gcd, we will refer to $s_i$ and $t_i$ as the current coefficients of 13 and 21, respectively.
# 
# 
# **Round 1:**
# 
# $21 = 1 \cdot 13 +8  $
# 
# $\hspace{2cm} \implies 8 = 21 - 1 \cdot 13$  We will call this EQN 1
# 
# $\hspace{2cm} \implies s_1 = -1, \hspace{0.5cm} t_1 = 1$
# 
# NOTICE:
# 
# $\hspace{2cm} s_1 = - \; ( \; b_1 \textbf{ div } a_1 \; ) = -(21 \textbf{ div } 13) = -1 $
# 
# 
# 
# **Round 2:**
# 
# $a_2 = 8,\;\; b_2 = 13$
# 
# $13 = 1 \cdot 8 + 5 $
# 
# $\hspace{2cm} \implies 5 = 13 - 1 \cdot 8$
# 
# $\hspace{3.5cm} = 1 \cdot 13 - 1 (21 - 1 \cdot 13) $  from EQN 1
# 
# $\hspace{3.5cm} = 2 \cdot 13 - 1 \cdot 21 $
# 
# $\hspace{2cm} \implies s_2 = 2, \hspace{0.5cm} t_2 = -1$
# 
# 
# NOTICE:
# 
# $\hspace{2cm} s_2 = s_0 -  s_1\; (\; b_2\textbf{ div }a_2 ) $
# 
# $\hspace{2.5cm} = 1 -  1\; (\; 13\textbf{ div }8) $
# 
# $\hspace{2.5cm} = 1 -\;( -1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\hspace{2cm} t_2 = t_0 - t_1\; (\; b_2\textbf{ div }a_2 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (\; 13\textbf{ div }8 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (1)$
# 
# $\hspace{2.5cm} = -1$
# 
# 
# **Round 3:**
# 
# $a_3 = 5,\;\; b_3 = 8$
# 
# $8 = 1 \cdot 5 + 3$
# 
# $\hspace{2cm} \implies 3 = 8 - \underbrace{1}_{b_3\textbf{ div }a_3} \cdot 5$
# 
# $\hspace{3.5cm} = 1 \cdot (\underbrace{1}_{t_1}  \cdot 21 \underbrace{-1}_{s_1}  \cdot 13) - \underbrace{1}_{b_3\textbf{ div }a_3} (\underbrace{2}_{s_2}  \cdot 13 \underbrace{-1}_{t_2}  \cdot 21 ) $
# 
# $\hspace{3.5cm} = - 3 \cdot 13 + 2 \cdot 21$
# 
# $\hspace{2cm} \implies s_3 = -3, \hspace{0.5cm} t_3 = 2$
# 
# 
# 
# NOTICE:
# 
# $\hspace{2cm} s_3 = s_1 -s_2 \; ( \; b_3\textbf{ div }a_3) $
# 
# $\hspace{2.5cm} = -1 -(2)(1) $
# 
# $\hspace{2.5cm} = -3$
# 
# $\hspace{2cm} t_3 = t_1 - t_2 \; ( \; b_3\textbf{ div }a_3)$
# 
# $\hspace{2.5cm} = 1 -(-1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\vdots$
# 
# **Round $k$:**
# 
# For any round $k \geq 2$, the corresponding $s_k$ and $t_k$ values are given by
# 
# * $s_k = s_{k-2} - s_{k-1} \;(\; b_{k} \textbf{ div } a_{k})$
# 
# * $t_k = t_{k-2} - t_{k-1} \; (\; b_{k} \textbf{ div } a_{k})$
# 
# 
# 
# You should verify for yourself that for any $a, b$,
# * $s_0 = 1$
# * $t_0 = 0$
# * $s_1 = -(\; b \textbf{ div } a)$
# * $t_1 = 1$
# 
# 
# 

# %%
# Writing a function to find the bezout coefficients of two numbers
def bezout_coeffs(a, b):
    # Variables to store the current and updated values of a and b
    value_a, value_b = abs(a), abs(b) # Using absolute values to avoid negative a & b values
    # Variables to store the current and updated values of the 1st & previous round coefficients of a and b
    first_coeff_a, first_coeff_b = 1, 0
    # Variables to store the current and updated values of the 2nd & next round coefficients of a and b
    second_coeff_a, second_coeff_b = 0, 1

    # Creating a loop to go through the rounds of coefficients until b is 0
    while value_b != 0:
        # Integer division of a and b
        quotient = value_a // value_b
        # Modulo of a and b
        remainder = value_a % value_b
        # Calculating the new coefficients of a and b
        new_coeff_a = first_coeff_a - quotient * second_coeff_a
        new_coeff_b = first_coeff_b - quotient * second_coeff_b 

        # Updating the values of a and b
        value_a = value_b
        value_b = remainder
        # Updating the previous and next round coefficients of a
        first_coeff_a = second_coeff_a
        second_coeff_a = new_coeff_a
        # Updating the previous and next round coefficients of b
        first_coeff_b = second_coeff_b
        second_coeff_b = new_coeff_b
            
    return {a: first_coeff_a, b: first_coeff_b} # Returning the coefficients of a and b as a dictionary

# %% [markdown]
# ----------------------------------------------------------------------
# #### Problem 3:
# 
# Create a function `gcd(a, b)` that computes the greatest common divisor of `a` and `b` using the `bezout_coeff` function you implemented for problem 2 lecture.  No credit will be given to functions that employ any other implementation.  For example, using the built-in function `math.gcd()` as part of our implementation will not receive any credit.
# 
# 1. INPUT: 
#     * `a`,` b` - integers
# 
# 2. OUTPUT: `d` - the gcd
# 
# EXAMPLE:  
#  
# `>> gcd(414, 662)` 
# 
# `2`

# %% [markdown]
# #### HINT
# 
# The GCD of any two numbers must be positive by definition.

# %%
# Writing a function to find the greatest common divisor of two numbers
def gcd(a,b):
    # Calling the bezout_coeffs function to find the coefficients of a and b
    a_b_coeffs = bezout_coeffs(a, b)
    s_coeff_a = a_b_coeffs[a] # Coefficient of a -> s
    t_coeff_b = a_b_coeffs[b] # Coefficient of b -> t

    # Calculating the greatest common divisor of a and b
    GCD = abs((a * s_coeff_a) + (b * t_coeff_b)) # Following the Bezout Identity: |a*s + b*t| = gcd(a,b) 
    
    return GCD # Returning the greatest common divisor of a and b

# %% [markdown]
# ------------------------------------
# #### Testing Your Functions
# 
# You can test your functions by running the cell below and verifying that your answers agree with the expected outcomes.
# 
# YOU MUST COMMENT OUT THE CELL BELOW PRIOR TO SUBMITTING ON CODEPOST

# %%
""" TESTER CELL: YOU MUST COMMENT THIS CELL OUT PRIOR TO SUBMITTING ON CODEPOST """
'''
print("\nTesting primes(1, 10)\nResult:", primes(1, 10), "\nExpected: {2, 3, 5, 7}")
print("\nTesting primes(2, 37)\nResult:", primes(2, 37), "\nExpected: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}")
print("\nTesting primes(2, 100)\nResult:", primes(2, 100), "\nExpected: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}")
print("\nTesting bezout_coeffs(414, 662)\nResult:", bezout_coeffs(414, 662), "\nExpected: {414: 8, 662: -5}")
print("\nTesting bezout_coeffs(26, 7)\nResult:", bezout_coeffs(26, 7), "\nExpected: {26: 3, 7: -11}")
print("\nTesting gcd(101, 4620)\nResult:", gcd(101, 4620), "\nExpected: 1")
print("\nTesting gcd(1011, 4620)\nResult:", gcd(1011, 4620), "\nExpected: 3")
print("\nTesting gcd(2349, 36)\nResult:", gcd(2349, 36), "\nExpected: 9")
'''


