from template_engine import TemplateEngine
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.engine = TemplateEngine()

    def test_evaluate_string_with_no_variables(self):
        string = "Hello"
        variables = {}
        evaluated_string = self.engine.evaluate(string, variables)
        self.assertEqual(evaluated_string, "Hello")

    def test_evaluate_string_with_single_variable(self):
        string = "Hello {name}"
        variables = {'name': 'Ben'}
        evaluated_string = self.engine.evaluate(string, variables)
        self.assertEqual(evaluated_string, "Hello Ben")

    def test_evaluate_string_with_multiple_variables(self):
        string = "Hello {fname} {sname}"
        variables = {
                        'fname': 'Ben',
                        'sname': 'Nuttall'
                    }
        evaluated_string = self.engine.evaluate(string, variables)
        self.assertEqual(evaluated_string, "Hello Ben Nuttall")

    def test_evaluate_string_with_non_existant_variable(self):
        string = "Hello {user}"
        variables = {}
        method_call = self.engine.evaluate
        expected_exception = TemplateEngine.MissingValueException
        self.assertRaises(expected_exception, method_call, string, variables)

    def test_evaluate_string_with_double_curly_braces_around_variable(self):
        string = "Hello {{name}}"
        variables = {'name': 'Ben'}
        evaluated_string = self.engine.evaluate(string, variables)
        self.assertEqual(evaluated_string, "Hello {Ben}")

    def test_evaluate_same_string_twice_with_different_variables(self):
        string = "Hello {name}"
        variables = {'name': 'Ben'}
        evaluated_string_1 = self.engine.evaluate(string, variables)
        variables = {'name': 'Bill'}
        evaluated_string_2 = self.engine.evaluate(string, variables)
        self.assertEqual(evaluated_string_1, "Hello Ben")
        self.assertEqual(evaluated_string_2, "Hello Bill")

if __name__ == '__main__':
    unittest.main()