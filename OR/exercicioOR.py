print('Pergunta sobre Prioridade\n escolha uma opção abaixo:')
print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')

resposta = int(input('\nVocê é: '))

if resposta in [1, 2, 3]:
    print('\n✅ Você tem direito à fila prioritária!')
elif resposta == 4:
    print('\n🚫 Vá pra fila e aguarde')
else:
    print('\n❌ Opção inválida. Leia de novo e digite um número de 1 a 4.')
# Fim do código