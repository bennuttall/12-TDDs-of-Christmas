from re import findall


class TemplateEngine:
    def evaluate(self, string, variables):
        vars_found = findall(r"\{([A-Za-z0-9_]+)\}", string)
        for var in vars_found:
            key = '{%s}' % var
            if var not in variables:
                raise TemplateEngine.MissingValueException
            string = string.replace(key, variables[var])
        return string

    class MissingValueException(Exception):
        pass