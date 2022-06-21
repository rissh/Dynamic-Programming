
def f(ind,buy,prices,fee):

    if(ind == len(prices)):
        return 0
    
    if(buy):
        profit = max(-prices[ind] + f(ind+1,0,prices,fee), 0 + f(ind+1,1,prices,fee))
		
    else:
        profit = max(prices[ind]-fee + f(ind+1,1,prices,fee), 0 + f(ind+1,0,prices,fee))
		
    return profit 

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        return f(0,1,prices,fee)
      
