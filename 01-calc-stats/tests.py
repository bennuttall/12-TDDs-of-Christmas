from calc import Calculator

values = [6, 9, 15, -2, 92, 11]
calc = Calculator(values)

assert calc.min == -2
assert calc.max == 92
assert calc.len == 6
assert calc.avg == 21.833333333333332
