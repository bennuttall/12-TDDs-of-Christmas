from recently_used_list import RecentlyUsedList
import pytest

def test_recently_used_list():
    rul = RecentlyUsedList()
    assert len(rul) == 0
    rul.add('A')
    assert len(rul) == 1
    rul.add('B')
    assert len(rul) == 2
    assert rul[0] == 'B'
    assert rul[-1] == 'A'
    rul.add('B')
    assert len(rul) == 2
    assert rul[0] == 'B'
    assert rul[1] == 'A'
    rul.add('A')
    assert len(rul) == 2
    assert rul[0] == 'A'
    assert rul[1] == 'B'
    with pytest.raises(TypeError):
        rul.add()
    with pytest.raises(ValueError):
        rul.add('')
    with pytest.raises(ValueError):
        rul.add(True)
    with pytest.raises(ValueError):
        rul.add(object)

def test_recently_used_list_with_overflow():
    rul = RecentlyUsedList(limit=1)
    rul.add('A')
    assert len(rul) == 1
    rul.add('B')
    assert len(rul) == 1

    rul = RecentlyUsedList(limit=10)
    for i in range(1, 20):
        rul.add(str(i))
    assert len(rul) == 10
    assert rul.items == ['19', '18', '17', '16', '15', '14', '13', '12', '11', '10']
