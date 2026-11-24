from even_odd import check_even_odd

def check_even_odd_test():
    result=check_even_odd(2)
    excepted=f"2 is Even"

    assert result==excepted


def check_even_odd_test_odd():
    result=check_even_odd(3)
    excepted=f"3 is Odd"

    assert result==excepted
