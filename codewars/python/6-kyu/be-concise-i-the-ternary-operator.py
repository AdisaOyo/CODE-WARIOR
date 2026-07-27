def describe_age(age):return f"You're a(n) {'kid'if age<=12else'teenager'if age<=17else'adult'if age<=64else'elderly'}"

import codewars_test as test
import preloaded
from solution import describe_age

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(describe_age(9), "You're a(n) kid")
    test.assert_equals(describe_age(10), "You're a(n) kid")
    test.assert_equals(describe_age(11), "You're a(n) kid")
    test.assert_equals(describe_age(12), "You're a(n) kid")
    test.assert_equals(describe_age(13), "You're a(n) teenager")
    test.assert_equals(describe_age(14), "You're a(n) teenager")
    test.assert_equals(describe_age(15), "You're a(n) teenager")
    test.assert_equals(describe_age(16), "You're a(n) teenager")
    test.assert_equals(describe_age(17), "You're a(n) teenager")
    test.assert_equals(describe_age(18), "You're a(n) adult")
    test.assert_equals(describe_age(19), "You're a(n) adult")
    test.assert_equals(describe_age(63), "You're a(n) adult")
    test.assert_equals(describe_age(64), "You're a(n) adult")