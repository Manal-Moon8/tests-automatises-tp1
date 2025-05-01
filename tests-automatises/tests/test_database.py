import pytest
from app.database import Database

@pytest.fixture
def db():
    return Database()

def test_add_user(db):
    result = db.add_user("testuser", "test@example.com")
    assert result is True
    user = db.get_user("testuser")
    assert user["email"] == "test@example.com"

def test_get_nonexistent_user(db):
    user = db.get_user("nonexistent")
    assert user is None

def test_delete_user(db):
    db.add_user("todelete", "delete@example.com")
    result = db.delete_user("todelete")
    assert result is True
    assert db.get_user("todelete") is None

def test_delete_nonexistent_user(db):
    result = db.delete_user("ghost")
    assert result is False
