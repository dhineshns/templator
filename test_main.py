import unittest
import main as main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    ## Test templator
    ## Requirement 1 :  Input of empty string should return empty string
    def test_gen_text_from_template(self):
        result = main.gen_text_from_template("")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()