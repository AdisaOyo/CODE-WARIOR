def calc_type(a, b, res) -> str:
    if float(a)+float(b) == float(res):
        return 'addition'
    elif float(a)-float(b) == float(res):
        return 'subtraction'
    elif float(a)*float(b) == float(res):
        return 'multiplication'
    elif float(a)/float(b) == float(res):
        return 'division'
import codewars_test as test
from solution import calc_type

@test.describe("Tests")
def _():
    @test.it("Sample tests")
    def _():
        test.assert_equals(calc_type(1, 2, 3), "addition")
        test.assert_equals(calc_type(10, 5, 5), "subtraction")
        test.assert_equals(calc_type(10, 4, 40), "multiplication")
        test.assert_equals(calc_type(9, 5, 1.8), "division")