while True:
    print("\nMenu:")
    print("1 - Opção A")
    print("2 - Opção B")
    print("Digite 'sair' para encerrar.")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print("Você escolheu a Opção A.")
    elif escolha == '2':
        print("Você escolheu a Opção B.")
    elif escolha.lower() == 'sair':
        print("Encerrando o programa... Tchau!")
        break
    else:
        print("Opção inválida. Tente de novo.")
