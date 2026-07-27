def quarter_of(month):
    # your code here
    if month < 4:
        return 1
    elif 3 < month < 7:
        return 2
    elif 6 < month < 10:
        return 3
    elif 9 < month < 13:
        return 4
    
from solution import quarter_of
import codewars_test as test

def dotest(n, expected):
    actual = quarter_of(n)
    test.assert_equals(actual, expected, f"Test failed with month = {n}")
    
@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        dotest(3, 1)
        dotest(8, 3)
        dotest(11, 4)