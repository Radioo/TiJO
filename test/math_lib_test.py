from src.math_lib import my_max, my_is_perfect, my_is_prime, luhn_checksum

def test_max():
    assert my_max(None) is None
    assert my_max([]) is None
    assert my_max([1]) == 1
    assert my_max([2, 1]) == 2
    assert my_max({}) is None

def test_is_perfect():
    assert my_is_perfect(None) == False
    assert my_is_perfect(-1) == False
    assert my_is_perfect(0) == False
    assert my_is_perfect(1) == False
    assert my_is_perfect(6) == True
    assert my_is_perfect(7) == False
    assert my_is_perfect(28) == True
    assert my_is_perfect([123]) == False
    assert my_is_perfect({}) == False

def test_is_prime():
    assert my_is_prime(None) == False
    assert my_is_prime("1") == False
    assert my_is_prime({}) == False
    assert my_is_prime(-1) == False
    assert my_is_prime(0) == False
    assert my_is_prime(1) == False
    assert my_is_prime(2) == True
    assert my_is_prime(3) == True
    assert my_is_prime(4) == False
    assert my_is_prime(5) == True
    assert my_is_prime(6) == False
    assert my_is_prime(7) == True
    assert my_is_prime(8) == False
    assert my_is_prime(9) == False
    assert my_is_prime(10) == False
    assert my_is_prime(2131) == True
    assert my_is_prime(3089) == True
    assert my_is_prime(7919) == True
    assert my_is_prime(7920) == False

def test_luhn_checksum():
    assert luhn_checksum(17893729974) == True
    assert luhn_checksum(17893729975) == False

if __name__ == "__main__":
    test_max()
    print("test_max passed")

    test_is_perfect()
    print("test_is_perfect passed")

    test_is_prime()
    print("test_is_prime passed")

    test_luhn_checksum()
    print("test_luhn_checksum passed")