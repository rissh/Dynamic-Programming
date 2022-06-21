
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        ahead = [0 for i in range(2)]
        curr = [0 for i in range(2)]
        
        ahead[0] = ahead[1] = 0
            
        ind = n-1
        while(ind>=0):
		
            for buy in range(2):
                if(buy):
                    profit = max(-prices[ind]-fee + ahead[0], 0 + ahead[1])
					
                else:
                    profit = max(prices[ind] + ahead[1], 0 + ahead[0])
                    
                curr[buy] = profit
				
            ahead = [x for x in curr]    
            ind -= 1    
			
        return ahead[1]
      
