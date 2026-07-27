def bmi(weight, height):
    #your code here
    bmi = weight/pow(height,2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0 and bmi>18.5:
        return "Normal"
    elif bmi <= 30.0 and bmi>25.0:
        return "Overweight"
    elif bmi > 30.0:
        return "Obese"
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight", "For weight = 50 and height = 1.80")
        test.assert_equals(bmi(80, 1.80), "Normal", "For weight = 80 and height = 1.80")
        test.assert_equals(bmi(90, 1.80), "Overweight", "For weight = 90 and height = 1.80")
        test.assert_equals(bmi(100, 1.80), "Obese", "For weight = 100 and height = 1.80")