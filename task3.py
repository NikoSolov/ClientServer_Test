def maxProfit(prices):
    min_price = 10**4
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

print(maxProfit([7,1,5,3,6,4]))  # 5
print(maxProfit([7,6,4,3,1]))    # 0
