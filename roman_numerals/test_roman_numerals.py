import unittest
from unittest.mock import patch

from roman_numerals import get_user_input, translate_roman_numerals_to_value

class TestRomanNumerals(unittest.TestCase):
    
    @patch('builtins.input', return_value='IAMNOTAVALIDROMANNUMERAL') # patch input
    def test_user_input_invalid_string_value(self, input):
        # test ValueError is raised if a user passes values which are not roman numerals
        with self.assertRaises(ValueError):
            get_user_input()

    def test_translate_roman_numerals_to_value_valid_input(self):
        # Test valid Roman numerals with the given correct value output
        test_cases = [
            ("X", 10),
            ("VI", 6),
            ("MXVII", 1017),
            ("MC", 1100),
            ("CXI", 111)
        ]
        
        for roman, value in test_cases:
            with self.subTest(roman=roman):
                self.assertEqual(translate_roman_numerals_to_value(roman), value, f"Calculation for roman numeral value {roman} is not {value}")
            
if __name__ == '__main__':
    unittest.main()