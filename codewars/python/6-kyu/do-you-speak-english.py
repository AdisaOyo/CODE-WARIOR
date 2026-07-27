def sp_eng(sentence): 
    # your code here
    sentence = sentence.lower()
    return sentence.__contains__("english")
@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals(sp_eng("english"), True)
        test.assert_equals(sp_eng("egnlish"), False)
        test.assert_equals(sp_eng("engliish"), False)
        test.assert_equals(sp_eng("1234egn lis;h"), False)
        test.assert_equals(sp_eng("1234english ;k"), True)
        test.assert_equals(sp_eng("English"), True)
        test.assert_equals(sp_eng("eNgliSh"), True)
        test.assert_equals(sp_eng("1234#$%%eNglish ;k9"), True)
        test.assert_equals(sp_eng("EGNlihs"), False)
        test.assert_equals(sp_eng("1234englihs**"), False)
        
    @test.it('Edge Test Case')
    def edge_test_case():
        test.assert_equals(sp_eng(""), False)