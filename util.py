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


def do_calculator(expression):                      # Define the function
    if not isinstance(expression, str):             # Checks if a expression is a str, because the split below only works with str
        return None                                 # If it is not, return None and stop
    
    if "+" in expression:                           # Identifies which math symbol the str contains    
        operator = "+"                              # Stores the found symbol in the variable operator
    elif "-" in expression:
        operator = "-"                              # The variable keeps being reassigned
    elif "*" in expression:
        operator = "*"
    elif "/" in expression:
        operator = "/"    
    else:                                           # If the string does not contain any of those symbols
        return None                                 # Return None and stop

    try:
        left, right = expression.split(operator)    # Splits the text into two parts using the operator as a separator. They are stored in left and right
    except ValueError:                              
        return None
    
    try:
        a = float(left)                             # Converts the text to numbers
        b = float(right)
    except ValueError:                              # If the conversion is not possible
        return None                                 # Return None
    
    if operator == "+":                             # Performs the operations
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return None
    

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
