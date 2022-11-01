#Exercicio 1
'''
frase = input ('Escreva uma frase:')

#Exercicio a)

print (frase)

#Exercicio b)

print (len(frase))

#Exercicio c)

print (frase.upper())
print (frase.lower())
print (frase.capitalize())

#Exercicio d)

print (frase.capitalize())
print (frase.title())

#Exercicio e)

def truncar (frase,a,b):
    return frase[a:b+1]

a = int(input('Indique um índice: '))
b = int(input('Indique um índice: '))

a,b = min(a,b), max (a,b)

resp = truncar(frase,a,b)
print (resp)

#Exercicio f)

def func2 (frase):
    return frase[::2]


resp = func2(frase)
print (resp)


#Exercicio g)

def trunc (frase,a):
    return frase[:a+1]

a = int(input('Indique um índice: '))

resp = trunc(frase,a)
print (resp)



#Exercicio h)

def trunc (frase,a):
    return frase[a:]

a = int(input('Indique um índice: '))

resp = trunc(frase,a)
print (resp)



#Exercicio i)


def truncar (frase,a,b):
    return frase[a::b]

a = int(input('Indique um índice: '))
b = int(input('Indique um salto: '))

resp = truncar(frase,a,b)
print (resp)



#Exercicio j)

def encontrar (frase,a):
    return frase.count(a)

a = str(input('Indique um caracter: '))

resp = encontrar(frase,a)

print (resp)



#Exercicio k)

def encontrar (frase,a):
    return frase.find(a)

a = str(input('Indique uma string: '))

resp = encontrar(frase,a)

print (resp) if resp>-1 else print ('a substring digitada não está contida na frase inicial')

'''

#Exercicio 2
'''

frase = input ('Escreva uma frase:')


def tamanho (frase):
    contador=0
    for i in frase:
        contador+=1
    return contador


resp = tamanho(frase)
print (f'O tamanho da frase é {resp}')

'''

#Exercicio3
'''

def contagem (texto):

    num=0
    ma=0
    mi=0

    for i in texto:

        if i.isnumeric()
            num += 1

        elif i.isupper()
            ma += 1
    
        elif i.islower() and i not in 'ºª'
            mi += 1

    return num, ma, mi


texto=str(input('Introduza um texto alfanumérico:'))

resp = contagem (texto)

print(f'No texto existem {resp[0]} números, {resp[1]} letras maiúsculas e {resp[2]} letras minúsculas')
'''

#Exercicio4

'''
nome=str(input('Introduza o seu nome completo:'))

print(nome.upper())
print (nome.lower())

esp = nome.count(' ')
print(f'O nome sem espaços tem {len(nome)-esp} caracteres')

lista = nome.split()

print(f'O primeiro nome tem {len(lista[0])} letras')

'''


#Exercicio5
'''

import random

num=random.randint(0,999999)
print(F'Número sorteado: {num}')
txt=str(num)[::-1]

lista=['Unidade','Dezena','Centena','Unidade milhar','Dezena milhar','Centena milhar']

for i in range (len(txt)):
    print(f'{lista[i]}:{txt[i]}',end=", ")

for p,i in enumerate(txt):
    print(f'{lista[p]}:{i}',end=", ")
'''

#Exercicio6
'''
def verifica (cidade):
    if cidade.find('Porto')==0:
        return True


cidade=str(input('Introduza o nome da cidade:')).title()

print ('O nome da cidade começa pela palavra "Porto"') if verifica(cidade) else print ('O nome da cidade não começa pela palavra "Porto"')

'''

#Exercicio7
'''
def verifica (nome):
    return 'Coelho' in nome

nome=str(input('Introduza o seu nome completo:')).title()

print ('O nome contem o apelido "Coelho"') if verifica (nome) else print ('O nome não contem o apelido "Coelho"')

'''


#Exercicio8


'''
nome=str(input('Introduza o seu nome completo:')).title()

nomes=nome.split()

print(f'Primeiro nome: {nomes[0]}\nÚltimo nome: {nomes[-1]}')


'''







