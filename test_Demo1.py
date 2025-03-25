# Any pytest file should start wih test_ keyword
# pytest method names should start with test
# any code should be wrapped in method only
# Method name should make sense
# -k stand for method names execution
#-s stand for logs in putput
#-v stands for more info metadata
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
#to skip specific test result but not the execution using @pytest.mark.xfail
#fixtures are used as setup & tear down methods for test cases
#conftest file to generalize fixtures and make it available for all test cases
# datadriven & parametrization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before the class is initiated and at the end




import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")
    print("Hello23")

@pytest.mark.xfail
def test_GreetCreditCard():
    print("Hello Shiv")
    print("Hello ShivAgain")

def test_crossBrowser(crossBrowser):
    print (crossBrowser)
