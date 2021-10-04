
from functools import lru_cache

class Stock:
    def maxProfit(self, share_price):
        
        
        @lru_cache(maxsize=None)
        def get_best_profit(day, have_stock):
            if day<0:
                return 0 if not have_stock else -float('inf')
            
            price = share_price[day]
            
            if have_stock:
                strategy_sell = get_best_profit(day-1, False) - price
                strategy_hold = get_best_profit(day-1, True)
                return max(strategy_hold, strategy_sell)
            else:
                strategy_buy = get_best_profit(day-1, True) + price
                strategy_avoid = get_best_profit(day-1, False)
                return max(strategy_buy, strategy_avoid)
            
        return get_best_profit(len(share_price)-1, False)


a = Stock()

print(a.maxProfit([3,2,6,5,0,3]))
            
            
                        
            
        
        