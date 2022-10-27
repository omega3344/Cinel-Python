#Exercício1
'''
nome = input("Introduza o seu nome: ")

print (f"O seu nome é {nome}")
'''

#Exercício2
'''
nome = input ("Introduza o seu nome: ")
idade = input ("Introduza a sua idade: ")

print (f"O seu nome é {nome} e você tem {idade} anos")
'''

#Exercicio3
'''
num1 = int(input("Introduza o primeiro número inteiro: "))
num2 = int(input("introduza o segundo número inteiro: "))

print (f"A soma de {num1} e de {num2} é {num1+num2}")
print (f"A diferença entre {num1} e {num2} é {num1-num2}")
print (f"O produto de {num1} por {num2} é {num1*num2}")
print (f"O quociente de {num1} por {num2} é {num1//num2} e o resto é: {num1%num2}")
print (f"O quociente de {num1} por {num2} é {num1/num2:.2f}")
'''

#Exercicio4
'''
import datetime

nome = input("Indique o seu nome: ")
ano_nasc = int(input ("indique o seu ano de nascimento: "))
data = datetime.date.today()
ano_atual = int(data.strftime("%Y"))

print (f"A idade de {nome} é {ano_atual-ano_nasc} anos")
'''

#Exercicio5
'''
codigo = int(input("Indique o código do produto: "))

while codigo<101 or codigo>105:
    print (f"O código {codigo} não é válido!")
    codigo = int(input("Indique o código do produto: "))
    
quantidade = int(input("Indique a quantidade desejada: "))

match codigo:
    case 101:
        print (f"O total a pagar pelo Café é {0.25*quantidade}€")
    case 102:
        print (f"O total a pagar pela Meia de Leite é {0.35*quantidade}€")
    case 103:
        print (f"O total a pagar pelo Pão com manteiga é {0.25*quantidade}€")
    case 104:
        print (f"O total a pagar pelo Pão com fiambre é {0.40*quantidade}€")
    case 105:
        print (f"O total a pagar pelo Cachorro é {1.10*quantidade}€")
    case _:
        print (f"O código {codigo} não é válido!")
    
'''

#Exercio6
'''
num = int(input("Introduza um número inteiro: "))

if num%2==0:
    print(f"O número {num} é par e a sua metade é {num/2}")
else:
    print(f"O número {num} é impar e o seu triplo adicionado de um é {num*3+1}")

'''

#Exercicio7
'''
import math

diametro_roda = int(input("Introduza o diâmetro da roda: "))
kms = int(input("introduza o número de quilómetros percorridos: "))


perimetro = diametro_roda*math.pi
num_voltas = kms*100000/perimetro

print (f"A roda da bicicleta fez {num_voltas:.1f} voltas")
'''
#Exercicio8
'''
cels = int(input("Introduza a temperatura em graus Celsius: "))
fahr = (9*cels+160)/5
print(f"{cels} graus Celsius correspondem a {fahr} graus Fahrenheit")
'''

#Exercicio9
'''
fahr = int(input("Introduza a temperatura em graus Fahrenheit: "))
cels = (fahr-32)*(5/9)
print(f"{fahr} graus Fahrenheit correspondem a {cels:.2f} graus Celsius")
'''


#Exercicio10
'''
num1 = int(input("Introduza o 1º número inteiro: "))
num2 = int(input("Introduza o 2º número inteiro: "))
num3 = int(input("Introduza o 3º número inteiro: "))

#a)
print (f"A soma dos seus quadrados: {num1**2+num2**2+num3**2}")
#b)
print (f"O quadrado da sua soma: {(num1+num2+num3)**2}")
#c)
print (f"A sua média aritmética: {(num1+num2+num3)/3}")

'''

#Exercicio11
'''
escudos = float(input("Introduza a quantia em escudos: "))

euros = escudos / 200.482

print (f"O valor convertido em euros é de {euros:.2f}")
'''

#Exercicio12
'''
dia = int(input("Indique o número do dia da semana: "))

match dia:
    case 1:
        print (f"O {dia}º dia da semana é o Domingo")
    case 2:
        print (f"O {dia}º dia da semana é a Segunda-Feira")    
    case 3:
        print (f"O {dia}º dia da semana é a Terça-Feira")
    case 4:
        print (f"O {dia}º dia da semana é a Quarta-Feira")
    case 5:
        print (f"O {dia}º dia da semana é a Quinta-Feira")          
    case 6:
        print (f"O {dia}º dia da semana é a Sexta-Feira")
    case 7:
        print (f"O {dia}º dia da semana é o Sábado")
    case _:
        print ("Número de dia da semana inváliso!")

'''

#Exercicio13
'''
nome = input("Indique o nome do trabalhador: ")
num_horas = int(input("Indique o número de horas trabalhadas: "))
valor_hora = int(input("Indique o valor/hora a pagar: "))

salario = (num_horas*valor_hora)-((num_horas*valor_hora)*0.25)

print (f"O salário liquido a receber por {nome} é {salario}€")

'''

#Exercicio14
'''
num = int(input("Introduza um número: "))

print (f"O valor absoluto de {num}-2 é {abs(num-2)}")

'''


#Exercicio15
'''
preco = float(input("Introduza o preço do artigo: "))

if 5<preco<=25:
    desc = preco*.05
elif 25<preco<=50:
    desc = preco*.1
elif 50<preco<=75:
    desc = preco*.15   
elif preco>75:
    desc = preco*.30
else:
    desc = 0

print(f"O preço de saldo do artigo é {preco-desc}")
'''

    #versão mais eficiente
'''

preco = float(input("Introduza o preço do artigo: "))

if preco <= 5:
    desc = 0
elif preco<=25:    
    desc = preco*.05
elif preco<=50:
    desc = preco*.1
elif preco<=75:
    desc = preco*.15   
else:
    desc = preco*.30

print(f"O preço de saldo do artigo é {preco-desc}")
'''

#Exercicio16
'''
a = int(input("Introduza o valor para a variável A: "))
b = int(input("Introduza o valor para a variável B: "))

#aux = a
#a = b
#b = aux

#atribuição multipla
a, b = b, a

print(f"O valor das variáveis depois da troca é: A={a} e B={b}")        

'''

#Exercicio17
'''
a = int(input("Introduza o valor para a variável A: "))
b = int(input("Introduza o valor para a variável B: "))

if a>b:
    print(f"{a} é o maior número")
else:
    print(f"{b} é o maior número")

#função python
# print(max(a,b))

#função ternário
#print(f"{a} é o maior número") if a>b else print(f"{b} é o maior número")

'''

#Exercicio18
'''
int1 = int(input("Introduza o valor para o 1º número inteiro: "))
int2 = int(input("Introduza o valor para o 2º número inteiro: "))

if int1>int2:
    quociente = int1//int2
    resto = int1%int2
    print(f"O quociente da divisão é {quociente} e o resto é {resto}")
else:
    print("O 2ª número inteiro é menor que o 1º")

'''

#Exercicio19
'''
n = int(input("Introduza um número N: "))

if n>100:
    print("Blue")
elif n>10:
    print("Green")
else:
    print("Red")
'''

#Exercicio20
'''
a = int(input("Indique o 1º número: "))
b = int(input("Indique o 2º número: "))
c = int(input("Indique o 3º número: "))

if a>b :
    if b>c :
       print(f"Números ordenados: {a,b,c}")
    elif a<c :
       print(f"Números ordenados: {c,a,b}")
    else :
       print(f"Números ordenados: {a,c,b}")
else:
    if b>c :
        if a>c :
            print(f"Números ordenados: {b,a,c}")
        else :
            print(f"Números ordenados: {b,c,a}")
    else:
        print(f"Números ordenados: {c,b,a}")

'''

#Exercicio21
'''
a = int(input("Indique o valor de A: "))
b = int(input("Indique o valor de B: "))
c = int(input("Indique o valor de C: "))

soma = a+b

if soma > c:
    print(f'A soma de {a} e {b} é maior que {c}')
elif soma < c:
    print(f'A soma de {a} e {b} é menor que {c}')
else:
    print(f'A soma de {a} e {b} é igual a {c}')
'''

#Exercicio22
'''
a = int(input("Indique o 1º número: "))
b = int(input("Indique o 2º número: "))
c = int(input("Indique o 3º número: "))

if a<b :
    menor = a
else:
    menor = b
if c<menor:
    menor = c
print(f'O menor número é o {menor}')
'''

#Exercicio23
'''
iban = input('Qual o IBAN da conta: ')
saldo = float(input('Qual o saldo da conta: '))
op = input('Qual o tipo de operação (Crédito/Débito): ')
while op!='Crédito' and op!='crédito' and op!='Débito' and op!='débito':
    op = input('Operação errada! Qual o tipo de operação (Crédito/Débito): ')
valor = float(input(f'Qual o montante a movimentar no {op}: '))

if op=='Débito':
    saldo = saldo-valor
else:
    saldo = saldo +valor

if saldo<0:
    print('Conta bloqueada. Saldo negativo.')
else:
    print(f'O novo saldo após a operação é {saldo:.2f}€')

'''

#Exercicio24
'''
nome = input('Indique o nome do aluno: ')
a = float(input("Indique a 1ª nota: "))
b = float(input("Indique a 2ª nota: "))
c = float(input("Indique a 3ª nota: "))

media = (a+b+c)/3

print(f'O aluno {nome} tem as seguintes notas: {a} , {b} , {c} e uma média de {media:.2f}')
print('REPROVADO') if media<10 else print('APROVADO')
              
'''

#Exercicio25

'''
nome = input('Indique o nome do aluno: ')
nota = -1

while nota < 0 or nota > 100:
    nota = int(input(f"Indique a nota do aluno {nome}: "))

if nota>84:
    clas='Excelente'
elif nota>64:
    clas='Bom'
elif nota>49:
    clas='Suficiente'
else:
    clas='Insuficiente'

print(f'O aluno {nome}, com uma nota de {nota} tem uma classificação de {clas}')

'''

#Exercicio26
'''

lado1 = int(input('Indique o 1º lado do triângulo: '))
lado2 = int(input('Indique o 2º lado do triângulo: '))
lado3 = int(input('Indique o 3º lado do triângulo: '))

if lado1==lado2==lado3:
    print('O triângulo é equilátero')
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')

'''

#Exercicio27
'''
ang1 = int(input('Indique o 1º ângulo do triângulo: '))
ang2 = int(input('Indique o 2º ângulo do triângulo: '))
ang3 = int(input('Indique o 3º ângulo do triângulo: '))

if ang1==90 or ang2==90 or ang3==90:
    print('O triângulo é Retângulo')
elif ang1>90 or ang2>90 or ang3>90: 
    print('O triângulo é Obtusângulo')
else:
    print('O triângulo é Acutângulo')
 
'''

'''


a = int(input("Indique o 1º número: "))
b = int(input("Indique o 2º número: "))
c = int(input("Indique o 3º número: "))

if a>b and a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)

'''
'''

x = int (input('Digite o 1º número: '))
y = int (input('Digite o 2º número: '))
z = int (input('Digite o 3º número: '))



if x>y and x>z and y>z:
    print (f'{x} {y} {z}')

if x>y and x>z and y<z:
    print (f'{x} {z} {y}')

if x<y and y>z and x>z:
    print (f'{y} {x} {z}')

if x<y and y>z and x<z:
    print (f'{y} {z} {x}')

if z>y and z>x and x>y:
    print (f'{z} {x} {y}')

if z>y and z>x and x<y:
    print (f'{z} {y} {x}')


'''






    



        
