from math import sqrt
import cmath as cm
from numbers import Real
from typing import Union, Tuple


def quadratic_solver(a: Real, b: Real, c: Real) -> Union[Tuple[float], Tuple[float, float], Tuple[complex, complex]]:
    """
        solves the quadratic equation ax^2 + bx + c
        :param a: Real - coefficient
        :param b: Real - coefficient
        :param c: Real - coefficient
        :return: Tuple[float, float] or Tuple[complex, complex]
        """
    if not (isinstance(a, Real) and
            isinstance(b, Real) and
            isinstance(c, Real)):
        raise TypeError("Inputs must be real numbers")

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        roots = ((-b - sqrt(discriminant))/(2*a),  (-b + sqrt(discriminant))/(2*a))
    elif discriminant == 0:
        roots = (-b/(2*a), )
    else:
        roots = ((-b - cm.sqrt(discriminant))/(2*a),  (-b + cm.sqrt(discriminant))/(2*a))

    return roots


if __name__ == "__main__":
    print("This is a program to solve the quadratic ax^2+bx+c=0")
    a_val = float(input("Enter value for a: "))
    b_val = float(input("Enter value for b: "))
    c_val = float(input("Enter value for c: "))
    my_roots = quadratic_solver(a_val, b_val, c_val)
    if len(my_roots) == 1:
        print(f"{a_val}x^2 + {b_val}x + {c_val} = 0 has a single root at x = {my_roots[0]:.2f}")
    else:
        print(f"{a_val}x^2 + {b_val}x + {c_val} = 0 has two roots at x = {my_roots[0]:.2f} and x = {my_roots[1]:.2f}")