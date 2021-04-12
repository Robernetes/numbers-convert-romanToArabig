'''
Funcion para convertir numeros Arabigos a Romanos
'''


def to_romano(number):
    
    units = number % 10
    number = number // 10
    tens = number % 10
    number = number // 10
    hundreds = number % 10
    number = number // 10


    if hundreds is not None:
        if hundreds == 1:
            print('C', end="")
        elif hundreds == 2:
            print('CC', end="")
        elif hundreds == 3:
            print('CCC', end="")
        elif hundreds == 4:
            print('CD', end="")
        elif hundreds == 5:
            print('D', end="")
        elif hundreds == 6:
            print('DC', end="")
        elif hundreds == 7:
            print('DCC', end="")
        elif hundreds == 8:
            print('DCCC', end="")
        elif hundreds == 9:
            print('CM', end="")



    if tens is not None:
        if tens == 1:
            print('X', end="")
        elif tens == 2:
            print('XX', end="")
        elif tens == 3:
            print('XXX', end="")
        elif tens == 4:
            print('XL', end="")
        elif tens == 5:
            print('L', end="")
        elif tens == 6:
            print('LX', end="")
        elif tens == 7:
            print('LXX', end="")
        elif tens == 8:
            print('LXXX', end="")
        elif tens == 9:
            print('XC', end="")




    if units is not None:
        if units == 1:
            print('I', end="")
        elif units == 2:
            print('II', end="")
        elif units == 3:
            print('III', end="")
        elif units == 4:
            print('IV', end="")
        elif units == 5:
            print('V', end="")
        elif units == 6:
            print('VI', end="")
        elif units == 7:
            print('VII', end="")
        elif units == 8:
            print('VIII', end="")
        elif units == 9:
            print('IX', end="")

