def to_freud(sentence):
  #your code here
  sentence = sentence.split()
  answer = ""
  for word in sentence:
    answer += ("sex ")
  return answer.strip()
import codewars_test as test
from solution import to_freud

@test.describe("Basic tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(to_freud("test"), "sex")
        test.assert_equals(to_freud("sexy sex"), "sex sex")
        test.assert_equals(to_freud("This is a test"), "sex sex sex sex")
        test.assert_equals(to_freud("This is a longer test"), "sex sex sex sex sex")
        test.assert_equals(to_freud("You're becoming a true freudian expert"), "sex sex sex sex sex sex")