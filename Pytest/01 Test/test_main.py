from main import get_weather

def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(19) == "hot"
        


# assert is a keyword used to check whether a condition is True.
# If the condition is False, it raises an AssertionError
# pytest uses this to determine whether a test passes or fails.