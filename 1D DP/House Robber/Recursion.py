
def f(ind,arr):

    if ind == 0:
        return arr[ind]

    if(ind < 0):
        return 0

    pick = arr[ind] + f(ind-2, arr)
    notPick = 0 + f(ind-1,arr)

    return max(pick,notPick)

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        return f(n-1,nums)
