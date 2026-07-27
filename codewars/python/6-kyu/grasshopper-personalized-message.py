def greet(name, owner):
    # Add code here
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

import codewars_test as test
from solution import greet

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
        test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')