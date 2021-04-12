'''
Funcion para convertir numeros romanos a arabigos
'''

def to_arabigo(letras):
    value = [ 1000, 500, 100, 50, 10, 5, 1 ]
    symbols = "MDCLXVI"
    i = 0
    last_value = 0
    response = 0
    correct = True
    while correct and i < len(letras):
        letra = letras[i]
        index = symbols.find(letra)
        if index >= 0:
            response = response + value[index]

            if value[index] > last_value:
                response = response - (2 * last_value)
            
            last_value = value[index]

        else:
            correct = False
            response = -1

        i+=1

    print(f'Return : {response}')