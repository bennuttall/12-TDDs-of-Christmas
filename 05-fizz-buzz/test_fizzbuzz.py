from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '2'
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(4) == '4'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(12) == 'Fizz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(16) == '16'
