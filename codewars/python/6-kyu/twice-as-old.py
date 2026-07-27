def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old >= 2 * son_years_old:
        return dad_years_old - 2*son_years_old
    else:
        return 2*son_years_old - dad_years_old
    pass
import codewars_test as test
from solution import twice_as_old

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(twice_as_old(36,7) , 22)
        test.assert_equals(twice_as_old(55,30) , 5)
        test.assert_equals(twice_as_old(42,21) , 0)
        test.assert_equals(twice_as_old(22,1) , 20)
        test.assert_equals(twice_as_old(29,0) , 29)
