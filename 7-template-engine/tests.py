from template_engine import TemplateEngine
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.engine = TemplateEngine()
        self.engine.add_variable('name', 'Ben')

    def test_evaluate_string_with_no_variables(self):
        string = "Hello"
        evaluated_string = self.engine.evaluate(string)
        self.assertEqual(evaluated_string, "Hello")

    def test_evaluate_string_with_single_variable(self):
        string = "Hello {name}"
        evaluated_string = self.engine.evaluate(string)
        self.assertEqual(evaluated_string, "Hello Ben")

    def test_evaluate_string_with_multiple_variables(self):
        self.engine.add_variable('fname', 'Ben')
        self.engine.add_variable('sname', 'Nuttall')
        string = "Hello {fname} {sname}"
        evaluated_string = self.engine.evaluate(string)
        self.assertEqual(evaluated_string, "Hello Ben Nuttall")

    def test_evaluate_string_with_non_existant_variable(self):
        string = "Hello {user}"
        method_call = self.engine.evaluate
        expected_exception = TemplateEngine.MissingValueException
        self.assertRaises(expected_exception, method_call, string)

    def test_evaluate_string_with_double_curly_braces_around_variable(self):
        string = "Hello {{name}}"
        evaluated_string = self.engine.evaluate(string)
        self.assertEqual(evaluated_string, "Hello {Ben}")

    def test_initialise_template_engine_object_with_dictionary(self):
        variables = {
                        'this': 'THE',
                        'is': 'STRING',
                        'a': 'IS NOW',
                        'string': 'CAPITALISED',
                    }
        new_engine = TemplateEngine(variables)
        string = "{this} {is} {a} {string}"
        expected_string = "THE STRING IS NOW CAPITALISED"
        self.assertEqual(new_engine.evaluate(string), expected_string)

if __name__ == '__main__':
    unittest.main()