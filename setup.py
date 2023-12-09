import setuptools
setuptools.setup(
name="bytealgebra",
version="1.1.1",
author="Ismail Boularbah",
author_email="boularbahismail01@gmail.com",
description="Algebraic Functions Package Built In Python Programming Languages",
long_description='''\
        The Algebraic Functions Package is a feature-rich library developed in Python, providing a wide array 
        of algebraic functions for mathematical computations. This package is designed to empower scientists,
        engineers, and mathematicians with a robust set of tools for algebraic operations, simplifications,
        and equation solving.

        Features:
        - Polynomial manipulations, including addition, subtraction, multiplication, and division.
        - Expression simplification and expansion for enhanced readability.
        - Equation solving capabilities for both linear and nonlinear equations.
        - Support for symbolic algebra, allowing manipulation of algebraic expressions with variables.
        - Integration and differentiation of algebraic expressions.
        - Error-free and efficient implementation for precise mathematical results.

        Whether you are working on symbolic mathematics or numerical computations, the Algebraic Functions Package 
        offers a versatile and easy-to-use solution for a wide range of algebraic tasks. Explore the power of
        algebraic manipulation with the convenience of Python.

        For more information and usage examples, visit the project repository: 
        https://github.com/yourusername/your-package
    ''',
    long_description_content_type='text/markdown',
url="https://github.com/boularbahsmail/bytealgebra",
packages=setuptools.find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)