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


def is_leap_year(year):                     # Defines the function. Year is the value to be evaluated
    if not isinstance(year, int):           # Checks that the value is an integer
        return None                         # If it is not, then return None
    
    if year % 400 == 0:                     # If it is divisible by 400
        return True                         # Then it is a leap year
    
    if year % 100 == 0:                     # If it is divisible by 100
        return False                        # Then it is not a leap year
    
    if year % 4 == 0:                       # If it is divisible by 4
        return True                         # Then it is a leap yea
    
    return False                            # In any other case, it is not


def do_calculator(expression):
    pass


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
