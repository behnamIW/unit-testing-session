def price_updater(prices, increase_rate):
    if isinstance(increase_rate, (int, float)):
        raise TypeError
    if increase_rate > 1 or increase_rate < 0:
        raise ValueError
    new_price_list = []
    for price in prices:
        if isinstance(price, (float, int)):
            new_price = price + (price * increase_rate)
            new_price_list.append(new_price)
        else:
            return "Incorrect Price Detected!"        
    return new_price_list
