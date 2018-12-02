from mine_field import Minefield

inp = """
3 4
*...
..*.
....
"""

def test_minefield():
    mf = Minefield(inp)
    assert mf.width, mf.height == (4, 3)
    assert mf.minefield == [
        [True, False, False, False],
        [False, False, True, False],
        [False, False, False, False],
    ]
    assert mf.hint == [
        ['*', '2', '1', '1'],
        ['1', '2', '*', '1'],
        ['0', '1', '1', '1'],
    ]
    assert str(mf) == """
*211
12*1
0111
"""
