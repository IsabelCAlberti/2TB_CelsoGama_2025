def calculadora():
    print("Calculadora simples\n")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    while True:
        operacao = input("Escolha a operação (1/2/3/4) ou 'sair' para encerrar: ")

        if operacao.lower() == 'sair':
            print("Calculadora encerrada. Até mais!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Operação inválida! Escolha entre 1, 2, 3, 4 ou 'sair'.\n")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Número inválido! Tente novamente.\n")
            continue

        if operacao == '1':
            resultado = num1 + num2
            simbolo = '+'
        elif operacao == '2':
            resultado = num1 - num2
            simbolo = '-'
        elif operacao == '3':
            resultado = num1 * num2
            simbolo = '*'
        elif operacao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida!\n")
                continue
            resultado = num1 / num2
            simbolo = '/'

        print(f"{num1} {simbolo} {num2} = {resultado}\n")


calculadora()
