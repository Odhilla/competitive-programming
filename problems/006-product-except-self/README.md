# 6. Product of Array Except Self

**Summary:** Return an array where each element is the product of all other elements, without using division.

**Approach:** Two passes. The first stores the product of everything to the left of each index. The second multiplies in the product of everything to the right.

**Complexity:** Time O(n), space O(1) beyond the output array.
