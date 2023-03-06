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
    pass

@pytest.mark.slow
def test_with_custom_mark2() -> None:
    pass


class Company:
    """
    Just defining a test class
    """
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}: {self.stock_symbol}"

# Fixtures
"""
What is a fixture, is a function and we can also call fixtures as a pytest mark. 
A fixture is a function that is marked as a fixture. When we mark a function as a fixture we are 
telling to Pytest that we might use this function before and/or after running the test functions. 

"""
@pytest.fixture
def company() -> Company:
    """Function that is marked as a fixture and that is just creating a company object """
    return Company(name="Fiver", stock_symbol="FVRR")

def test_with_fixture(company:Company) -> None:
    """
    Just simple test that is using the company fixture.
    In this case  Pytest is going to look for a fixture function with the same name of the argument of
    the argument in the test function, so this function is using the fixture function company()
    :param company:
    :return: None
    """
    print(f"Printing {company} from fixture")

    # Pytest Parametrized
    """
    Pytest parametrized is a simply pytest very elegant way of running the same test over and over again 
    with different inputs.
    
    For make use of parametrized test we have to decorate the funcion with the mark parametrize.
    
    The fist argument of the decorator is the name of the variable we want to override, The second argument is a 
    list with the values that we want to override, with the varible of the first argument.
    We can also add labels to the tests with the different used values in each running of the test. 
    This can be e2asil y achieved with the IDS argument.    
    """

# Example
@pytest.mark.parametrize(
    "company_name",
    ["Tiktok", "Instagram", "Twitch"],
    ids=["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"]
)
def test_parametrized(company_name: str) -> None:
    """

    :param company_name:
    :return:
    """
    print(f"\nTest with{company_name}")

# PYTEST RAISES
"""
This is a context manager used for create test that is supposed to assert that we are raising some sort of 
exception. For this purpose we use pytest.raises context manager
"""


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)

