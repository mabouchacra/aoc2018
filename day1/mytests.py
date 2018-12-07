import unittest
import mycode
import operator

class MyTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(mycode.hello_world(), 'Hello world !')
    
    def test_get_operator_plus(self):
        self.assertEqual(operator.add, mycode.get_operator('+2'))

    def test_get_operator_minus(self):
        self.assertEqual(operator.sub, mycode.get_operator('-2'))

    def test_addition_ok(self):
        self.assertEqual(3, mycode.add_element(0, "+3"))

    def test_addition_ok_2(self):
        self.assertEqual(8, mycode.add_element(3, "+5"))

    def test_sub_ok(self):
        self.assertEqual(0, mycode.add_element(3, '-3'))
        
    def test_sub_ok_2(self):
        self.assertEqual(-2, mycode.add_element(3, '-5'))

    def test_reduce_work_one_element(self):
        input = ["-3"]
        res = mycode.reduce_input(input)
        self.assertEqual(-3, res)

    def test_reduce_work_two_element(self):
        input = ["-3","+8"]
        res = mycode.reduce_input(input)
        self.assertEqual(5, res)

if __name__=='__main__':
    unittest.main()