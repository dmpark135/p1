z = ['sup','ho','bleh']

def show_messages(x):
    for word in x:
        y = f'word: {word.title()}'
        print(y)
    
show_messages(z)