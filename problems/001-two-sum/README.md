# 1. Two Sum

**Summary:** Given an array of integers and a target, return the indices of two numbers that add up to the target.

**Approach:** One pass with a hash map from value to index. For each number, check whether its complement has already been seen.

**Complexity:** Time O(n), space O(n).
