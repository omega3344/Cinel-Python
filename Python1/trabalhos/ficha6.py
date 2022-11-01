#Exercicio1
'''
cidades = []

for i in range(5):
    cidades.append(input(f"Introduza o {i+1}º nome de cidade: ").title())

print(cidades)

'''
#Exercicio2
'''
def troca2 (lista,cidade1,cidade2):
    if cidade1 not in lista:
        return f"A cidade não está na lista"
    else:
        lista.remove(cidade1)
        lista.append(cidade2)
            
    return lista


def troca (lista,cidade1,cidade2):
    if cidade1 not in lista:
        return f"A cidade não está na lista"
    for pos, cid in enumerate (lista):
        if cid==cidade1:
            lista[pos]=cidade2
            
    return lista

cidades = ['Porto','Braga','Faro','Lisboa','Guimarães']

retirar = input('Indique o nome da cidade a retirar: ').title()

entrar = input('Indique o nome da cidade a colocar: ').title()

resp = troca(cidades,retirar,entrar)
    
print(resp)

cidades = ['Porto','Braga','Faro','Lisboa','Guimarães']

resp = troca2(cidades,retirar,entrar)
    
print(resp)
'''

#Exercicio3

'''
def elimina (lista,sai):
    if sai not in lista:
        return f"A cidade não está na lista"
    
    lista.remove(sai)

    return lista


cidades = ['Porto','Braga','Faro','Lisboa','Guimarães']

retirar = input('Indique o nome da cidade a retirar: ').title()

resp = elimina(cidades,retirar)

print(resp)

'''
#Exercicio4

'''
cidades = ['Porto','Braga','Faro','Braga','Lisboa','Porto','Guimarães','Faro']
print(cidades)

#print(list(set(cidades)))

lista = []

for nome in cidades:
    if nome not in lista:
        lista.append(nome)

print(lista)

'''
#Exercicio5

'''
def determina (numeros,x):
    conta = 0
    pos = []

    for p, n in enumerate (numeros):
        if n == x:
            conta += 1
            pos.append(p)
    return conta,pos


numeros = [3,5,7,5,4,2,3,7,9,7]

x = int(input('Indique o número a procurar: '))

resp = determina(numeros,x)
    
print(f'O número {x} aparece {resp[0]} vezes e nas posições {resp[1]}')

'''

#Exercicio6

'''
def maiores (numeros):
    for n in numeros:
        


numeros = [3,5,7,5,4,2,3,7,9,7]

resp = maiores(numeros)

print(resp)
'''

#Exercicio7








