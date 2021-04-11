'''
@author : Robernetes
'''

def to_roman():
    pass

def to_arabig():
    pass




out = False
while(not out):
    print()
    print('1. Convertir de Arabigo a Romano')
    print('2. Convertir de Romano a Arabigo')
    print('3. Salir')
    opt = int(input('Ingrese una opcion: '))
    if opt == 1:
        to_roman()
    elif opt == 2:
        to_arabig()
    elif opt == 3:
        print('Adios!')
        out = True
    else:
        print('Ingresa una opción que se encuentre en la lista!')
