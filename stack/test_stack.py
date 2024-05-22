import unittest
from stack import FifthInterpreter

class TestFifthInterpreter(unittest.TestCase):
        
    def test_add(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [1,2,3]
        fifth_interpreter.add()
        self.assertEqual(fifth_interpreter.stack, [1,5])
        
    def test_minus(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [10,5]
        fifth_interpreter.minus()
        self.assertEqual(fifth_interpreter.stack, [5])
        
    def test_multiply(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [1,2]
        fifth_interpreter.multiply()
        self.assertEqual(fifth_interpreter.stack, [2])
        
    def test_divide(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [10,5]
        fifth_interpreter.divide()
        self.assertEqual(fifth_interpreter.stack, [2])
        
    def test_divide_by_zero(self):
        # divide by 0 should keep the stack the same
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [1,0]
        fifth_interpreter.divide()
        self.assertEqual(fifth_interpreter.stack, [1,0])
        
    def test_divide_rounds_down(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [2,4]
        fifth_interpreter.divide()
        self.assertEqual(fifth_interpreter.stack, [0])
        
    def test_push(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [2]
        fifth_interpreter.push(4)
        self.assertEqual(fifth_interpreter.stack, [2,4])
        
    def test_pop(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [2]
        fifth_interpreter.pop()
        self.assertEqual(fifth_interpreter.stack, [])
        
    def test_swap(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [2,4]
        fifth_interpreter.swap()
        self.assertEqual(fifth_interpreter.stack, [4,2])
        
    def test_dup(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.stack = [2,4]
        fifth_interpreter.dup()
        self.assertEqual(fifth_interpreter.stack, [2,4,4])
        
if __name__ == '__main__':
    unittest.main()