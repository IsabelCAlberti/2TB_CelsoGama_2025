dano = int(input("Digite o dano: "))
saude = int(input("Digite a saúde: "))

def personagem_morreu(dano, saude):
    if saude - dano <= 0:
        return "O personagem morreu"
    else:
        return "O personagem sobreviveu"

resultado = personagem_morreu(dano, saude)
print(resultado)
