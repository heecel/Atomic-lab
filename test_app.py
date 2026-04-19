from app import get_user_status

def test_status_junior():
    assert get_user_status(15) == "Junior"

def test_status_senior():
    assert get_user_status(20) == "Senior"