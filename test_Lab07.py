"""
Basic tests for Lab07"
"""

import pytest
import random
from Lab07 import roll_dice, play_game

def test_roll_dice():
    params = [(4, 6), (4,), (10, 10), (3, 20)]
    vals = [16, 16, 72, 44]
    for p,v in zip(params, vals):
        random.seed(1)
        student = roll_dice(*p)
        assert student == v, "You seem to be returning incorrect totals from roll dice."

def test_play_game():
    params = [(20,), (20, 5,), (50, 5, 10), (100, 6, 2)]
    vals = [3, 1, 2, 12]
    for p,v in zip(params, vals):
        random.seed(1)
        student = play_game(*p)
        assert student == v, "You seem to be returning an incorrect number of turns to reach the end from play_game.."
