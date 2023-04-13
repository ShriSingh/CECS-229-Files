import math

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

#print(decimal_to_binary(10))
#print(decimal_to_binary(100))
#print(decimal_to_binary(1000))

# Pesudo Code for Product of two binary numbers
'''
def binaryProduct(a, u):
    c = [] # Empty container
    s = 0
    k = bin(u)[2:]
    for i in range(len(k) - 1, -1, -1):
        u_i = 1 # or replace this line with the appropriate expression to get the value of u_i
        if u_i == 1:
            x = a << i
            c.append(x)
    for j in range(0, len(c)):
        s = binary_add(s, c[j])
    return s   
binaryProduct('1000111', '1110111')
'''

# Actual Code for Product of two binary numbers
'''
def binary_product(a, b):
    product = 0
    for i in range(0, int(math.log2(b)) + 1):
        if b & (1 << i) != 0:
            product += a << i
            print(product)
    return product
binary_product('1000111', '1110111')
'''

'''
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
'''

# Writing a function that computes the modular exponentiation of a number
def mod_exp(b, n, m): # b -> base; n -> exponent; m -> modulus (all positive integers)
    result = 1 # result -> the final result of the modular exponentiation
    if b < 0 or n < 0 or m < 0: # Checks if the base, exponent, and modulus are positive integers
        result = 0
        pass    
    k = bin(n)[2:] # k -> converting the exponent 'n' into binary form using 'bin' without the '0b'
    power = b % m # power -> base to the power of 2
    print("Power: ", power)
    for i in range(len(k) -1, -1, -1): # Iterates through the binary form of the exponent in reverse order
        if k[i] == '1':
            result = (result * power) % m
        power = (power * power) % m
        print("power: ", power)
    return result # result = b^n mod m
mod_exp(11, 644, 645)
