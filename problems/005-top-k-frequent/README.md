# 5. Top K Frequent Elements

**Summary:** Return the k most frequent values in an array.

**Approach:** Count frequencies with a hash map, then take the k most common entries.

**Complexity:** Time O(n log n) using `most_common`, space O(n). A bucket sort gives O(n) time if needed.
