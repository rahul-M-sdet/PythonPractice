# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sence
# - k stands for method name execution, -s log in out put, -v stands for more info
# you can run specific file py.test <filename>
# you can mark (tag) @pytest.mark.smoke and then run with -m
# you can skip test by @pytest.mark.skip.
# pytest.mark.xfail
# fixtures are used to setup and tears down for test case
# Conftest file to generalize fixture and make it available to all test cases
# datadriven and pramitrisation can be done with return statement in tuple format.
# when u define fixture scope to  class only, it will run once before class is initiated and at the end.
import pytest


@pytest.mark.smoke
def test_firstprogram():
   print("Hello")


def test_crossBrowser(crossBrowser):
   print(crossBrowser[1])