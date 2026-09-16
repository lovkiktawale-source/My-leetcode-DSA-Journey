class Solution:

  def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    def backtrack(start: int, path: list[int]):
      res.append(path.copy())

      for i in range(start, len(nums)):
        # Skip duplicates at the same level of recursion
        if i > start and nums[i] == nums[i - 1]:
          continue

        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

    backtrack(0, [])
    return res