from re import findall


class TemplateEngine:
    def __init__(self, variables={}):
        self.variables = variables

    def add_variable(self, key, value):
        self.variables[key] = value

    def evaluate(self, string):
        vars_found = findall(r"\{([A-Za-z0-9_]+)\}", string)
        for var in vars_found:
            key = '{%s}' % var
            if var not in self.variables:
                raise TemplateEngine.MissingValueException
            string = string.replace(key, self.variables[var])
        return string

    class MissingValueException(Exception):
        pass