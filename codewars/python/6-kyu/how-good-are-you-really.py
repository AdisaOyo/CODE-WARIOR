def better_than_average(class_points, your_points):
    # Your code here
    total_class = 0
    total_stu = 0
    for point in class_points:
        total_class += point
        total_stu += 1
    avg = total_class/total_stu
    if avg < your_points:
        return True
    else:
        return False
import codewars_test as test

def test_it(arr, points, expected):
    @test.it(f"Testing with arr={arr}, points={points}")
    def _():
        test.assert_equals(better_than_average(arr, points), expected, f"better_than_average({arr}, {points}) should return {expected}")

@test.describe("Basic Tests")
def basic_tests():
    test_it([2, 3], 5, True)
    test_it([100, 40, 34, 57, 29, 72, 57, 88], 75, True)
    test_it([12, 23, 34, 45, 56, 67, 78, 89, 90], 69, True)
    test_it([41, 75, 72, 56, 80, 82, 81, 33], 50, False)
    test_it([29, 55, 74, 60, 11, 90, 67, 28], 21, False)
    test_it([100, 90, 80], 85, False)
    test_it([50, 50, 50], 50, False)