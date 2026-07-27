a = "code"
b = "wa.rs"
name = a + b
import codewars_test as test
from solution import name

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(name, "codewa.rs")