def area_or_perimeter(l , w):
    # return your answer
    if l == w:
        return l*w
    elif l != w:
        return (2*l) + (2*w)
import codewars_test as test
from solution import area_or_perimeter

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(area_or_perimeter(4, 4), 16)
        test.assert_equals(area_or_perimeter(6, 10), 32)