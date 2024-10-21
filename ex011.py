#faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidad de tinta necessaria para pintala, cada litro = 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area:.2f}m²')
print(f'Para pintar essa parede, você precisa de {tinta}l de tinta')