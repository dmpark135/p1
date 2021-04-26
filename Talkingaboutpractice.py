z = ['sup','ho','bleh']
sent_messages = []
def show_messages(x):
    for word in x:
        y = f'word: {word.title()}'
        print(y)
        
def send_messages(x):
    while x:
        y = x.pop()
        print(f'here you go foo {y}')
        sent_messages.append(y)
send_messages(z[:])
print(sent_messages)
print(z)


        
                
    

        
    
        
        