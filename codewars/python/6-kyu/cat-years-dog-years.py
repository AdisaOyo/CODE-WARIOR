def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat_years = 0
    dog_years = 0
    count = 0
    for x in range(human_years):
        count += 1
        if count == 1:
            cat_years += 15
            dog_years += 15
        if count == 2:
            cat_years += 9
            dog_years += 9
        if count > 2:
            cat_years += 4
            dog_years += 5 

    return [human_years,cat_years,dog_years]
import codewars_test as test
from solution import human_years_cat_years_dog_years

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("one")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(1), [1,15,15])
    @test.it("two")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(2), [2,24,24])
    @test.it("ten")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(10), [10,56,64])