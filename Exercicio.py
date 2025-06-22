dano = int(input("Digite o dano causado: "))
saude = 100

def calcular_saude(dano,saude):
    if saude -dano <=0:
        return "O personagem morreu"
    else:
        return "Personagem sobreviveu"


resultado = calcular_saude(dano, saude)
print(resultado)