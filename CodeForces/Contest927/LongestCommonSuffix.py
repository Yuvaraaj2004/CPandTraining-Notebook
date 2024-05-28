

from icecream import ic
from sortedcontainers import SortedDict
from typing import List


class Solution:
    def stringIndices(self, C: List[str], Q: List[str]) -> List[int]:
        d = [{}, 0]
        for ind, i in enumerate(C):
            root = d
            for j in i[::-1]+' ':
                if j not in root[0]:
                    root[0][j] = [{}, ind]
                else:
                    if len(C[root[1]]) > len(i):
                        root[1] = ind
                root = root[0][j]
        ans = []
        ic(d)
        for i in Q:
            ans.append(0)
            root = d
            print(i)
            for j in i[::-1]:
                # print(j,root)
                if j in root[0]:
                    ans[-1] = (root[1])
                    root = root[0][j]
                else:
                    ans[-1] = (root[1])
                    break
            if root[0].get(' ', None):
                ans[-1] = root[1]
        return ans


print(
    Solution().stringIndices(["abcdefgh", "poiuygh",
                              "ghghgh"], ["gh", "acbfgh", "acbfegh"])
)

print(Solution().stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]))

SortedDict()
