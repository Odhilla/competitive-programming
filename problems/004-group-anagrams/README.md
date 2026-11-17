# 4. Group Anagrams

**Summary:** Group the strings that are anagrams of each other.

**Approach:** Use the sorted characters of each word as a hash key and collect words that share a key.

**Complexity:** Time O(n * k log k), where k is the maximum word length. Space O(n * k).
