from top_k_frequent import top_k_frequent


def test_top_two():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_single():
    assert top_k_frequent([1], 1) == [1]
