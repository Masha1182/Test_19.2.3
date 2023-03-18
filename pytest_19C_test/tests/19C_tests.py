import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiple_calc_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4   #тест на правильность умножения

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 4, 2) == 2   #тест на правильность деления

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2  #тест на правильность вычитания

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4  #тест на правильность сложения
