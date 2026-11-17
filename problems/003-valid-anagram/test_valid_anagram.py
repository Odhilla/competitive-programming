from valid_anagram import is_anagram


def test_anagram():
    assert is_anagram("anagram", "nagaram") is True


def test_not_anagram():
    assert is_anagram("rat", "car") is False


def test_different_lengths():
    assert is_anagram("ab", "abc") is False
