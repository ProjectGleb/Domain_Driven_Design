import pytest

@pytest.fixture(autouse=True)
def setup_env():
    # Automatically run for every test
    a = 1+1
    assert a ==20000000
    print("\nSetting up environment")

def test_example():
    assert True