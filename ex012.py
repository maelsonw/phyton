#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Preço do produto: '))
desc = preço * 5 / 100
res = preço - desc
print(f'O Valor do produto {preço:.2f}, com desconto de 5% será : {res:.2f}')