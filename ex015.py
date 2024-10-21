#escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo
#que o carro custa R$60 por dia e R$0,15 por Km rodado. 

d = int(input('Por quantos dias o carro foi utilizado? '))
k = float(input('Quantos Km foram percorridos? '))
c = (d * 60) + (k *0.15)
print(f'O valor do aluguel a ser pago será R${c:.2f}')