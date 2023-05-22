
def f(ind,arr,dp):

    if ind == 0:
        return arr[ind]

    if dp[ind] != -1:
        return dp[ind]

    if(ind < 0):
        return 0

    pick = arr[ind] + f(ind-2, arr,dp)
    notPick = 0 + f(ind-1,arr,dp)

    dp[ind] = max(pick,notPick)
    return dp[ind]

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * (n)
        
        return f(n-1,nums,dp)
