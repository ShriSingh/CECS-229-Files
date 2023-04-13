# %% [markdown]
# # CECS 229 Programming Assignment #3
# 
# #### Due Date: 
# 
# Sunday, 3/5 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks:

# %% [markdown]
# ------------------------------------------
# #### Utility functions

# %%
"""Utility Functions from previous coding assignments"""
# Writing a function to find the bezout coefficients of two numbers
def bezout_coeffs(a, b):
    # Variables to store the current and updated values of a and b
    value_a, value_b = a, b # Using absolute values to avoid negative a & b values
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

# Writing a function to find the greatest common divisor of two numbers
def gcd(a,b):
    # Calling the bezout_coeffs function to find the coefficients of a and b
    a_b_coeffs = bezout_coeffs(a, b)
    s_coeff_a = a_b_coeffs[a] # Coefficient of a -> s
    t_coeff_b = a_b_coeffs[b] # Coefficient of b -> t

    # Calculating the greatest common divisor of a and b
    GCD = abs((a * s_coeff_a) + (b * t_coeff_b)) # Following the Bezout Identity: |a*s + b*t| = gcd(a,b) 
    
    return GCD # Returning the greatest common divisor of a and b

# Writing a function that computes the modular exponentiation of a number
def mod_exp(b, n, m): # b -> base; n -> exponent; m -> modulus (all positive integers)
    result = 1 # result -> the final result of the modular exponentiation
    if b < 0 or n < 0 or m < 0: # Checks if the base, exponent, and modulus are positive integers
        result = 0 # Returns as the result 0 to satisfy the condition
        pass    
    k = bin(n)[2:] # k -> converting the exponent 'n' into binary form using 'bin' without the '0b'
    power = b % m # power -> base to the power of 2
    for i in range(len(k) -1, -1, -1): # Iterates through the binary form of the exponent in reverse order
        if k[i] == '1': # Checks if the current digit is 1
            result = (result * power) % m # Computes the result
        power = (power * power) % m # Computes the power
    return result # result = b^n mod m

"""Using given utility functions in Programming Assignment #3 file"""
# Utility function to convert letters to digits
def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter) - 65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

# Utility function to convert digits to letters
def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) + 65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

# Returns the size of a block in an RSA encrypted string
def blocksize(n):
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

# %% [markdown]
# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.
# 
# 

# %%
# Writing a function that returns the smallest, positive inverse of a modulo m
def modinv(a,m):
    """returns the smallest, positive inverse of a modulo m
    INPUT: a - integer
    m - positive integer
    OUTPUT: an integer in the range [0, m-1]
    """
    # Storing the result after calling the result of the gcd() function
    GCD_Calculation = gcd(a,m)
    if GCD_Calculation != 1: # Checking if a and m are relatively prime
        raise ValueError("The given values are not relatively prime") # Raising an error if a and m are not relatively prime
    elif m < 1:
        raise ValueError("\'m\' has to be a positive integer") # Raising an error if m is not greater than 1
    else: # When the basic requirements above are met
        # Calling the bezout_coeffs() function to find the coefficients of a and m
        a_m_coeffs = bezout_coeffs(a, m)
        """Only the coefficient of 'a' is needed to find the inverse of 'a' modulo 'm'
        Because sa = 1 (mod m), and s is the coefficient of 'a', where s(s_coeff_a in this case) is the inverse
        According to the THM 4.4.1"""
        # Setting up variables to store the coefficients of a and m
        s_coeff_a = a_m_coeffs[a] # Coefficient of a -> s

        correct_value = 0 # Variable to store the value of the inverse of 'a' modulo 'm'

        # Setting up conditonal statments to check coefficient of 'a' are in the range [0, m-1]
        if s_coeff_a >= 0 and s_coeff_a < m: 
            correct_value = s_coeff_a # If the coefficient of 'a' is in the range [0, m-1], then it is the correct value
        else:
            correct_value = s_coeff_a + m # Otherwise, add 'm' to the coefficient of 'a' to get the correct value
       
        mod_inv_value = correct_value # Transferring the value to a better-named variable

    return mod_inv_value # Returning the value of x as the inverse of 'a' modulo 'm'

# %% [markdown]
# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
# Writing a function that outputs a cipher text encrypted using key(a, b)
def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer   
    OUTPUT: The encrypted message as a string of characters
    """
    # Calling on the gcd() instruction 
    GCD_calculation = gcd(a, 26)
    # Checking if the gcd(a, 26) is not equal to 1
    if GCD_calculation != 1:
        raise ValueError("The given key is invalid. The gcd(a, 26) must be 1")
    else: # When the basic requirements above are met
        digit_letters = letters2digits(text) # Converting the text to "digits"(numbers in string format)
        # Creating a variable to store the encrypted text
        encrypted_cipher_num = "" 

        # Writing a loop to shift the digit letters
        for char_digit in range(0, len(digit_letters), 2): # --> Each letter is associated with 2 digits
            # Converting the "digits" into numbers
            numbers = int(digit_letters[char_digit:char_digit + 2]) # --> Each letter is associated with 2 digits
            # Implementing the affine encryption formula
            encrypted_num = (a * numbers + b) % 26
            # Converting the encrypted numbers into "digits"
            if encrypted_num < 10: # --> Each letter is associated with 2 digits, e.g. A = 10, B = 11, C = 12, etc.
                # Adding a "0" to the front of the encrypted number to make it 2 digits
                encrypted_digits = "0" + str(encrypted_num)
            else: # If the encrypted number is greater than 10
                encrypted_digits = str(encrypted_num)
            # Adding the encrypted digits to the encrypted cipher "numbers"
            encrypted_cipher_num += encrypted_digits

        # Converting the encrypted cipher "numbers" into letters
        cipher_message_encrypted = digits2letters(encrypted_cipher_num)

    return cipher_message_encrypted # Returning the encrypted cipher text 

# %% [markdown]
# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
# Writing a function that outputs a cipher text decrypted using key(a, b)
def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    # Calling on the gcd() instruction 
    GCD_calculation = gcd(a, 26)
    # Checking if the gcd(a, 26) is not equal to 1
    if GCD_calculation != 1:
        raise ValueError("The given key is invalid. The gcd(a, 26) must be 1")
    else: # When the basic requirements above are met
        digit_letters = letters2digits(ciphertext) # Converting the text to "digits"(numbers in string format)
        decrypted_message_num = "" # Creating a variable to store the decrypted text

        # Writing a loop to shift the digit letters
        for char_digit in range(0, len(digit_letters), 2): # --> Each letter is associated with 2 digits
            # Converting the "digits" into numbers
            numbers = int(digit_letters[char_digit:char_digit + 2]) # --> Each letter is associated with 2 digits
            # Implementing the affine decryption formula
            decrypted_num = (modinv(a, 26) * (numbers - b)) % 26
            # Converting the decrypted numbers into "digits"
            if decrypted_num < 10: # --> Each letter is associated with 2 digits, e.g. A = 10, B = 11, C = 12, etc.
                # Adding a "0" to the front of the decrypted number to make it 2 digits
                decrypted_digits = "0" + str(decrypted_num)
            else: # If the decrypted number is greater than 10
                decrypted_digits = str(decrypted_num)
            # Adding the decrypted digits to the decrypted cipher "numbers"
            decrypted_message_num += decrypted_digits

        # Converting the decrypted cipher "numbers" into letters
        cipher_message_decrypted = digits2letters(decrypted_message_num)

    return cipher_message_decrypted # Returning the decrypted cipher text

# %% [markdown]
# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(m, n, e)` which encrypts a string `m` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
# Writing a function that encrypts a string using RSA key(n = p * q, e)
def encryptRSA(m, n, e):
    """encrypts the plaintext m, using RSA and the key (n = p * q, e)
    INPUT:  m - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    # Converting the plaintext into digit "numbers"(numbers in string format)
    digit_letters = letters2digits(m)
    # Create a variable to store the block size
    block_size = blocksize(n)

    # Writing a while loop if the length of the digit_letters is not a multiple of the block size
    while len(digit_letters) % block_size != 0:
        # Padding the "digits" with "23"(X) to make it a multiple of the block size
        digit_letters += "23" 

    # Creating a variable to store the "digits" into blocks
    unencrypted_blocks = []
    # Writing a loop to split the "digits" into blocks
    for i in range(0, len(digit_letters), block_size): # --> Each letter is associated with 2 digits
        # Converting the "digits" into numbers
        numbers = digit_letters[i:i + block_size] # --> Each letter is associated with 2 digits
        # Appending the "numbers" to the unencrypted_blocks list
        unencrypted_blocks.append(numbers)

    encrypted_blocks = [] # Creating a variable to store the encrypted blocks
    # Writing a loop to encrypt the blocks
    for block in unencrypted_blocks:
        message_num = int(block) # Converting the "digits" into numbers
        # Implementing the RSA encryption formula
        encrypt_RSA_num = str(mod_exp(message_num, e, n)) # --> C = M^e mod n
        # Padding the "digits" with "0" to make the length of the "digits" a multiple of the block size
        encrypt_RSA_num = encrypt_RSA_num.zfill(block_size)
        # Adding the encrypted blocks to the cipher_blocks list
        encrypted_blocks.append(encrypt_RSA_num)

    # Creating a variable to store the encrypted cipher "numbers"
    RSA_encrypted_num = " ".join(encrypted_blocks) 

    return RSA_encrypted_num # Returning the encrypted cipher text


# %%
'''--------------------- ENCRYPTION TESTER CELL ---------------------------'''
"""----------------------- TEST 1 ---------------------------"""
'''
encrypted1 = encryptRSA("STOP", 2537, 13)
encrypted2 = encryptRSA("HELP", 2537, 13)
encrypted3 = encryptRSA("STOPS", 2537, 13)
print("Encrypted Message:", encrypted1)
print("Expected: 2081 2182")
print("Encrypted Message:", encrypted2)
print("Expected: 0981 0461")
print("Encrypted Message:", encrypted3)
print("Expected: 2081 2182 1346")
'''

"""--------------------- TEST 2 ---------------------------"""
'''
encrypted = encryptRSA("UPLOAD", 3233, 17)
print("Encrypted Message:", encrypted)
print("Expected: 2545 2757 1211")
'''


# %% [markdown]
# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.

# %%
# Writing a function to output the decrypted message using RSA key(n = p * q, e)
def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    actual_message = '' # Creating a variable to store the actual message
    encrypted_cipher = c.replace(" ", "") # Removing the spaces in the cipher text 
    n = p * q # Storing the product of the prime numbers as part of the key n = p * q
    m = (p - 1) * (q - 1) # Storing the product of (p - 1) and (q - 1)

    cipher_length = len(encrypted_cipher) # Storing the length of the encrypted cipher

    # Writing a loop for the decrypting the encrypted cipher
    for i in range(0, cipher_length, 4):
        # Splitting the encrypted cipher into blocks of 4
        cipher_blocks = encrypted_cipher[i:i + 4]
        # Finding the inverse of e
        inverse = modinv(e, m)
        # Decrypting the blocks using the RSA decryption formula
        cipher_blocks = int(cipher_blocks) ** inverse % n
        # Converting the decrypted numbers into string of "digits"
        cipher_blocks = str(cipher_blocks)

        # Conditional statement to check if the length of the cipher_blocks is less than 4
        if len(cipher_blocks) < 4:
            # Padding the "digits" with "0" to make the length of the "digits" a multiple of the block size
            actual_message += digits2letters('0' + cipher_blocks)
        else: # Otherwise printing the decrypted cipher blocks
            actual_message += digits2letters(cipher_blocks)
    
    return actual_message # Returning the decrypted cipher text


# %%
'''
"""--------------------- TESTER CELL ---------------------------"""
decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")

"""--------------------- TEST 2---------------------------"""
decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
print("Decrypted Message:", decrypted)
print("Expected: SILVER")
'''


