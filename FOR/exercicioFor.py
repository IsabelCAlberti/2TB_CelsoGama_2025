
numeros = [10, 15, 22, 33, 40, 51, 60, 73, 84, 95]

for numero in numeros: #se um valor está contido em uma sequência
    if (numero % 2 == 0 and numero % 3 == 0):
        print(f"{numero} é par e múltiplo de 3.")
    elif (numero % 2 == 0 or numero % 3 == 0):
        print(f"{numero} é par ou múltiplo de 3.")
    else:
        print(f"{numero} não é par nem múltiplo de 3.")