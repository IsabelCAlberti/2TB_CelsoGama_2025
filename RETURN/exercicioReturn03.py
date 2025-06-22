def inverte(nome, sobrenome):
    nomeInverso = sobrenome+","+nome
    return nomeInverso

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido = inverte(nome,sobrenome)

print("Olá", invertido)
