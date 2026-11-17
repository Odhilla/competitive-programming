# 7. Longest Consecutive Sequence

**Summary:** Return the length of the longest run of consecutive integers in an unsorted array.

**Approach:** Put the values in a set. Start counting only from numbers whose predecessor is absent, so each run is walked once.

**Complexity:** Time O(n), space O(n).
