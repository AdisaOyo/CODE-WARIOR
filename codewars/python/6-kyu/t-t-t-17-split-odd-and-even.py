def split_odd_and_even(n):
    n = str(n)
    ans = []
    current_group = ""
    previous_was_even = None

    for digit in n:
        current_is_even = int(digit) % 2 == 0

        if previous_was_even is not None and current_is_even != previous_was_even:
            ans.append(int(current_group))
            current_group = ""

        current_group += digit
        previous_was_even = current_is_even

    ans.append(int(current_group))
    return ans
        #your code here

@test.describe("Basic tests")
def f():
    @test.it("")
    def f():
        test.assert_equals(split_odd_and_even(123), [1,2,3])
        test.assert_equals(split_odd_and_even(223),  [22,3])
        test.assert_equals(split_odd_and_even(111),  [111])
        test.assert_equals(split_odd_and_even(13579),  [13579])
        test.assert_equals(split_odd_and_even(2468642), [2468642])
        test.assert_equals(split_odd_and_even(135246),  [135,246])
        test.assert_equals(split_odd_and_even(123456),  [1,2,3,4,5,6])
        test.assert_equals(split_odd_and_even(8123456),  [8,1,2,3,4,5,6])
        test.assert_equals(split_odd_and_even(82123456),  [82,1,2,3,4,5,6])
        test.assert_equals(split_odd_and_even(88123456),  [88,1,2,3,4,5,6])