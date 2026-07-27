def merge_arrays(first, second):
    c = []
    for x in first:
        c.append(x)
    for x in second:
        c.append(x)
    c.sort()
    c = list(dict.fromkeys(c))
    return c
    
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])        
    test.assert_equals(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])        