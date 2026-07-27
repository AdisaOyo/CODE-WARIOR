def find_quarter_notes(time_signature):
    top, bottom = map(int, time_signature.split("/"))

    if bottom < 1 or bottom & (bottom - 1) != 0:
        return None

    return (top * 4) // bottom
import codewars_test as test
from solution import find_quarter_notes

sample_test_cases = [
    ('Standard time signatures', [
        ('4/4',   4),
        ('3/4',   3),
    ]),
    ('Eight-note denominators', [
        ('6/8',   3),
        ('9/8',   4),
    ]),
    ('Very small values', [
        ('1/8',   0),
        ('1/16',  0),
    ]),
    ('Invalid denominators', [
        ('9/0',  None),
        ('7/3',  None),