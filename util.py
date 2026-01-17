def is_palindrome(str_to_evaluate):         # We define the function is_palindrome
    is_palindrome = False                   # Initially, we assume that is_palindrome is false and we will try to prove otherwise.
    
    cleaned = ""                            # We create a variable with an empty string where we will store the later result.
                                            # WE START CLEANING
    for char in str_to_evaluate.lower():    # Convert each caracter of the string to evaluate to lowercase.
        if char.isalnum():                  # Determine whether it is a letter or a number, or if it is a special character. If so, remove it.   
            cleaned += char                 # The result will be sent to the empty variable created previously.
                                            # WE COMPARE
    if cleaned == cleaned[::-1]:            # If the text of the empty string reads the same from left to right or viceversa.
            is_palindrome = True            # If so, then it states that it is a palindrome
    
    return is_palindrome                    # Returns the response to the program to indicate whether it is a palindrome
