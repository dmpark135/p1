class User:
    def __init__(self, first_name, last_name, *xyz):
        self.first_name= first_name
        self.last_name= last_name
        self.xyz = xyz
        
        
        
    def describe_user(self, xyz):
        print(f'{first_name}, {last_name} {xyz}')        
 
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')
        
mike = User('mike', 'lee', 'ace')
print(f'Name : {mike.first_name} {mike.last_name} {mike.xyz}')

        
    
    