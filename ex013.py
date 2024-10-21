#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input('Qual o seu salario? '))
#ajuste = salario + (salario * 15 / 100) ou (salario *0.15)
ajuste = salario * 15 / 100
res = salario + ajuste
print(f'O seu salario de {salario:.2f} com aumento de 15% ficará: {res:.2f}')