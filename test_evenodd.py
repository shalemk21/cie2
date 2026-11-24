
from even_odd import check_even_odd

def test_check_even_odd_even():
    result=check_even_odd(2)
    expected=f"2 is Even"

    assert result==expected


def test_check_even_odd_odd():
    result=check_even_odd(3)
    expected=f"3 is Odd"

    assert result==expected