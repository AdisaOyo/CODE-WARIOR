def was_package_received_yesterday(tz_from, tz_to, start, duration):
    utc_departure = start - tz_from

    # Add travel time
    utc_arrival = utc_departure + duration

    # Convert to destination local time
    destination_time = utc_arrival + tz_to

    # Determine which day the package arrives locally
    arrival_day = destination_time // 24

    # Sent on day 0, so check if received on day -1
    return arrival_day == -1
from solution import was_package_received_yesterday
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Should return a boolean")
    def _():
        test.assert_equals(type(was_package_received_yesterday(1, 1, 1, 1)), bool, "Must return bool")
        test.assert_equals(type(was_package_received_yesterday(12, -11, 5, 6)), bool, "Must return bool")
    @test.it("Same from and to zone should return False")
    def _():
        test.assert_equals(was_package_received_yesterday(0, 0, 0, 0), False, "Same from and to zone should return False")
        test.assert_equals(was_package_received_yesterday(1, 1, 0, 1), False, "Same from and to zone should return False")
        test.assert_equals(was_package_received_yesterday(-11, -11, 12, 8), False, "Same from and to zone should return False")
    @test.it("East to zone 12 should return False")
    def _():
        test.assert_equals(was_package_received_yesterday(1, 5, 6, 3), False, "East to zone 12 should return False (to is greater than from)")
        test.assert_equals(was_package_received_yesterday(-11, -8, 3, 12), False, "East to zone 12 should return False (to is greater than from)")
    @test.it("West past midnight should return True")