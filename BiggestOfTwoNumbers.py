import unittest

def BiggestOfTwoNumbers(x,y):
    if x>y:
        return "number is bigger"
    else:
        return "number is smaller"
class  BiggestNumbers(unittest.TestCase):
    def test_case1(self):
        x = 40
        y = 30
        result = BiggestOfTwoNumbers(x,y)
        self.assertEqual("number is bigger",result)
    def test_case2(self):
        x=60
        y=88
        result = BiggestOfTwoNumbers(x,y)
        self.assertEqual("number is smaller",result)

if  __name__=="__main__":
    unittest.main()
