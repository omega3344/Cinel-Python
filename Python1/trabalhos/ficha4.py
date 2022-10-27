#Exercicio1
'''
def pot(base, exp): 
    
     prod = 1
     while exp > 0: # 5 4 3 2 1 0
          prod = prod * base  # 1 x 4 = 4x4 = 16 x 4 x 4 x 4
          exp -= 1 #exp = exp - 1

     return prod

base = int(input('Insira o valor da base: '))
exp = int(input('Qual o valor para representar o expoente? '))

res = pot(base, exp) 
print(f"{base} levantado a {exp} = {res}")
'''

#Exercicio2
'''
def fatorial(num): 
     
     x = 1 
     produto = 1 

     while x <= num:
          produto = produto * x 
          x = x + 1 
        
     return produto 

num = int(input("Insira valor inteiro positivo: "))
res = fatorial(num)
print(f"O fatorial de {num} é {res}")
'''

#Exercicio3
'''

def mdc(n1, n2):

     x = min(n1, n2)
     while x > 0:
          if   n1 % x == 0 and n2 % x == 0:
               return x     
          else:
               x = x - 1

n1 = 0
while n1 == 0:
     n1 = int(input("insira 1 nº inteiro positivo: "))

n2 = 0
while n2 == 0:
     n2 =  int(input("insira outro nº inteiro positivo: "))
   
res = mdc(n1, n2)

print(f"mdc({n1},{n2}) = {res}") #mdc(3,7) =  1
'''

#Exercicio4
'''
def somadiv(num):
     if num == 0:
          return 0 

     soma = num 
     x = 1
     lim = num // 2
     
     lista = [num] 
     
     while x <= lim:
          if num % x == 0: 
               soma = soma + x 
               
               lista.append(x) 
               
          x = x + 1 #x += 1

     print(f"Os divisores são {sorted(lista)}") #sorted(lista) -> ordena os elementos da lista
     return soma
    
num = int(input("Insira valor: "))
print(f"A soma dos divisores de {num} é {somadiv(num)}")
'''

#Exercico5
'''
from math import ceil, sqrt

def verifica(num):
     qtdiv = 2
     x = 2
     limite = ceil(sqrt(num))

     while x <= limite:
          if num%x == 0:
               return False

          x = x+1

     return True


num = int(input("insira valor igual ou superior a 2: "))

while num < 2: 
     num = int(input("Número inválido para verificação.\nInsira valor superior ou igual a 2: "))

resp = verifica(num)

print(f"{num} é primo") if resp else print(f"{num} não é primo")

'''


#Exercicio6
'''
def triangular (num):
     soma=0
     for x in range (1,num):
          soma += x
          if soma == num:
               return f"O número {num} é triangular"
          if soma > num:          
               return f"O número {num} não é triangular"

num=int(input("Insira um número: "))
print (triangular(num))

'''

#Exercicio7
'''

def fatorial (n):
     if n == 0 or n == 1:
          return 1
     return n*fatorial(n-1)

num = int(input("Indique um número: "))
resp = fatorial(num)
print (f"O fatorial de {num} é {resp}")

'''

#Exercicio8

'''
def pot (b, e):
     if e==0:
          return 1
     return b*pot(b,e-1)

base = int(input("Indique um número de base: "))
exp = int(input("Indique um número de base: "))
resp = pot(base,exp)
print (f"A potência de {base} elevado a {exp} é {resp}")

'''

