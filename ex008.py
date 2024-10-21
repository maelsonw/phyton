#escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A media de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')