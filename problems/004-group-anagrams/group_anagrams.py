from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())
