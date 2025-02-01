# Root-Finding Assignment (COT4500)

This project implements and tests four numerical approaches to root-finding:

- Approximation algorithm (for root of 2)
- Bisection Method
- Fixed-Point Iteration
- Newton-Raphson Method
    
The algorithms are tested on three functions:

    f(x)=x^2−2

    f(x)=cos⁡(x)−x

    f(x)=x^3+4x^2−10

With appropriate variations chosen for the fixed-point method to ensure convergence. The project is structured to use pytest for testing and includes a requirements.txt file for dependency management.

---

## Installation
Clone the respository with
```bash
git clone https://github.com/fshcat/cot-4500-Pro1.git
```
and run the following command in the project directory
```bash 
pip install -r requirements.txt
```
in order to install required packages.

---

## Running tests
Use the command
```bash
pytest src/test/test_assignment_1.py -v
```
to execute all test cases and show detailed output.

New test cases may be added by modifying `src/test/test_assignment_1.py`
