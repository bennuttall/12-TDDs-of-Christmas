# 7. Template Engine

Write a "template engine" meaning a way to transform template strings, "Hello {$name}" into "instanced" strings. To do that a variable->value mapping must be provided. For example, if name="Bill" and the template string is "Hello {$name}" the result would be "Hello Bill".

- Should evaluate template single variable expression:

        mapOfVariables.put("name","Bill");
        templateEngine.evaluate("Hello {$name}", mapOfVariables)
        => "Hello Bill"

- Should evaluate template with multiple expressions:

        mapOfVariables.put("firstName","Bill");
        mapOfVariables.put("lastName","Clay");
        templateEngine.evaluate("Hello {$firstName} {$lastName}", mapOfVariables);
        => "Hello Bill Clay"

- Should give error if template variable does not exist in the map:

        map empty
        templateEngine.evaluate("Hello {$firstName} ", mapOfVariables);
        => missingvalueexception

- Should evaluate complex cases:

        mapOfVariables.put("name","Bill");
        templateEngine.evaluate("Hello ${{$name}}", mapOfVariables);
        => should evaluate to "Hello ${Bill}"
