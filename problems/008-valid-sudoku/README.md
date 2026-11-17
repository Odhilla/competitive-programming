# 8. Valid Sudoku

**Summary:** Decide whether a partially filled 9x9 board breaks any row, column, or 3x3 box rule. Only the filled cells are checked.

**Approach:** Keep a set of seen digits for each row, column, and box. Use `(r // 3) * 3 + c // 3` to index the box.

**Complexity:** Time O(81), constant. Space O(81), constant.
