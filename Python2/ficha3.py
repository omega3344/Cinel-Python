#exercicio1

fp = open('dados.csv', 'r', encoding='UTF-8-SIG')
cont = fp.readlines()

#a

npessoas = len(cont)
#print(f'estão registadas {npessoas} pessoas no ficheiro')

#b

qtN, qtC, qtS = 0,0,0

for linha in cont:
    dados = linha.split(',')
    local = dados[3]
    if local[0] == 'N':
        qtN += 1
    elif local[0] == 'C':
        qtC +=1
    elif local[0] == 'S':
        qtS += 1

print(f'Norte: {qtN}')
print(f'Centro: {qtC}')
print(f'Sul: {qtS}')

#c

zona = input('Qual a zona do país que deseja determinar a média de idades? ').title()

while zona != 'Norte' and zona != 'Centro' and zona != 'Sul':
    zona = input('Qual a zona do país que deseja determinar a média de idades? ').title()

soma = 0

for linha in cont:
    dados = linha.split(',')
    local = dados[3]
    if zona[0] == dados [3][0]:
        idade = int(dados[2])
        soma = soma + idade

if zona[0] == 'N':
        qt = qtN
elif zona[0] == 'C':
        qt = qtC
else:
        qt = qtS

media = round(soma/qt,0)

print(f'A média de idades da zona {zona} é de {media}')

#d

lnomes = []

for linha in cont:
    dados = linha.split(',')
    if dados[0] not in lnomes:
        lnomes.append(dados[0])

nome = input('Qual o nome a procurar? ').title()
while nome not in lnomes:
    print('nome não consta no ficheiro...')
    nome = input('Qual o nome a procurar? ').title()

for linha in cont:
    dados = linha.split(',')
    if nome == dados[0]:
        print(f'{nome}:{dados[1]}')





