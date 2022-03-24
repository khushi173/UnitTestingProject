import unittest

def BiggestOfTwoNumbers(x,y):
    if x>y:
        return x
    else:
        return y
class  BiggestNumbers(unittest.TestCase):
    def test_case1(self):
        x = 40
        y = 30
        result = BiggestOfTwoNumbers(x,y)
        self.assertEqual(x,result)
    def test_case2(self):
        x=60
        y=88
        result = BiggestOfTwoNumbers(x,y)
        self.assertEqual(y,result)

if  __name__=="__main__":
    unittest.main()
