# Problem 2 Solution:
#FIXME: Implement this function
def binary_add(a, b):
    sum = "" # Holds the sum of a and b
    carry = 0 # Holds the carry bit

    bin_num1 = [] # Holds the binary number a
    # Checks and compensates for the spaces in the binary number
    for i in a:
        # Checks if the current character is a space
        if i != ' ':
            bin_num1.append(int(i)) # Appends the binary number to the list

    bin_num2 = [] # Holds the binary number b
    # Checks and compensates for the spaces in the binary number
    for i in b:
        # Checks if the current character is a space
        if i != ' ':
            bin_num2.append(int(i)) # Appends the binary number to the list

    # Checks if the length of the binary numbers are equal
    # Adds 0s to the beginning of the shorter binary number
    if len(bin_num1) < len(bin_num2):
        bin_num1 = [0] * (len(bin_num2) - len(bin_num1)) + bin_num1 
    else:
        bin_num2 = [0] * (len(bin_num1) - len(bin_num2)) + bin_num2

    for i in range(0, max(len(bin_num1), len(bin_num2))):
        x = (bin_num1[len(bin_num1) - 1 - i] + bin_num2[len(bin_num2) - 1 - i] + carry) % 2 # Holds the current binary digit using modulus
        y = (bin_num1[len(bin_num1) - 1 - i] + bin_num2[len(bin_num2) - 1 - i] + carry) // 2 # Holds the updated carry bit using integer division
        sum = str(x) + sum # Adds the current binary digit to the sum
        carry = y # Updates the carry bit
    if carry: # If the carry bit is 1, add it to the sum
        sum = str(carry) + sum # Adding the carry bit to the sum

    final_sum = '' # Holds the sum with spaces every 4 digits
    count = 0 # Holds the count of the digits
    for i in range(len(sum) -1, -1, -1): # Iterates through the sum in reverse order
        count += 1 # Increments the count 
        final_sum = str(sum[i]) + final_sum # Adds the current digit to the final sum
        if count % 4 == 0 and i != 0: # Check for the 4th digit 
            final_sum = ' ' + final_sum # Adds a space to the sum every 4 digits

    return final_sum


# Problem 3 Solution:
def mod_exp(b, n, m):
    '''
    x = 1 # Holds the result of the modular exponentiation
    while n > 0: 
        if n % 2 == 1:
            x = (x * b) % m
        n = n >> 1
        b = (b * b) % m
    return x
    '''
    
