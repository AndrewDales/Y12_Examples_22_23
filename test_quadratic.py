import pytest
from quadratic import quadratic_solver
from math import sqrt


# Normal test - two integer solutions
def test_quadratic_solver_normal():
    assert quadratic_solver(1, -5, 6) == (2, 3)


# Normal test - non-integer coefficients and solutions
def test_quadratic_solver_non_integer():
    assert quadratic_solver(5, 1/3, -2/3) == (-2/5, 1/3)


# Normal test - two irrational solutions
def test_quadratic_solver_irrational():
    assert quadratic_solver(2, -4, 1) == (1 - sqrt(2)/2, 1 + sqrt(2)/2)


# Boundary test - single root
def test_quadratic_solver_one_root():
    assert quadratic_solver(1, 2, 1) == (-1, )


# Normal test - complex roots
def test_quadratic_solver_complex():
    assert quadratic_solver(1, 0, 1) == (-1j, 1j)


# Normal test - irrational complex roots
def test_quadratic_solver_complex_irrational():
    assert quadratic_solver(3, -2, 7) == ((2 - 4j * sqrt(5)) / 6, (2 + 4j * sqrt(5)) / 6)


# test for non-numeric inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        quadratic_solver(3, "3", 2)  # type: ignore
        quadratic_solver("3", 3, 2)  # type: ignore


# Example of parameterized tests
# --- list of data to test
test_data = [
    (3, 1, -2, (-1, 2/3)),
    (1, -1, -1, ((1 - sqrt(5))/2, (1 + sqrt(5)) / 2)),
    (1, 0, 9, (-3j, 3j)),
    (1, 6, 9, (-3, ))
]


# Test using test_data
@pytest.mark.parametrize("a, b, c, roots", test_data)
def test_quadratic_multiple(a, b, c, roots):
    assert quadratic_solver(a, b, c) == roots
