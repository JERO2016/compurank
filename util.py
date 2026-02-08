def is_palindrome(str_to_evaluate):         # Palindrome is a word that can be read from left to right and viceversa and retains its meaning.
    is_palindrome = False                   
   
    cleaned = ""                            # We create a variable with an empty string where we will store the later result.
                                            # WE START CLEANING
    for char in str_to_evaluate.lower():    # Convert each caracter of the string to evaluate to lowercase.
        if char.isalnum():                  # Determine whether it is a letter or a number, or if it is a special character. If so, remove it.   
            cleaned += char                 # The result will be sent to the empty variable created previously.
                                            # WE COMPARE
    if cleaned == cleaned[::-1]:            # If the text of the empty string reads the same from left to right or viceversa.
            is_palindrome = True            # If so, then it states that it is a palindrome
    
    return is_palindrome                    # Returns the response to the program to indicate whether it is a palindrome


def is_fizzbuzz(number):
    pass


def is_prime(number):
    pass


def is_leap_year(year):
    pass


def do_calculator(expression):                      # Ensure the input is a string
    if not isinstance(expression, str):         
        return None

    operator = None                                 # Placeholder to store the detected operator
    for op in ["+", "-", "*", "/"]:             
        if op in expression:
            operator = op
            break                                   # Stop once the first operator is found

    if not operator:                                # If no operator is found, the expression is invalid
        return None

    parts = expression.split(operator)              # Split the expression into two operands using the operator
    
    p1 = parts[0]                                   # First operand
    p2 = parts[1]                                   # Second operand

    if not p1.isdigit() or not p2.isdigit():        # Validate that both operands contain only digits
        return None                                 # isdigit() returns True only for numeric strings
    
    a = int(p1)                                     # Convert strings to integers for calculation
    b = int(p2)

    if operator == "+":                             # Perform the corresponding operation                       
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return None                                 # Fallback for any unexpected case
    

def generate_difference_between_dates(date1, date2, unit):
    pass


def vector_addition(vec1, vec2):
    pass


def vector_multiplication(vec, scalar):
    pass


def matrix_addition(mat1, mat2):
    pass


def matrix_multiplication(mat1, mat2):
    pass
