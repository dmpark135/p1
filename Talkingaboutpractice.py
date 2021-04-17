def make_album(name,title, songs = None):
    x = {'name':name, 'title': title}
    if songs:
        x['songs']= songs
    return x

while True:
    print('\nPlease tell me the name of the album: ')
    print('(enter \'q\' at any time to quit)')
    
    n = input("name of artist: ")
    if n =='q':
        break
    
    t = input("title of album: ")
    if t == 'q':
        break
    
    s = input("songs name: ")
    if s == 'q':
        break
    
    info = make_album(n, t, s)
    print(f'\nHello, {info}')

