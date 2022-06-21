
def f(ind,buy,prices,fee,dp):

    if(ind == len(prices)):
        return 0
    
    if(dp[ind][buy] != -1):
        return dp[ind][buy]
    
    if(buy):
        profit = max(-prices[ind] + f(ind+1,0,prices,fee,dp), 0 + f(ind+1,1,prices,fee,dp))
		
    else:
        profit = max(prices[ind]- fee + f(ind+1,1,prices,fee,dp), 0 + f(ind+1,0,prices,fee,dp))
        
    dp[ind][buy] = profit	
    return dp[ind][buy]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        dp =[[-1 for i in range(2)] for i in range(n)]
        
        return f(0,1,prices,fee,dp)
      
