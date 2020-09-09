"""
Basic tests for Lab07"
"""

import pytest
from Lab07 import roll_dice, play_game


def test_bigger_than_min():
    params = [(4, 6), (4,), (10, 10), (3, 20)]
    mins = [4, 4, 10, 3]
    for p, m in zip(params, mins):
        student = roll_dice(*p)
        assert (
            student >= m
        ), "You are somehow getting a total less than the minimum possible?"


def test_smaller_than_max():
    params = [(4, 6), (4,), (10, 10), (3, 20)]
    maxes = [24, 24, 100, 60]
    for p, m in zip(params, maxes):
        student = roll_dice(*p)
        assert (
            student <= m
        ), "You are somehow getting a total greater than the maximum possible?"


def test_bigger_than_min_num_turns():
    params = [(20,), (20, 5,), (20, 5, 10), (100, 6, 2)]
    mins = [2, 1, 1, 9]
    for p, m in zip(params, mins):
        student = play_game(*p)
        assert (
            student >= m
        ), "You are somehow getting a total less than the minimum number of turns possible?"
