import pytest


@pytest.fixture(scope="class")
def setup():
    print("This will be executed first")
    yield
    print("This will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
