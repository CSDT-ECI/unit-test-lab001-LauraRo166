from yatzy import Yatzy
import pytest


# chance

def test_chance_sums_all_dice():
    assert Yatzy.chance(1, 2, 3, 4, 5) == 15

def test_chance_all_same():
    assert Yatzy.chance(6, 6, 6, 6, 6) == 30


# yatzy

def test_yatzy_five_of_same_returns_50():
    assert Yatzy.yatzy([4, 4, 4, 4, 4]) == 50

def test_yatzy_not_five_of_same_returns_0():
    assert Yatzy.yatzy([1, 1, 1, 1, 2]) == 0


# ones / twos / threes

def test_ones_all_ones():
    assert Yatzy.ones(1, 1, 1, 1, 1) == 5

def test_ones_mixed():
    assert Yatzy.ones(1, 2, 1, 3, 1) == 3

def test_twos_all_twos():
    assert Yatzy.twos(2, 2, 2, 2, 2) == 10


# fours / fives / sixes (instance methods) — solo fours

def test_fours_all_fours():
    y = Yatzy(4, 4, 4, 4, 4)
    assert y.fours() == 20

def test_fours_none():
    y = Yatzy(1, 2, 3, 5, 6)
    assert y.fours() == 0


# score_pair

def test_score_pair_highest_pair():
    assert Yatzy.score_pair(3, 3, 6, 6, 1) == 12

def test_score_pair_no_pair():
    assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0


# two_pair

def test_two_pair_valid():
    assert Yatzy.two_pair(1, 1, 2, 2, 5) == 6

def test_two_pair_only_one_pair():
    assert Yatzy.two_pair(3, 3, 1, 2, 5) == 0


# three_of_a_kind

def test_three_of_a_kind_basic():
    assert Yatzy.three_of_a_kind(3, 3, 3, 1, 2) == 9

def test_three_of_a_kind_not_enough():
    assert Yatzy.three_of_a_kind(1, 1, 2, 3, 4) == 0


# straights — solo smallStraight

def test_small_straight():
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15

def test_small_straight_wrong():
    assert Yatzy.smallStraight(2, 3, 4, 5, 6) == 0


# fullHouse

def test_full_house_basic():
    assert Yatzy.fullHouse(2, 2, 3, 3, 3) == 13

def test_full_house_not_valid():
    assert Yatzy.fullHouse(1, 1, 2, 3, 4) == 0