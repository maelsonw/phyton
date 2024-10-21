q = input('Digite algo: ')
q1 = 'O tipo primitivo desse valor é '
q2 = 'Só tem espaços?'
q3 = 'É um numero?'
q4 = 'É alfabético?'
q5 = 'É alfanúmerico?'
q6 = 'Está em maiúsculas?'
q7 = 'Está em minúsculas?'
q8 = 'Está capitalizada?'
print(f'{q1} , {type(q)}')  
print(f'{q2} {q.isspace()}')
print(f'{q3} {q.isnumeric()}')
print(f'{q4} {q.isalpha()}')
print(f'{q5} {q.isalnum()}')
print(f'{q6} {q.isupper()}')
print(f'{q7} {q.islower()}')
print(f'{q8} {q.istitle()}')