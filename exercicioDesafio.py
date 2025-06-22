#Contador de Números Positivos, Negativos e Zeros
#Enunciado:
#Faça um programa que pede para o usuário digitar 5 números.
#Depois, o programa deve contar e exibir quantos desses números são:

#Positivos
#Negativos
#Zeros

#Regras:
#👉 Tem que usar um laço for
#👉 Tem que usar if e else pra fazer as verificações

positivos = 0 # Inicializa o contador de positivos
negativos = 0 # Inicializa o contador de negativos
zeros = 0 # Inicializa o contador de zeros

for i in range(5):  # Loop para solicitar 5 números
    numero = int(input(f"Digite o {i+1}º número: ")) # Solicita o número ao usuário

    if numero > 0: # Verifica se o número é positivo
        positivos += 1
    elif numero < 0: # Verifica se o número é negativo
        negativos += 1
    else: # Se não for positivo nem negativo, é zero
        zeros += 1

print("\nResultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
