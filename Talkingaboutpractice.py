Jane = {'name': 'Lee','fav': 'hiking'}
monica = {'name':'Tse','fav':'food'}
page = {'name' : 'brusky','fav':'netflix'}

people = [Jane, monica]

for x in people:
    print(x)        
    
p1 = {'dog':'Dave'}
p2= {'bird':'Anne'}
p3 = {'cat':'Hatmaker'}

pets =[p1,p2,p3]

for x in pets:
    print(x)

favorite_places = {
        'ace':['seoul','usa','hk'],
        'brian':['vietnam','africa','london'],
        'dan':['china','oc','la']
        }
for key,value in favorite_places.items():
    print(f'This dude {key.title()}, loves getting chicks from:')
    for y in value:
        print(f'\t{y.title()}')
