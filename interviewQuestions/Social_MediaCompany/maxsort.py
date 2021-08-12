""" Counting Sort """

def sol(unsorted_prices, max_price):
    prices_to_count = [0] * (max_price + 1)
    for price in unsorted_prices:
        prices_to_count[price] += 1
    sorted_prices = []
    
    for price,count in enumerate(prices_to_count):
        for time in range(count):
            sorted_prices.append(price)
    return sorted_prices

print(sol([1,2,3,4,5,4,3,2,9,11,45,14],45))