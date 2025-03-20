# Any pytest file should start wih test_ keyword
# pytest method names should start with test
# any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "Hi", "Test Failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"



@pytest.fixture()
def setup():
    print("This will be executed first")


def test_fixtureDemo(setup):
    print("This will execute steps in fixtureDemo method")