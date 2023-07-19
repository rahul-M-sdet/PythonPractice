import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will execute last")


@pytest.fixture()

def dataLoad():
    print("I will edit the profile")
    return ["Rahul", "Mishra", "87rhlmishra@gmail.com"]


@pytest.fixture(params=[("Chrome","Rahul"),("Firefox","Mishra"),("IE","SS")])
def crossBrowser(request):
    return request.param
