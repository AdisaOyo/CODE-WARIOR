from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    first_name_alias = FIRST_NAME.get(f_name[0].upper())
    last_name_alias = SURNAME.get(l_name[0].upper())
    if first_name_alias is None or last_name_alias is None:
        return 'Your name must start with a letter from A - Z.'
    else:
        return f"{first_name_alias} {last_name_alias}"
    

import codewars_test as test
from solution import alias_gen

@test.describe("Fixed Tests")
def fixed_tests():
    basic_tests = (
        (('Mike', 'Millington'), 'Malware Mike'),
        (('Fahima', 'Tash'), 'Function T-Rex'),
        (('Daisy', 'Petrovic'), 'Data Payload'),
        (('Barny', 'White'), 'Beta Worm'),
        (('Hank', 'Kutz'), 'Half-life Killer'),
        (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
        (('walter', 'white'), 'WiFi Worm')
    )

    for names, result in basic_tests:
        @test.it('{} {}'.format(*names))
        def _():
            test.assert_equals(alias_gen(*names), result)