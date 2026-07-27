geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    for x in geese:
        if x in birds:
            birds.remove(x)
    return birds
import codewars_test as test
from solution import goose_filter

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
        test.assert_equals(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
        test.assert_equals(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),[])