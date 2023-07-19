import pytest

@pytest.mark.skip
def test_FirstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test case fail bcz both the string doesn't match"
@pytest.mark.smoke
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2==6,  "Addition do not match"

