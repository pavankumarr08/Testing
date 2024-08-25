import unittest
import main
import example

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param=10
        result=main.do_test(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param='abcdef'
        result=main.do_test(test_param)
        self.assertTrue(isinstance(result, ValueError))
    
    def test_do_stuff3(self):
        test_param=None
        result=main.do_test(test_param)
        self.assertEqual(result, 'please enter a number')
    
    def test_do_stuff4(self):
        test_param=''
        result=main.do_test(test_param)
        self.assertEqual(result,'please enter a number')
    
    def TestGame(self):
        answer =5
        guess = 5
        result = example.run_guess(answer, guess)
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()