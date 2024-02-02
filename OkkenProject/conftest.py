from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture()
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()

def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"