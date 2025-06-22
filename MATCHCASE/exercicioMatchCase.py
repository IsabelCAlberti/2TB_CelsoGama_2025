#Enunciado: Calculadora simples de dias da semana
#O programa pede um número de 1 a 7 e mostra o dia da semana correspondente.

dia = int(input("Digite um número de 1 a 7: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido. Por favor, digite um número de 1 a 7.")