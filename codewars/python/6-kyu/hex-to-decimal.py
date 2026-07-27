def hex_to_dec(s):
    dec = 0
    num_pos = len(s)-1
    for hexa in s:
        
        if hexa.isalpha() == True:
            if hexa == 'a':
                dec += 10 * pow(16,num_pos)
            elif hexa == 'b':
                dec += 11 * pow(16,num_pos)
            elif hexa == 'c':
                dec += 12 * pow(16,num_pos)
            elif hexa == 'd':
                dec += 13 * pow(16,num_pos)
            elif hexa == 'e':
                dec += 14 * pow(16,num_pos)
            elif hexa == 'f':
                dec += 15 * pow(16,num_pos)
        elif hexa.isdigit() == True:
            dec += (int(hexa) * pow(16,num_pos))
        #else:
        #    dec += int(hexa)
        num_pos -= 1   
    return dec
import codewars_test as test
from solution import hex_to_dec

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hex_to_dec("1"), 1)
        test.assert_equals(hex_to_dec("a"), 10)
        test.assert_equals(hex_to_dec("10"), 16)