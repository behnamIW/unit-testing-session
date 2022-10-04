def add_price(price_list): # No DI
    value = int(input("Please enter a number: ")) 
    price_list.append(value)
    return price_list
