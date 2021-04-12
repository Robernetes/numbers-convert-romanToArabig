'''
@author : Robernetes

Ejecutar solo este archivo main
'''
from to_roman import to_romano
from to_arabig import to_arabigo

out = False
while(not out):
    print()
    print('1. Convertir de Arabigo a Romano')
    print('2. Convertir de Romano a Arabigo')
    print('3. Salir')
    opt = int(input('Ingrese una opcion: '))
    if opt == 1:
        number = int(input('Ingresa un numero entre 1 - 100: '))
        to_romano(number)
        print()
    elif opt == 2:
        letras = input("Ingresa numero en romano: ").upper()
        to_arabigo(letras)
    elif opt == 3:
        print('Adios!')
        out = True
    else:
        print('Ingresa una opción que se encuentre en la lista!')
