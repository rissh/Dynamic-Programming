
def f(ind,buy,prices):

    if(ind >= len(prices)):
        return 0
    
    if(buy):
        profit = max(-prices[ind] + f(ind+1,0,prices), 0 + f(ind+1,1,prices))
		
    else:
        profit = max(prices[ind] + f(ind+2,1,prices), 0 + f(ind+1,0,prices))
		
    return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        return f(0,1,prices)
      
