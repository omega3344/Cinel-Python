#exercicio1
'''
nome=input("introduza o seu nome: ")

try:
    fich = open("texto.txt","w", encoding="UTF-8")
    fich.write(nome)
    fich.close()

except:
    print("erro ao abrir o ficheiro")

'''

#exercicio2
'''

def junta_fich(f1,f2):

    try:
        fp1 = open(f1, "r", encoding="UTF-8")
        conteudo1 = fp1.read()
        fp1.close()
        
        if conteudo1[-1] != '\n':
            conteudo1 = conteudo1 + '\n'
            
        fp2 = open(f2, "r", encoding="UTF-8")
        conteudo2 = fp2.read()
        fp2.close()

        conteudofinal = conteudo1+conteudo2
        a=f1.rfind(".")
        b=f2.rfind(".")
        nome = f1[:a]+"_"+f2[:b]+".txt"
        
        fp3 = open(nome, 'w', encoding='UTF-8')        

        fp3.write (conteudofinal)
        fp3.close()
    except:
        print("erro")

    return 
        




nome1=input("indique o nome do primeiro ficheiro: ")

nome2=input("indique o nome do segundo ficheiro: ")

junta_fich (nome1, nome2)

'''


#exercicio3

'''

palavra=input("introduza a palavra a procurar: ")

try:
    fich = open("texto.txt","r", encoding="UTF-8")
    conteudo = fich.read()
    fich.close()
    n = conteudo.count(palavra)
    print(f"a palavra {palavra} aparece {n} vezes no ficheiro")

except:
    print("erro ao abrir o ficheiro")

'''

#exercicio4

'''
palavra1=input("introduza a palavra a ser substituída: ")
palavra2=input("introduza a palavra substituta: ")

try:
    fich = open("texto.txt","r", encoding="UTF-8")
    conteudo = fich.read()
    fich.close()
    
    conteudo = conteudo.replace(palavra1,palavra2)
    
    fich = open("texto.txt","w", encoding="UTF-8")
    fich.write(conteudo)
    fich.close()


except:
    print("erro ao abrir o ficheiro")

'''

#exercicio5

#alinea a)

'''
try:
    fich = open("pensamentos.txt","r", encoding="UTF-8")
    conteudo = fich.read()
    fich.close()
    
    conteudoLinhas = conteudo.split('\n')
    conteudoPalavras = conteudo.split(' ')
    
    if conteudoLinhas[-1] != '':
        qtLinhas = len(conteudoLinhas)
    else:
        qtLinhas = len(conteudoLinhas)-1
        
    print(f"a quantidade de linhas é {qtLinhas}")
    print(f"a quantidade de palavras é {len(conteudoPalavras)}")
    
    string = ''.join(conteudoPalavras)
    
    vogais = 'aeiouáéíóúàèìòùâêîôûãõ'
    qtvogais, qtconsoantes = 0, 0
    for simbolo in string:
        if simbolo.isalpha():
            if simbolo.lower() in vogais:
                qtvogais += 1
            else:
                qtconsoantes += 1
                
    print(f"a quantidade de vogais é {qtvogais}")
    print(f"a quantidade de consoantes é {qtconsoantes}")

except:
    print("erro ao abrir o ficheiro")



#alinea b)

plv=input("indique a palavra a procurar no texto: ")
qt = 0
linhas = []
for pos,txt in enumerate (conteudoLinhas):
    if txt.count(plv)>0:
        qt += txt.count(plv)
        linhas.append(pos+1)

print(f"a palavra {plv} aparece {qt} vez(es) e na(s) linha(s) {linhas}")

'''


#exercicio6


def junta_fich(f1,f2):

    try:
        fp1 = open(f1, "r", encoding="UTF-8")
        conteudo1 = fp1.read()
        fp1.close()
        
        if conteudo1[-1] != '\n':
            conteudo1 = conteudo1 + '\n'
            
        fp2 = open(f2, "r", encoding="UTF-8")
        conteudo2 = fp2.read()
        fp2.close()

        conteudofinal = conteudo1+conteudo2
        a=f1.rfind(".")
        b=f2.rfind(".")
        nome = f1[:a]+"_"+f2[:b]+".txt"
        
        fp3 = open(nome, 'w', encoding='UTF-8')        

        fp3.write (conteudofinal)
        fp3.close()
    except:
        print("erro")

    return 


junta_fich("fich1.txt", "fich2.txt")



