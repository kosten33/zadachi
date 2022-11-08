mapa = {1:'Зима',
        2:'Зима',
        3:'Весна',
        4:'Весна',
        5:'Весна',
        6:'Лето',
        7:'Лето',
        8:'Лето',
        9:'Осень',
        10:'Осень',
        11:'Осень',
        12:'Зима'}

a = int(input())

if(a < 3 or a == 12):
    print('From if', 'Зима')

elif(a > 2 and a < 6):
    print('From if', 'Весна')

elif(a > 5 and a < 9):
    print('From if', 'Лето')

else:
    print('From if', 'Осень')
    


print('From map', mapa.get(a))
