def take(arr,n):
    if n > arr.__len__():
        return arr
    else:
        return arr[0:n]

import codewars_test as test
from solution import take

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(take([0, 1, 2, 3, 5, 8, 13], 3), [0, 1, 2], "should return the first 3 items")
      