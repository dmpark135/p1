class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f'name of restaurant is {self.restaurant_name}.')
        print(f'dish specialty is {self.cuisine_type}.')
        
        
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')
        
xyz= Restaurant('mama mia','spagatti')
xyz.describe_restaurant()
xyz.open_restaurant()


abc = Restaurant('mcdonalds','big mac')
abc.describe_restaurant()
abc.open_restaurant()
