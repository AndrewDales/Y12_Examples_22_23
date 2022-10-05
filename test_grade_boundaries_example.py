import pytest
from grade_boundaries import calc_grade


def test_calc_grade():
    assert calc_grade(259) == "A"
    assert calc_grade(188) == "C"
