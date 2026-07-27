def distance_between_points(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
import codewars_test as test
from solution import distance_between_points
from preloaded import Point

@test.describe("Fixed Tests")
def fixed_tests():

    def do_test(a, b, expected):
        actual = distance_between_points(a, b)
        test.assert_approx_equals(actual, expected, 1e-6, f"Incorrect answer for:\n  a=Point({a.x}, {a.y})\n  b=Point({b.x}, {b.y})\n")
    
    @test.it('Basic Test Cases')
    def basic_test_cases():
        do_test(Point(3, 3), Point(3, 3), 0)
        do_test(Point(1, 6), Point(4, 2), 5)
        do_test(Point(-10.2, 12.5), Point(0.3, 14.7), 10.728001)