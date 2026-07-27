def wrap(value):
    return {"value": value}
import codewars_test as test
from solution import wrap

@test.describe("example")
def test_group():
    @test.it("fixed_test")
    def test_case():
        res = wrap("my_test")
        test.assert_equals(res["value"], "my_test")
        test.assert_equals(wrap(343)["value"], 343)
        obj = {"test":"testy"}
        test.assert_equals(wrap(obj)["value"], obj)