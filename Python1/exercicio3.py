#Exercicio3
'''
texto=str(input('Introduza um texto alfanumérico:'))

num=0
ma=0
mi=0

for i in range(0,len(texto)):
    
    if ord(texto[i])>47 and ord(texto[i])<58:
        num += 1

    if ord(texto[i])>64 and ord(texto[i])<91:    
        ma += 1
    
    if ord(texto[i])>96 and ord(texto[i])<123:
        mi += 1

print(f'No texto existem {num} números, {ma} letras maiúsculas e {mi} letras minúsculas')

'''
#Exercicio4
'''

nome=str(input('Introduza o seu nome completo:'))

print(nome.upper())
print (nome.lower())

esp=nome.count(' ')
print(f'O nome sem espaços tem {len(nome)-esp} caracteres')

lista = nome.split()

print(f'O primeiro nome tem {len(lista[0])} letras')


'''

#Exercicio5
'''
import random

num=random.randint(0,999999)
print(num)
txt=str(num)[::-1]
print(txt)

lista=('Unidade','Dezena','Centena','Unidade milhar','Dezena milhar','Centena milhar')

for i in range (len(txt)):
    print(f'{lista[i]}:{txt[i]}',end=", ")

'''

#Exercicio6

'''
cidade=str(input('Introduza o nome da cidade:'))

print ('O nome da cidade começa pela palavra "Porto"') if cidade.find('Porto')==0 else print ('O nome da cidade não começa pela palavra "Porto"')

'''


#Exercicio7

'''

nome=str(input('Introduza o seu nome completo:'))

print ('O nome contem o apelido "Coelho"') if 'Porto' in cidade else print ('O nome não contem o apelido "Coelho"')


'''

#Exercicio8

nome=str(input('Introduza o seu nome completo:'))

nomes=nome.split()

print(f'Primeiro nome: {nomes[0]}\nÚltimo nome: {nomes[len(nomes)-1]}')














