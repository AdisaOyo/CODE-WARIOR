def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    return (blue_start-blue_pulled) / ((blue_start-blue_pulled)+(red_start-red_pulled))
@test.describe("Basic tests")
def _():
    test.assert_approx_equals(guess_blue(5, 5, 2, 3), 0.6)
    test.assert_approx_equals(guess_blue(5, 7, 4, 3), 0.2)
    test.assert_approx_equals(guess_blue(12, 18, 4, 6), 0.4)