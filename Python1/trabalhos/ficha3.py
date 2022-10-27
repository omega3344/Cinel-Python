#Exercicio1
'''
a=int(input('Introduza um número: '))

print(f'O número anterior a {a} é o {a-1} e o número seguinte é o {a+1}')
'''

#Exercicio2
'''
from math import sqrt

x=int(input('Introduza um número inteiro positivo: '))

while x<1:
    x=int(input('Introduza um número inteiro positivo: '))

a= 2*x
b= 3*x
c= sqrt(x)
d= pow(x,(1/3))

print(f' O dobro de {x} é {a} \n O triplo de {x} é {b} \n A raiz quadrada de {x} é {c:.2f} \n e a raiz cúbica de {x} é {d:.2f}')

'''

#Exercio3

'''

a,b,c = int(input('Introduza três números inteiros: \n')), int(input()), int(input())

media=(a+b+c)/3

print(f'A média aritmética de {a, b, c} é {media:.2f}')

'''

'''
qt = int(input('Indique o número de valores a introduzir: '))

soma=0

for i in range(qt):
    a = int(input('Introduza um número inteiro: '))
    soma = soma + a
    
print(f'A média aritmética é {(soma/qt):.2f}')

'''


#Exercicio4
'''

a,b,c = int(input('Introduza três números inteiros: \n')), int(input()), int(input())

pa,pb,pc=float(input('Introduza o peso dos números introduzidos: \n')), float(input()), float(input())

media_ponderada = (a*pa + b*pb + c*pc)

print(f'A média ponderada de {a,b,c} com os pesos de {pa,pb,pc} é {media_ponderada}')

'''

#Exercicio5

'''
a = input("Introduza qualquer coisa: ")

print("A introdução é do tipo", type(a))
print("A introdução é numérica?", a.isnumeric())
print("A introdução é alfanumérica?", a.isalnum())
print("A introdução é alfabética?", a.isalpha())
print("A introdução está em maiúsculas?", a.isupper())
print("A introdução está em minúsculas?", a.islower())
print("A introdução está capitalizada?", a.istitle())

'''

#Exercicio6
'''

mt=float(input("Introduza os metros a converter: "))

print(f"Os múltiplos são:\n {mt/1000}km \n {mt/100}hm \n {mt/10}dam \n")

print(f"Os submúltiplos são:\n {mt*10}dm \n {mt+100}cm \n {mt+1000}mm \n")     

'''

#Exercicio7

'''
eur=float(input("Introduza o valor em euros a converter: "))
tx=float(input("Introduza a taxa de conversão EUR/USD: "))

print(f"O valor em dólares é: {eur*tx}")


'''

#Exercicio8

'''
altura=float(input("Indique a altura da parede: "))
largura=float(input("Indique a largura da parede: "))
tinta=float(input("Indique a quantidade de tinta a utilizar por m2: "))

area=altura*largura
perímetro= 2*(altura+largura)
tinta_gasta=area*tinta

print(f"A parede tem um perímetro de {perímetro} e uma área de {area} sendo necessários {tinta_gasta} litros de tinta")

'''

#Exercicio9

'''
preco = float(input("Indique o preço do artigo: "))
desc = float(input("Indique a percentagem do desconto: "))/100

print(f"O valor final a pagar é {preco-(preco*desc)}")

'''

#Exercicio10

'''

soma=0

for i in range(1,6):
    nota=-1
   
    while nota<0 or nota>20:
        nota = float(input(f"Indique a {i}ª nota: "))
        
    soma = soma + nota


media = soma/5

if media<10:
    print(f"O aluno tem uma média de {media}, sendo um mau aluno")
elif media<14:
    print(f"O aluno tem uma média de {media}, sendo um aluno médio")
elif media<=18:
    print(f"O aluno tem uma média de {media}, sendo um bom aluno")
else:
    print(f"O aluno tem uma média de {media}, sendo um aluno muito bom")                                                                                                               
'''

#Exercicio11
'''

num=int(input("Qual a tabuada a visualizar: "))

for i in range(1,11):
    print(f"{num}X{i}={num*i}")

'''
#Exercicio12

'''
import math

a = float(input("Introduza um valor: "))

print(f"O valor truncado de {a} é {math.trunc(a)}")
print(f"O valor arredondado de {a} é {round (a)}") 
print(f"O cubo do valor truncado de {a} é {math.pow(math.trunc(a),3)}")
print(f"A raiz quadrada do valor arredondado de {a} é {math.sqrt(round (a)):.4f}") 
print(f"O fatorial do valor arredondado ao inteiro seguinte de {a} é {math.factorial(math.ceil(a))}")

'''

#Exercicio13

'''
import random
from time import sleep

for i in range (10):
    print("Número aleatório entre 20 e 100: ",random.randint(20,100))
    sleep(1)
          
'''

#Exercicio14

'''
import random
from time import sleep

print("Os números sorteados são: ")
      
for i in range (5):
    print(random.randint(1,50))
    sleep(1)
      
print("As estrelas sorteadas são: ")
      
for i in range (2):
    print(random.randint(1,12))
    sleep(1)

'''













