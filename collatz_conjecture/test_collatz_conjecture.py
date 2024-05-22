import unittest
from unittest.mock import patch

from collatz_conjecture import calculate_collatz_conjecture_steps, get_user_input

class TestCollatzConjecture(unittest.TestCase):
    
    @patch('builtins.input', return_value='mystring') # patch input
    def test_user_input_invalid_string_value(self, input):
        # test ValueError is raised if a user passes a non-numeric value
        with self.assertRaises(ValueError):
            get_user_input()

    @patch('builtins.input', return_value='-10') # patch input    
    def test_user_input_negative_value_(self, input):
        # test ValueError is raised if a user passes a negative number
        with self.assertRaises(ValueError):
            get_user_input()

    @patch('builtins.input', return_value='0') # patch input   
    def test_user_input_zero_value(self, input):
        # test ValueError is raised if a user passes 0
        with self.assertRaises(ValueError):
            get_user_input()
            
    def test_calculate_collatz_conjecture_steps_num_1_steps_0(self):
        # for n = 1, the expected number of steps should be 0
        self.assertEqual(
            calculate_collatz_conjecture_steps(1), 
            0, 
            "Test failed for calculate collatz conjecture steps for input value 1, steps calculated is not 0"
        )
        
    def test_calculate_collatz_conjecture_steps_num_10_steps_6(self):
        # for n = 10, the expected number of steps should be 6
        self.assertEqual(
            calculate_collatz_conjecture_steps(10), 
            6, 
            "Test failed for calculate collatz conjecture steps for input value 10, steps calculated is not 6"
        )
        
if __name__ == '__main__':
    unittest.main()