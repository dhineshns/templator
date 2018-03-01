import unittest
import main as main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    ## Test templator
    ## Requirement 1 :  Input of empty string should return empty string
    def test_replace_string_empty_string(self):
        result = main.replace_string("", "", "")
        self.assertEqual(result, "")

    ## Requirement 2 : Input of template, string to be replaced, replacing_string will return the generate text.
    def test_replace_string_replacing_string(self):
        template = "Please return the <<<BOOK_NAME>> book. Again the books name is <<<BOOK_NAME>>"
        string_to_be_replaced = "<<<BOOK_NAME>>"
        replacing_string = "Outliers"
        result = main.replace_string(template, string_to_be_replaced, replacing_string)
        self.assertEqual(result, "Please return the Outliers book. Again the books name is Outliers")

    ## Requirement 3 : Input of template, map of replaced and replacing string would return replaced outputs.
    def test_gen_text_valid_inputs(self):
        template = "Hello <<<NAME>>>, Please return the <<<BOOK_NAME>> book."
        replacing_to_replaced_map = {"<<<NAME>>>": "Dhinesh", "<<<BOOK_NAME": "Outliers"}
        result = main.gen_text_from_template(template, replacing_to_replaced_map)
        self.assertEqual("Hello Dhinesh, Please return the Outliers book.", result)
if __name__ == '__main__':
    unittest.main()