from number_names import number_name

def test_number_names():
    assert number_name(9) == 'nine'
    assert number_name(10) == 'ten'
    assert number_name(11) == 'eleven'
    assert number_name(12) == 'twelve'
    assert number_name(15) == 'fifteen'
    assert number_name(16) == 'sixteen'
    assert number_name(20) == 'twenty'
    assert number_name(21) == 'twenty one'
    assert number_name(55) == 'fifty five'
    assert number_name(99) == 'ninety nine'
    assert number_name(300) == 'three hundred'
    assert number_name(310) == 'three hundred and ten'
    assert number_name(1501) == 'one thousand, five hundred and one'
    assert number_name(12609) == 'twelve thousand, six hundred and nine'
    assert number_name(512607) == 'five hundred and twelve thousand, six hundred and seven'
    assert number_name(43112603) == 'forty three million, one hundred and twelve thousand, six hundred and three'
    
