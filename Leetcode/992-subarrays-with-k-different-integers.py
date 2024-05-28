class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            d, l, ans = {}, 0, 0
            for ind, i in enumerate(nums):
                d[i] = d.get(i, 0)+1
                while len(d) > k:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        del d[nums[l]]
                    l += 1
                ans += (ind-l+1)
            return ans
        return f(k)-(0 if k == 1 else f(k-1))
