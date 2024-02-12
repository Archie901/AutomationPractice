import pytest
import random

@pytest.fixture(scope='function')
def randomizer():
    return random.choice()

def test_something(randomizer):
    list1 = ['123213', 'fdgdfgdf', '8-4234']
    list2 = [12312, 5555, 67776]
    result = randomizer(list1) + randomizer(list2)
    print(result)