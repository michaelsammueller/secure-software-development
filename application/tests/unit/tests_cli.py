'''
    This file contains unit tests for Sensor components.
'''
from context import CommandLineInterface
import unittest

class TestCLI(unittest.TestCase):
    '''
        A class for encapsulating unit tests for the CommandLineInterface class.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()

    def test_exit(self):
        '''
            A method that tests the read_data method.
        '''
        mock_selections = (x for x in ['2'])
        self.cli.ask_for_selection = lambda: next(mock_selections) # monkey patch
        self.assertTrue(self.cli.display_main_menu())
    




if __name__ == '__main__':
    unittest.main()

