names = ['ace', 'bees','cds']
print (f'{names[0]} please join us for dinner')
print (f'{names[1]} please join us for dinner')
print (f'{names[2]} please join us for dinner')

x="ace"
names.remove(x)
print(names)
print(x)

names.append('bob')
print (names)
print('we found more space')
names.insert(0,'xeno')
names.insert(int(len(names)/2),'fox' )
names.append('hero')
print(names)

print(f'{names.pop()} sorry your not invited')
print(f'{names.pop()} sorry your not invited')
print(f'{names.pop()} sorry your not invited')
print(f'{names.pop()} sorry your not invited')
print(f'{names[0]} your still invited')
del names[0:2]
print(names)
