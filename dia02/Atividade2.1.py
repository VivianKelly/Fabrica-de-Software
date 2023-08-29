'''
1 - Crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)

1 - Adicionar um input
2 - Verifique se tem a idade correta
3 - retorne se tem
'''

idade = (input("Digite sua idade:"))

try:
    if int(idade) >= 18:
        print("Pode obter a carteira de motorista")
    else:
        print("Não pode")
except:
    raise ValueError("Código inválido, digite sua idade em números")