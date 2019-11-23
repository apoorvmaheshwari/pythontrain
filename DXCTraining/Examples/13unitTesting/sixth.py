import unittest
''' 
setup , teardown
'''
class TestStringMethods(unittest.TestCase):
	 def setUp(self):
        self.string1 = "foo"
        self.string2 = "FOO"

    def tearDown(self):
        delattr(self,"string1")
        delattr(self,"string2")
    def test_upper(self):
        self.assertEqual(self.string1.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue(self.string2.isupper())
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
   