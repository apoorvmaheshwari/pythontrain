import unittest
'''
The following decorators and exception implement 
test skipping and expected failures:

@unittest.skip(reason)
Unconditionally skip the decorated test. 
reason should describe why the test is being skipped.

@unittest.skipIf(condition, reason)
Skip the decorated test if condition is true.

@unittest.skipUnless(condition, reason)
Skip the decorated test unless condition is true.

@unittest.expectedFailure
Mark the test as an expected failure. 
If the test fails it will be considered a success.
If the test passes, it will be considered a failure.

exception unittest.SkipTest(reason)
This exception is raised to skip a test.
'''
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")