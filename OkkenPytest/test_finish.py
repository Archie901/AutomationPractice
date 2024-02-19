import pytest
import cards
from cards import Card, InvalidCardId


@pytest.mark.smok
@pytest.mark.exception
def test_start_non_existent(cards_db):
    """Shouldn't be able to start a non-existent card."""
    any_number = 123 # any number will be invalid, db is empty
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)