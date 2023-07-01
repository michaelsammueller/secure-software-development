"""
    This file contains the Input_Sanitisation_Service class
"""

# Imports
from imports import re

# Input Sanitisation Service Class
class Input_Sanitisation_Service:

    def filter_sql_keywords(self, user_input): # TESTED AND WORKING
        """Filters SQL keywords from user input"""
        sql_keywords = ['SELECT', 'UPDATE', 'INSERT', 'DELETE', 'FROM', 'WHERE', 'JOIN']

        for keyword in sql_keywords:
            if keyword in user_input:
            # Replace SQL keywords with empty string
                sanitized_input = user_input.replace(keyword, '')
                return sanitized_input

        return user_input

    def filter_special_characters(self, user_input, whitespace=True): # TESTED AND WORKING
        """
            Filters special characters from user input. If whitespace is false,
            whitespace is not filtered.
        """
        if whitespace:
            sanitized_input = re.sub(r'[^\w\s]', '', user_input)
        else:
            sanitized_input = re.sub(r'[^\w]', '', user_input)
        
        # Check if any changes were made
        if sanitized_input == user_input:
            return user_input
        
        return sanitized_input

    def assert_input_size(self, user_input, min_size, max_size):
        """Asserts that the length of input is within specified range"""
        if len(user_input) < min_size or len(user_input) > max_size:
            raise ValueError(f"Input must be between {min_size} and {max_size} characters long")
        else:
            return True

    def assert_number(self, user_input):
        """Asserts that input is a number"""
        try:
            float(user_input)  # Convert input to float
            return True
        except ValueError:
            return False

    def match_pattern(self, user_input, pattern):
        """Matches input against specified pattern"""
        match = re.match(pattern, user_input)
        return bool(match)  # Returns True if match is found, False otherwise

    def sanitise_phrase(self, phrase): # TESTED AND WORKING
        """Sanitises phrase"""
        try:
            # Filter SQL keywords
            phrase = self.filter_sql_keywords(phrase)
            # Filter special characters
            phrase = self.filter_special_characters(phrase, False)
            return phrase # Return sanitised phrase
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
