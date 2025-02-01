import pytest
from src.main.assignment_1 import (
    approximation_algo,
    bisection_algo,
    fixed_point_algo,
    newton_raphson_algo,
)
import math

# Defining functions for test cases

# Calculating root of 2
def root_two(x):
    return x*x - 2
def d_root_two(x):
    return 2*x
def fixed_point_root_two(x):
    return (x*x+2)/(2*x)

# Calculating root of a certain cubic
def cubic(x):
    return x*x*(x + 4) - 10
def d_cubic(x):
    return x*(3*x + 8)
def fixed_point_cubic(x):
    return (10 - x*x*x)**(0.5) / 2

# Calculating x that satisfies cos(x)=x
def cos_fixed_point(x):
    return math.cos(x)
def cos_root(x):
    return math.cos(x) - x
def d_cos_root(x):
    return -math.sin(x) - 1


# Functions to check test cases for each relevant function

def test_root_two_algorithms():
    # Setup for x^2 - 2 = 0
    f = root_two
    df = d_root_two
    fixed_f = fixed_point_root_two
    init_left = 1
    init_right = 2
    init = 1.5
    expected_root = math.sqrt(2)

    # Test "Approximation algorithm"
    result = approximation_algo(init, 1e-6, debug=False)

    # Test Bisection method
    result = bisection_algo(f, init_left, init_right, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Fixed-Point method
    result = fixed_point_algo(fixed_f, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Newton-Raphson method
    result = newton_raphson_algo(f, df, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

def test_cos_root_algorithms():
    # Setup for cos(x) - x = 0
    f = cos_root
    df = d_cos_root
    fixed_f = cos_fixed_point
    init_left = 0
    init_right = math.pi / 2
    init = math.pi / 4
    expected_root = 0.739085133215  # Known value (Dottie number)

    # Test Bisection method
    result = bisection_algo(f, init_left, init_right, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Fixed-Point method
    result = fixed_point_algo(fixed_f, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Newton-Raphson method
    result = newton_raphson_algo(f, df, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

def test_cubic_algorithms():
    # Setup for x^3 + 4x^2 - 10 = 0
    f = cubic
    df = d_cubic
    fixed_f = fixed_point_cubic
    init_left = -4
    init_right = 7
    init = 1.5
    expected_root = 1.365230013414  # Precomputed approximate root

    # Test Bisection method
    result = bisection_algo(f, init_left, init_right, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Fixed-Point method
    result = fixed_point_algo(fixed_f, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

    # Test Newton-Raphson method
    result = newton_raphson_algo(f, df, init, 1e-6, debug=False)
    assert pytest.approx(expected_root, abs=1e-6) == result

