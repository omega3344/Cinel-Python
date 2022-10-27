#Exercicio1
'''
num=int(input("introduza um número: "))
soma=0

for i in range(1,num+1):
    soma = soma+i

print(f'A soma é {soma}')

'''

#Exercicio2

'''
num=int(input("introduza um número inteiro: "))
divisores = []

for i in range (1,num+1):
    if num%(i)==0:
        divisores = divisores + [i]

print(f'Os divisores de {num} são: {divisores}')
        
'''

#Exercicio3
'''
num=int(input("introduza um número inteiro: "))
contador=2
limite=int(num**0.5)

for i in range (2,limite+1):
    if num%(i)==0:
        contador = 3
        break
        
if contador == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')

'''


#Exercicio4
'''

num=int(input("introduza um número inteiro: "))
soma=0

for i in range (1,num+1):
    if num%(i)==0:
        soma = soma + i

print(f'A soma dos divisores de {num} é {soma}')


'''

#Exercicio5
'''
num=int(input("introduza um número inteiro menor que 50: "))

fatorial=1

for i in range(2,num+1):
    fatorial = fatorial*i

print(f'O fatorial de {num} é {fatorial}')

'''

#Exercicio6
'''
idade=int(input('Introduza a sua idade: '))

while idade<0:
    idade=int(input('Idade errada. Introduza a sua idade: '))

if idade<3:
    print('Você é um bebé')
elif idade<13:
    print('Você é uma criança')
elif idade<18:
    print('Você é um adolescente')
else:
    print('Você é um adulto')
'''

#Exercicio7
'''
num=int(input("introduza um número inteiro: "))
soma=0

for i in range (1,num):
    if num%(i)==0:
        soma = soma + i

if soma==num:
    print(f'O número {num} é um número perfeito')
else:
    print(f'O número {num} não é um número perfeito')

'''

#Exercicio8
'''
num=int(input("introduza um número inteiro: "))
soma=0

while num>0:
    soma = soma + num%10
    num = num//10

print(f'A soma dos digitos é: {soma}')    

'''


#Exercicio9
'''
num = int(input("introduza um numero inteiro (>1): "))

fator = 2

while num != 1:
    mult = 0;
    while num%fator == 0:
        num = num / fator;
        mult = mult + 1;

    if mult != 0:
        print(f"fator {fator} elevado a {mult}")

    fator = fator + 1

'''















