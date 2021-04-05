prompt = '\nTicket prices \n\t 0-3= $0 \n\t3-12 = $10 \n\t12+ =$15\n\t quit '
what = True
while what:
    x = input(prompt)
    
    
    if x =='quit':
        
        what = False 
    
    elif 0< int(x) < 3:
        print('$0')
    
    elif 3<int(x)<12:
        print('$10')
    else: 
        12<int(x)<200
        print('$15')
   
    
        
          
  
        
        

    
        
        
        
        
