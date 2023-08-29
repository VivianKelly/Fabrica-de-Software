'''
2. Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. Mostre que ele foi multado, a multa é de 7R$ por cada km acima do limite.
'''

velocidade = input("Digite a velocidade do carro: ")

velocidade_float = 0

try:
    velocidade_float = float(velocidade)
except ValueError:
    raise ValueError("Código inválido, digite a velocidade em números.")

if velocidade_float > 80:
    print(f"A velocidade {velocidade} é acima do limite.")
    print(f"Você foi multado em {(velocidade_float - 80) * 7} R$ reais.")
else:
    print("Velocidade no limite permitido.")