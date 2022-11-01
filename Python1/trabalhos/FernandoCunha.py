#Exercicio1
'''
import datetime

nome = str(input('Indique o seu nome: ')).title()
ano_nasc = int(input(f'{nome}, indique o seu ano de nascimento: '))

data = datetime.date.today()
ano_atual = int(data.strftime("%Y"))
idade = ano_atual - ano_nasc

print(f'A idade de {nome} é {idade} anos')
'''

#Exercicio2
'''
num1 = 0
while num1 == 0:
    num1 = int(input('Introduza um valor inteiro diferente de zero: '))
    
num2 = 0
while num2 == 0:
    num2 = int(input('Introduza um outro valor inteiro diferente de zero: '))

print(f'A soma de {num1} e {num2} é {num1+num2}')

print(f'A diferença entre {num1} e {num2} é {num1-num2}')

print(f'O produto de {num1} por {num2} é {num1*num2}')

print(f'O quociente da divisão de {num1} por {num2} é {num1//num2} e o resto é {num1%num2}')

'''

#Exercicio3
'''
nome = input('Indique o nome do aluno: ').title()
nota = -1

while nota < 0 or nota > 20:
    nota = int(input(f"Indique a nota do aluno {nome}: "))

if nota>19:
    clas='Excelente'
elif nota>15:
    clas='Bom'
elif nota>10:
    clas='Suficiente'
else:
    clas='Insuficiente'

print(f'O aluno {nome}, com uma nota de {nota} tem uma classificação de {clas}')

'''

#Exercicio4

'''
frase = "Programação em Python e Javascript"

expres = str(input('Introduza uma expressão: '))

#a)
print(f'O tamanho da frase é {len(frase)} e o tamanho da expressão é {len(expres)}')

#b)
if expres in frase:
    print(f'A expressão «{expres}» é uma substring da frase «{frase}»')
else:
    print(f'A expressão «{expres}» não é uma substring da frase «{frase}»')

#c)

nova_frase = frase.replace("Python",expres)

print(f'A nova frase é: {nova_frase}')

'''

#Exercicio5

'''
palavra = str(input('Introduza uma palavra: '))


if palavra == palavra[::-1]:
    print(f'A palavra {palavra} é palíndroma')
else:
    print(f'A palavra {palavra} não é palíndroma')

'''

#Exercicio6


def contagem (frase):

    crct=len(frase)
    num=0
    ma=0
    mi=0
    simb=0

    for i in frase:

        if i == ' ':
            crct -= 1
            
        elif i.isnumeric():
            num += 1

        elif i.isupper():
            ma += 1
    
        elif i.islower() and i not in 'ºª':
            mi += 1
        
        elif i in '.!?':
            simb += 1        

    return crct, num, ma, mi, simb

frase=str(input('Introduza uma frase: '))

resp = contagem(frase)

print(f'A quantidade de caracteres em «{frase}», sem espaços, é {resp[0]}')
print(f'Contém {resp[2]} maiúsculas, {resp[3]} minúsculas, {resp[1]} números e {resp[4]} símbolos')



#Exercicio 7
'''

from random import randint

lista = []

for i in range (15):
    lista.append(randint(20,30))

print(lista)

num=int(input('Introduza um número: '))

conta = 0
pos = []

for p, n in enumerate (lista):
        if n == num:
            conta += 1
            pos.append(p)

print(f'O número {num} ocorre {conta} vezes na lista acima e nos índices: {pos}')

'''

#Exercicio8

'''
lista_nomes = ['Ana','Joaquim','Maria','Manuel','Francisco']

print(lista_nomes)

nome = str(input('Introduza um nome: ')).title()

if nome not in lista_nomes:
    print(f"O nome {nome} não está na lista")
else:
    for i, n in enumerate (lista_nomes):
        if n == nome:
            del lista_nomes[i]

    print(f'Foi removido o nome {nome} da lista.')
    print(f'Nova lista: {lista_nomes}')
          
'''







