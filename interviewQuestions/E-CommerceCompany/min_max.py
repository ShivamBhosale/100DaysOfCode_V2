def profit(stock_prices):
    min_stock_price = stock_prices[0] #Starting the minimum price at index 0 
    max_profit = 0 #intializing the max value 0
    
    for price in stock_prices:
        min_stock_price = min(min_stock_price,price)
        
        comparision_profit = price - min_stock_price
        
        max_profit = max(max_profit,comparision_profit)
        
    return max_profit

print(profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))
        

def profit2(stock_prices2):
    min_stock_price2 = stock_prices2[0]
    max_profit2 = 0
    
    for prices2 in stock_prices2:
        min_stock_price2 = min(min_stock_price2,prices2)
        comparision_profit2 = prices2 - min_stock_price2
        max_profit2 = max(max_profit2,comparision_profit2)
        
    return max_profit2
print(profit2([10,12,14,12,13,11,8,7,6,13,23,50,11,10]))

def profit3(stock_prices3):
    if len(stock_prices3) < 2:
        raise Exception('Need at least two stock prices!')
    else:
        mini = min(stock_prices3)
        maxi = max(stock_prices3)
    
    return maxi - mini
print(profit3([10,12,14,12,13,11,8,7,6,13,23,50,11,10]))