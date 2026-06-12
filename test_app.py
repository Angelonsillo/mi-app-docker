from app import suma

def test_suma_correcta():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0