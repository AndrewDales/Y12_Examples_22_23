import pytest
from grade_boundaries import calc_grade

test_data = [(0, "U"),
             (72, "E"),
             (111, "D"),
             (150, "C"),
             (189, "B"),
             (229, "A"),
             (264, "A*"),
             ]


def test_calc_grade():
    assert calc_grade(259) == "A"
    assert calc_grade(188) == "C"


def test_calc_grade_invalid():
    with pytest.raises(ValueError):
        calc_grade(400)
    with pytest.raises(ValueError):
        calc_grade(-20)
    with pytest.raises(TypeError):
        calc_grade("A")     # type: ignore


@pytest.mark.parametrize("score, grade", test_data)
def test_calc_grade_min_boundary(score, grade):
    assert calc_grade(score) == grade



