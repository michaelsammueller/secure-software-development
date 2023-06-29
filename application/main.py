"""
    Contains the main function for the program.
"""
# Imports
from commandline_interface import CommandLineInterface
from user import User

# Insert test user
#john_doe = User('john doe', '1', '30061998', '1', '1', 'john.doe', b'$2b$12$1sloC3lxVFlrwguDUNmT8O.QAKu6uSxUtyd1EkvsduH7ov9Oyqm.O')

#john_doe.add_user()


# Main Function
def main():
    """Main function"""
    # Create instance of Commandline_Interface class
    commandline_interface = CommandLineInterface()
    commandline_interface.display_main_menu()

# Run Program
if __name__ == "__main__":
    main()
=======
