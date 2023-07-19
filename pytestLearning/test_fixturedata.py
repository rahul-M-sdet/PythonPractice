import pytest


@pytest.fixture(scope = "class")
def setup():
    print("I will be executing frst")
    yield
    print("I will execute last")


def dataload():
    print("user profile data is being created")
    return ("Rahul","Mishra","87rhlmishra@gmail.com")


