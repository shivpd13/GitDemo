import pytest


@pytest.mark.usefixtures("setup")

class TestExample:


    def test_fixtureDemo(self):
        print("This will execute steps in fixtureDemo method")


    def test_fixtureDemo1(self):
        print("This will execute steps in fixtureDemo1 method")


    def test_fixtureDemo2(self):
        print("This will execute steps in fixtureDemo2 method")


    def test_fixtureDemo3(self):
        print("This will execute steps in fixtureDemo3 method")
