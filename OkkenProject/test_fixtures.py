import pytest

@pytest.fixture(scope='module')
def something():
    """Return answer to ultimate question."""
    item1 = "slider"
    item2 = "loher"
    print(item1)
    yield item1 + item2
    print(item1 + item2)

@pytest.fixture(scope='module')
def calculate():
    """Use fixture return value in a test."""
    calc1 = 182
    calc2 = 150
    return calc1 - calc2

def test_function1(something):
    print(something)


#def test_function2(calculate):
 #   print(calculate)