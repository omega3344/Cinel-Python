#Ficha nº3

#Ex1

fp = open('dados.csv', 'r', encoding='UTF-8-SIG')
cont = fp.readlines()
#a

npessoas = len(cont)
#print(f"estão registados {npessoas} pessoas no ficheiro")

#b
qtN, qtC, qtS = 0,0,0
for linha in cont: #['Ana,Faro,22,Sul\n', 'Pedro,Porto,45,Norte\n',]
     #linha -> 'Ana,Faro,22,Sul\n'
     #dividir a linha pela ,
     dados = linha.split(",") #dados = ['Ana','Faro','22','Sul\n']
     local = dados[3] # local = 'Sul\n'
     if local[0] ==  'N': #local[0] obtém a primeira letra (N,C,S)
          qtN = qtN + 1
     elif local[0] == 'C':
          qtC = qtC + 1
     elif local[0] == 'S':
          qtS = qtS + 1
     
print(f"Norte: {qtN}")
print(f"Centro: {qtC}")
print(f"Sul: {qtS}")

#c
#cont variavém com lista de linhas do ficheiro
zona = input("Qual a zona do país que deseja determinar a média de idades? ").title()

while zona != 'Norte' and zona != 'Centro' and zona != 'Sul':
     zona = input("Qual a zona do país que deseja determinar a média de idades? ").title()

soma = 0 #irá somar as idades de todas as pessoas da zona indicada
for linha in cont: #['Ana,Faro,22,Sul\n', 'Pedro,Porto,45,Norte\n',]
     dados = linha.split(',') #dados = ['Ana','Faro','22','Sul\n']
     if zona[0] == dados[3][0]: #S  ul == S  ul\n
          idade = int(dados[2]) #dados[2] está representado como string
          soma = soma + idade


if zona[0]=='N': 
     qt = qtN 
elif zona[0]=='C':
     qt = qtC
else:
     qt = qtS
     
media = round(soma / qt, 0) #arredonda a 0 casas décimais  

print(f"A média de idades da zona {zona} é de {media}")

#d

#criar lista de todos os nomes
l_nomes = []
for linha in cont: #['Ana,Faro,22,Sul\n', 'Pedro,Porto,45,Norte\n',]
     dados = linha.split(',') #dados = ['Ana','Faro','22','Sul\n']
     if dados[0] not in l_nomes: #dados[0] é o nome da pessoa
          l_nomes.append(dados[0])


nome = input("Qual o nome a procurar? ").title()
while nome not in l_nomes:
     print("Nome não consta no ficheiro...")
     nome = input("Qual o nome a procurar? ").title()


for linha in cont: #['Ana,Faro,22,Sul\n', 'Pedro,Porto,45,Norte\n',]
     dados = linha.split(',') #dados = ['Ana','Faro','22','Sul\n']
     if nome == dados[0]: # Ana == Ana
          print(f"{nome}:{dados[1]}")





















