import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_FixtureDemo(self):
        print("I will execute methods in fixture demo")

    def test_FixtureDemo1(self):
        print("I will execute methods in fixture demo1")

    def test_FixtureDemo2(self):
        print("I will execute methods in fixture demo2")

    def test_FixtureDemo3(self):
        print("I will execute methods in fixture demo3")

    def test_FixtureDemo4(self):
        print("I will execute methods in fixture demo4")