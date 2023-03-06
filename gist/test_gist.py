import pytest


def test_our_first_test() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    """With pytest.mark.skip is a built in mark which tells to pytest skip the test"""
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped because 4 > 1")
def test_should_be_skipped_if() -> None:
    """
       In the decorator the first argument is the condition that will make it run the test or not.
       The second argument of the decorator is just a string with some explanation about what the
       test could be skipped.
        This test make use of a built-in decorator that pytest marks to skip the test
        with a certain condition"""
    assert 1 == 2

"""
XFAIL: Is another built-in pytest mark(basically a decorator), and we usally use XFAIL
when we have test that we are OK with them of failing.
"""

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 2

# Custom Pytest marks

@pytest.mark.slow
def test_with_custom_mark1() -> None:
    passX

@pytest.mark.slow
def test_with_custom_mark2() -> None:
    pass
