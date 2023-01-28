#! /usr/bin/env python3

from utfolding.segment import chord_length, get_x_list
from pytest import approx

'''
Testing settup for project
'''

def test_chord_length ():
    assert chord_length(50, 180) == approx(100)
    assert chord_length(50, 60) == approx(50)
    assert chord_length(50, 0.1) == approx(0.08726645)
    assert chord_length(50, 0) == 0

def test_get_x_list():
    assert get_x_list(10, 50) == [
        approx(0),
        approx(9.54915028),
        approx(34.54915028),
        approx(65.45084972),
        approx(90.45084972),
        approx(100),
        approx(90.45084972),
        approx(65.45084972),
        approx(34.54915028),
        approx(9.54915028),
        approx(0),
    ]
