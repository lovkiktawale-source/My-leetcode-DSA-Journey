class Solution:

  def longestValidParentheses(self, s):
    stack = [-1]  # Base index for boundary calculation
    max_len = 0

    for i, char in enumerate(s):
      if char == "(":
        stack.append(i)
      else:
        stack.pop()
        if not stack:
          # Push current index as a new boundary when stack is empty
          stack.append(i)
        else:
          # Calculate length of the valid substring ending at i
          max_len = max(max_len, i - stack[-1])

    return max_len