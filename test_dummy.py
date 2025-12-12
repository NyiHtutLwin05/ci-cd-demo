from app import check_credentials
def test_correct_credentials():
    assert check_credentials("admin", "1234") is True
def test_wrong_username():
    assert check_credentials("user", "1234") is False
def test_wrong_password():
    assert check_credentials("admin", "wrong") is False
def test_both_wrong():
    assert check_credentials("user", "wrong") is False