class Solution(object):

  def plusOne(self, digits):
    """:type digits: List[int]

    :rtype: List[int]
    """
    # Iterate from the rightmost digit (least significant) to the leftmost
    for i in range(len(digits) - 1, -1, -1):
      # If current digit is less than 9, just increment it and return
      if digits[i] < 9:
        digits[i] += 1
        return digits

      # If digit is 9, it becomes 0 and carry continues to the next left digit
      digits[i] = 0

    # If all digits were 9 (e.g., [9, 9, 9]), we need an extra leading 1
    return [1] + digits