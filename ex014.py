#escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5 ) + 32 #lembrar da ordem de prescedencia
print(f'A temperatura de {c}ºC corresponde {f}ºF!')