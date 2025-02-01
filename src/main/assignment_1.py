import math

def approximation_algo(initial_value, tolerance, max_iterations=100, debug=True):
    """
    'Approximation algorithm' as titled in the slides.
    Approximates the square root of 2 using a specific fixed point method
    """

    last_val = val = initial_value
    i = 0

    if debug:
        print(f"{0}:\t {val:.12f} \t| error: N/A")

    for i in range(max_iterations):

        # Perform iteration
        val = val/2 + 1/val

        # Calculate error
        error = abs(val - last_val) 

        if debug:
            print(f"{i+1}:\t {val:.12f} \t| error: {error}")
        if error < tolerance:
            break

        last_val = val

    if debug:
        print(f"\nConvergence after {i+1} iterations")

    return val

def bisection_algo(f, left_bound, right_bound, tolerance, max_iterations=100, debug=True):
    """
    Bisection method
    Finds root of the function f by binary search over given bounds.
    Left and right bounds should have differing signs.
    """

    f_left = f(left_bound)
    f_right = f(right_bound)

    # Check that left and right bounds have different signs
    if (f_left > 0) == (f_right > 0) or f_left == 0 or f_right == 0:
        print("Improper inputs (function values at bounds must have different signs)")
        return None
    
    # Swap order of bounds if left has positive function value
    if f(left_bound) > 0:
        left_bound, right_bound = right_bound, left_bound

    i = 0
    mid = last_mid = (left_bound + right_bound)/2

    if debug:
        print(f"{0}:\t {mid:.12f} \t| error: N/A")

    for i in range(max_iterations):
        # Iterate binary search
        f_left = f(left_bound)
        f_right = f(right_bound)
        f_mid = f(mid)

        if f_mid > 0:
            right_bound = mid
        else:
            left_bound = mid

        mid = (left_bound + right_bound) / 2

        # Calculate error
        error = abs(mid - last_mid)

        if debug:
            print(f"{i}:\t {mid:.12f} \t| error: {error}")
        if error < tolerance:
            break

        last_mid = mid
    
    if debug:
        print(f"\nConvergence after {i+1} iterations")
    
    return mid

def fixed_point_algo(f, initial_value, tolerance, max_iterations=100, debug=True):
    """ 
    Fixed point iteration
    Finds fixed point of the function f
    """

    last_val = val = initial_value
    i = 0

    if debug:
        print(f"{0}:\t {val:.12f} \t| error: N/A")

    for i in range(max_iterations):
        # Fixed point iteration
        val = f(val)

        # Calculate error
        error = abs(val - last_val) 
    
        if val == float('inf'):
            print(f"\nDivergence after {i+1} iterations")
            return None
        if debug:
            print(f"{i+1}:\t {val:.12f} \t| error: {error}")
        if error < tolerance:
            break
    
        last_val = val
    
    if debug:
        print(f"\nConvergence after {i+1} iterations")
    
    return val 

def newton_raphson_algo(f, df, initial_value, tolerance, max_iterations=100, debug=True):
    """
    Newton-Raphson method
    Finds roots of function f with derivative df by iteratively using linear approximation
    """

    last_val = val = initial_value
    i = 0

    if debug:
        print(f"{0}:\t {val:.12f} \t| error: N/A")

    for i in range(max_iterations):
        f_val = f(val)
        df_val = df(val)
        val = val - f_val/df_val

        error = abs(val - last_val) 
    
        if val == float('inf'):
            print(f"\nDivergence after {i+1} iterations")
            return None
        if df_val == 0:
            print(f"\nFailure due to zero derivative after {i+1} iterations")
        if debug:
            print(f"{i+1}:\t {val:.12f} \t| error: {error}")
        if error < tolerance:
            break
    
        last_val = val
    
    if debug:
        print(f"\nConvergence after {i+1} iterations")

    return val
