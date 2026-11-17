def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for n in values:
        if n - 1 not in values:
            length = 1
            while n + length in values:
                length += 1
            best = max(best, length)
    return best
