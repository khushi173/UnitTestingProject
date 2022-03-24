import unittest

def login_verification(username, password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False
class LoginVerificationTest(unittest.TestCase):
    def test_login_check(self):
        result = login_verification("admin","12345")
        self.assertTrue(result)
if  __name__=="__main__":
    unittest.main()

