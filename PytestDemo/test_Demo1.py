import pytest


@pytest.mark.smoke

def test_FirstProgram():
    print("Hello")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])
    print(crossBrowser[1])