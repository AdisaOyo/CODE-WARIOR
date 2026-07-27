def xo(s):
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    else:
        return False
import codewars_test as test
from solution import xo

@test.describe("Sample tests")
def _():
    test_cases = [
        ("ooxx",    True),
        ("xooxx",   False),
        ("ooxXm",   True), # Comparison is case-insensitive
        ("zpzpzpp", True), # when no 'x' and 'o' is present should return true
        ("zzoo",    False),
        ("oxOx",    True),
        ("",        True),  # Empty string contains equal amount of x and o
    ]
    for s, expected in test_cases:
        @test.it(f"{s = }")
        def _():
            test.assert_equals(xo(s), expected)