class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, served= 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = served
        
    def describe_restaurant(self):
        print(f'name of restaurant is {self.restaurant_name}.')
        print(f'dish specialty is {self.cuisine_type}.')
        
    def set_number_served(self):
        print(f'You been served {self.served}')
        
    def increment_number_served(self, given):
        if given >= self.served:
            self.served = given
        else:
            print(f'too much {self.served}')
        
        
        
        
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')
        
xyz= Restaurant('mama mia','spagatti', served = 80)
xyz.describe_restaurant()
xyz.open_restaurant()
xyz.set_number_served()

xyz.increment_number_served(90)
xyz.set_number_served()
