def draw_stairs(n):
    stairs = []

    for step in range(n):
        stairs.append(" " * step + "I")

    return "\n".join(stairs)
import codewars_test as test
from solution import draw_stairs


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(draw_stairs(3), '''I\n I\n  I''')
        test.assert_equals(draw_stairs(5), '''I\n I\n  I\n   I\n    I''')