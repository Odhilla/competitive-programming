from group_anagrams import group_anagrams


def test_groups():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(g) for g in result)
    assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_empty_string():
    assert group_anagrams([""]) == [[""]]
