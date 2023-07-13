"""
    This file contains the Input_Sanitisation_Service class
"""

# Imports
import re
import datetime

# Input Sanitisation Service Class
class Input_Sanitisation_Service:

    def filter_sql_keywords(self, user_input): # TESTED AND WORKING
        """Filters SQL keywords from user input"""
        sql_keywords = ['SELECT', 'UPDATE', 'INSERT', 'DELETE', 'FROM', 'WHERE', 'JOIN', ' OR', 'OR']

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
    
    def validate_password(self, password): # SHOULD THIS CONTAIN CHARACTER FILTER TO PREVENT EVIL REGEX?
        """Validates user password based on constraints"""
        try:
            # Assert password size
            if self.assert_input_size(password, 8, 64):
                # Assert that no special characters in password
                if self.filter_special_characters(password, True) == password:
                    return True
                else:
                    print("Password cannot contain special characters")
                    return False
            else:
                print("Password must be between 8 and 64 characters long")
            return True
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
    
    def validate_country(self, country):
        """Validates country input"""
        countries = ["CA", "DK", "FR", "DE", "IT", "JP", "NL", "NO", "RU", "ES", "SE", "SZ", "GB", "US"]
        if country in countries:
            return True
        else:
            print(f"Invalid country. Please select from: \n{countries} ")
            return False
    
    def validate_role(self, role):
        """Validates roles input"""
        roles = ["Superadmin", "Moderator", "Astronaut"]
        if role.lower().capitalize() in roles:
            return True
        else:
            print("Invalid role.")
            return False
    
    def validate_dob(self, dob):
        """Validates date of birth input"""
        try:
            datetime.datetime.strptime(dob, '%d-%m-%Y')
            return True
        except ValueError:
            print("Incorrect data format, should be DD-MM-YYYY")
            return False
        
    def validate_integer(self, number):
        """Validates integer"""
        try:
            int(number)
            return True
        except ValueError:
            print("Please enter an integer")
            return False
        
    def validate_enum(self, user_input, options):
        """Validates option"""
        if user_input in options:
            return True
        else:
            print(f"Please select from: {options}")
            return False
        
    def validate(self, user_input, type, options, *args, **kwargs):
        '''
            Validates user input based on type. Returns True if validation passes,
            False otherwise.
        '''
        if type == 'PASSWORD':
            return self.validate_password(user_input)
        elif type == 'COUNTRY':
            return self.validate_country(user_input)
        elif type == 'ROLE':
            return self.validate_role(user_input)
        elif type == 'DATE':
            return self.validate_dob(user_input)
        elif type == 'ENUM':
            return self.validate_enum(user_input, options)
        elif type == 'INT':
            return self.validate_integer(user_input)
        else:
            print("Invalid type.")
            return False

    def connect_logger(self, logger):
        """Connects the logger"""
        self.__logger = logger