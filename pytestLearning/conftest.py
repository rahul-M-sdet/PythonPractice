import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will show once will paid")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Mishra","87rhlmishra@gmail.com"]


@pytest.fixture(params=[("chrome","Rahul","Mishra"),("firefox","Mishra"),("IE","SS")])
def crossBrowser(request):
    return request.param
