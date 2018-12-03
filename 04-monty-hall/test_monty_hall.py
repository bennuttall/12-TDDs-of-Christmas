from monty_hall import Game
import pytest

def test_select_invalid_door():
    game = Game(prize=1)
    with pytest.raises(ValueError):
        game.select_door(0)
    with pytest.raises(ValueError):
        game.select_door(4)
    game.select_door(2)
    assert 3 not in game._options
    with pytest.raises(ValueError):
        game.select_door(3)

def test_correct_first_choice():
    game = Game(prize=1)
    assert game.options == [1, 2, 3]
    game.select_door(1)
    assert len(game.options) == 2 and 1 in game.options

def test_incorrect_first_choice():
    game = Game(prize=1)
    game.select_door(2)
    assert game.options == [1, 2]

def test_change_selection():
    game = Game(prize=1)
    assert game.won is None
    assert game.options == [1, 2, 3]
    game.select_door(1)
    assert len(game.options) == 2 and 1 in game.options
    game.final_selection(change=True)
    assert game.won is not None
    assert game.won is False

def test_keep_selection():
    game = Game(prize=1)
    assert game.won is None
    assert game.options == [1, 2, 3]
    game.select_door(1)
    assert len(game.options) == 2 and 1 in game.options
    game.final_selection(change=False)
    assert game.won is not None
    assert game.won is True

def test_random_prize():
    game = Game()
    assert game._prize in [1, 2, 3]
