dictx= {}

nums = True
while nums:
    name = input('whats your name boy?')
    response= input('where yo headed')
    
    dictx[name] = response
    
    repeat= input('would you like to let the next person respond? (yes/no)')
    if repeat == 'no':
        nums = False
        
print('\n-- Poll Results--')
for name,response in dictx.items():
    print(f'{name} is my name, and I\'m headed to {response}')
    

        

    
        
        
        
        
