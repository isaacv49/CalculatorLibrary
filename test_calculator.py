"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiply(self):
        assert 100 == calculator.multiply(10, 10)

    def test_divide(self):
        assert 10 == calculator.divide(100, 10)
