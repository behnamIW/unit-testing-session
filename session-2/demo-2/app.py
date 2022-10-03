import time
import random 


def get_todays_price_per_unit():
    time.sleep(3)
    return random.randint(1, 200)


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def get_price(self, my_get_todays_price_per_unit=get_todays_price_per_unit):
        price_per_unit = my_get_todays_price_per_unit() # Dependency
        return self.width * self.length * price_per_unit
