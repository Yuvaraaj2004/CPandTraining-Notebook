class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badindex = left = right = -1
        ans = 0
        for ind, i in enumerate(nums):
            if not minK <= i <= maxK:
                badindex = ind
            elif i == minK:
                left = ind
            elif i == maxK:
                right = ind
            print(nums[badindex:ind+1], badindex, left, right)
            ans += max(0, min(left, right)-badindex)
        return ans
