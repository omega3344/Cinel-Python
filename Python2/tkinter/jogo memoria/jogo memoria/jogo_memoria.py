####################################################################################################
#                                        JOGO DA MEMÓRIA                                           #
#                                           Versão 3.0                                             #
####################################################################################################


#importar bibliotecas

from tkinter import *
from tkinter import ttk
import tkinter as tk
import winsound
import random
import time
import os
import sys


#FUNÇÕES:


    
    #global img1, img2, img3, img4, img5, img6, img7, img8, inicio, tema
    

#janela de arranque do jogo

def jan_init ():

    #atribui escolha do tema

    def atribuir_tema():

        global tema
        tema = combo.get()
        init.destroy()

    #criar janela de arranque do jogo

    init = Tk()
    in_l = 300
    in_a = 300
    centrar(init, in_l, in_a)
    init['bg']=('Linen')
    init.resizable(0,0)
    init.wm_overrideredirect(True) 
    init.focus_force()


    #criar combobox com temas de jogo
    
    temas = ['Frutas', 'Cores', 'Animais', 'Formas', 'Super-Heróis']

    lab = Label(init, text='Escolha o tema do jogo', bg = 'Linen', font= ('Helvetica', 18, 'bold'))
    lab.pack(pady=25)
    combo = ttk.Combobox(init, values = temas, textvariable = tk.StringVar(), width=30, font= ('Helvetica', 10, 'bold'))
    combo.set(temas[2])
    combo.configure(state='readonly', justify='center')
    combo.pack(pady=10)

    #criar botão de escolha para iniciar jogo

    ini = Button(init, text = "Iniciar jogo", font= ('Helvetica', 15, 'bold'), command = atribuir_tema)
    ini.pack(pady=15)

    init.mainloop()


#(re)iniciar o jogo

def iniciar():

    global pares, vencedor, lista_btn, lista_resp, dict_resp, jogadas, cont, tema

    #definição de variáveis

    vencedor = 0
    jogadas = 0
    cont = 0
    lista_resp = []
    dict_resp = {}

    #criar emparelhamento e baralhar imagens

    pares = [img1, img1, img2, img2, img3, img3, img4, img4, img5, img5, img6, img6, img7, img7, img8, img8]
    random.shuffle(pares)


#limpar caixas de texto e botões

def limpar():

    iniciar()
    njoga['text']=(f'Número de jogadas: {jogadas}')
    rec['text']=(f'Recorde de jogadas: {recorde}')
    legenda.config(text='', bg='Bisque',)
    nome['bg']=('Bisque')
    copyr['bg']=('Bisque')
    for btn in lista_btn:
        btn.config(image=inicio, state='normal', cursor='hand2', relief='groove')
    janela['bg']=('Bisque')


#jogo concluído

def vitoria():

    global jogadas, recorde
    
    legenda.config(text='PARABÉNS!!!', bg= 'Coral1',)
    nome['bg']=('Coral1')  
    copyr['bg']=('Coral1')      
    janela['bg']=('Coral1')
    janela.update()
    time.sleep(1)
    legenda['text']=(f'Terminou o jogo em {jogadas} jogadas!')
    janela.update()
    winsound.PlaySound('./sons/vitoria.wav', winsound.SND_FILENAME)
    
    
    if jogadas < recorde:
        recorde = jogadas
        gravarrec(recorde)
        time.sleep(1)
        legenda['text']=(f'Conseguiu um NOVO RECORDE!')


#verificar emparelhamento ao clicar nos botões

def click_botao(b, num):

    global cont, lista_resp, dict_resp, vencedor, lista_certo, lista_errado, jogadas

    if num not in lista_resp:

        if cont < 2:
            b['image'] = pares[num] 
            lista_resp.append(num)
            dict_resp[b] = pares[num]
            cont += 1
        
        if len(lista_resp) == 2:
            jogadas += 1 
            njoga['text']=(f'Número de jogadas: {jogadas}')

            if pares[lista_resp[0]] == pares[lista_resp[1]]:  
                legenda['text']=(lista_certo[random.randint(0,3)])
                for chave in dict_resp:
                    chave.config(state='disable', cursor='arrow', relief='sunken')
                janela.update()
                winsound.PlaySound('./sons/certo.wav', winsound.SND_FILENAME)    
                cont = 0
                lista_resp = []
                dict_resp = {}
                vencedor += 1
                if vencedor == 8:
                    vitoria()    
                else:
                    legenda['text']=('')
            else:  
                cont = 0
                lista_resp = []
                legenda['text']=(lista_errado[random.randint(0,5)])
                janela.update()
                time.sleep(0.5)
                winsound.PlaySound('./sons/errado.wav', winsound.SND_FILENAME)     
                legenda['text']=('')
                for chave in dict_resp:
                    chave['image'] = inicio
                dict_resp = {}   


#centrar janela

def centrar (jan, jan_l, jan_a):

    ecra_l = jan.winfo_screenwidth()
    ecra_a = jan.winfo_screenheight()
    posx = ecra_l//2 - jan_l//2
    posy = ecra_a//2 - jan_a//2
    jan.geometry(f'{jan_l}x{jan_a}+{posx}+{posy}')


#gravar ficheiro com novo recorde

def gravarrec(recorde):

    try:
        
        fich = open('recorde.txt', 'w', encoding='UTF-8-SIG')
        fich.write(str(recorde))
        fich.close()

    except:
        
        print("Erro ao gravar ficheiro!")


#PROGRAMA PRINCIPAL:

#inicializar temas de jogo

jan_init()


#criar janela do jogo

janela = Tk()
jan_l = 800
jan_a = 930
centrar(janela, jan_l, jan_a)
janela['bg']=('Bisque')
janela.resizable(0,0)
janela.wm_overrideredirect(True)


#criar label para nome do jogo

nome = Label(janela, text=f'JOGO DA MEMÓRIA', bg='Bisque', font= ('Helvetica', 20, 'bold'))
nome.pack(pady = 10)


#criar contentor superior para mensagens

contentor = Frame(janela, bg='lightyellow', highlightbackground="black", highlightthickness=1)
contentor.pack(pady=10)


#criar contentor para tabuleiro de jogo

frame = Frame(janela)
frame.pack(pady=10)


#importar valor do recorde

try:
    
    fich = open('recorde.txt', 'r', encoding='UTF-8-SIG')
    recorde = int(fich.read())
    fich.close()

except:
    
    recorde = 50
    

#importação de imagens

img1 = PhotoImage(file = f'./imagens/{tema}/imagem1.png').subsample(2,2)
img2 = PhotoImage(file = f'./imagens/{tema}/imagem2.png').subsample(2,2)
img3 = PhotoImage(file = f'./imagens/{tema}/imagem3.png').subsample(2,2)
img4 = PhotoImage(file = f'./imagens/{tema}/imagem4.png').subsample(2,2)
img5 = PhotoImage(file = f'./imagens/{tema}/imagem5.png').subsample(2,2)
img6 = PhotoImage(file = f'./imagens/{tema}/imagem6.png').subsample(2,2)
img7 = PhotoImage(file = f'./imagens/{tema}/imagem7.png').subsample(2,2)
img8 = PhotoImage(file = f'./imagens/{tema}/imagem8.png').subsample(2,2)
inicio = PhotoImage(file = f'./imagens/inicio.png').subsample(2,2)


#inicializar jogo

iniciar()


#criar labels para jogadas e recorde

njoga = Label(contentor, text=f'Número de jogadas: {jogadas}', bg='lightyellow', font= ('Helvetica', 12, 'bold'))
rec = Label(contentor, text=f'Recorde de jogadas: {recorde}', bg='lightyellow', font= ('Helvetica', 12, 'bold'))
njoga.grid(row=0, column=0, padx=20)
rec.grid(row=0, column=1, padx=20)


#criar botões com imagem inicial

b0 = Button(frame, image=inicio, command=lambda: click_botao(b0, 0), cursor = 'hand2', relief='groove')
b1 = Button(frame, image=inicio, command=lambda: click_botao(b1, 1), cursor = 'hand2', relief='groove')
b2 = Button(frame, image=inicio, command=lambda: click_botao(b2, 2), cursor = 'hand2', relief='groove')
b3 = Button(frame, image=inicio, command=lambda: click_botao(b3, 3), cursor = 'hand2', relief='groove')
b4 = Button(frame, image=inicio, command=lambda: click_botao(b4, 4), cursor = 'hand2', relief='groove')
b5 = Button(frame, image=inicio, command=lambda: click_botao(b5, 5), cursor = 'hand2', relief='groove')
b6 = Button(frame, image=inicio, command=lambda: click_botao(b6, 6), cursor = 'hand2', relief='groove')
b7 = Button(frame, image=inicio, command=lambda: click_botao(b7, 7), cursor = 'hand2', relief='groove')
b8 = Button(frame, image=inicio, command=lambda: click_botao(b8, 8), cursor = 'hand2', relief='groove')
b9 = Button(frame, image=inicio, command=lambda: click_botao(b9, 9), cursor = 'hand2', relief='groove')
b10 = Button(frame, image=inicio, command=lambda: click_botao(b10, 10), cursor = 'hand2', relief='groove')
b11 = Button(frame, image=inicio, command=lambda: click_botao(b11, 11), cursor = 'hand2', relief='groove')
b12 = Button(frame, image=inicio, command=lambda: click_botao(b12, 12), cursor = 'hand2', relief='groove')
b13 = Button(frame, image=inicio, command=lambda: click_botao(b13, 13), cursor = 'hand2', relief='groove')
b14 = Button(frame, image=inicio, command=lambda: click_botao(b14, 14), cursor = 'hand2', relief='groove')
b15 = Button(frame, image=inicio, command=lambda: click_botao(b15, 15), cursor = 'hand2', relief='groove')


#dispor botões em grid

lista_btn = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]

for y in range(4):
    for x in range(4):
        lista_btn[4*y+x].grid(row=y, column=x)


#criar label para mensagem de texto

legenda = Label(janela, text='', bg='Bisque', font= ('Helvetica', 20, 'bold'))
legenda.pack(pady=15)


#criar listas de mensagens de texto

lista_certo = ['Certíssimo!','És o maior!','Bem jogado!','Craque!','Siga!','Boa!']
lista_errado = ['Incorreto!','Tenta novamente!','Podes fazer melhor!','Não estás atento!','Nope!','Errado!']


#criar menu de opções

menu = Menu(janela)
janela.config(menu=menu)

opcoes_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Opções do jogo', menu=opcoes_menu)
opcoes_menu.add_command(label='Reiniciar jogo', command=limpar)
opcoes_menu.add_separator()
opcoes_menu.add_command(label='Escolher novo tema', command=lambda:os.execv(sys.executable, ['python'] + sys.argv))
opcoes_menu.add_separator()
opcoes_menu.add_command(label='Sair do jogo', command=janela.destroy)


#mensagem copyright

icon = PhotoImage(file = './imagens/omega3344.png').subsample(30,30)
copyr = Label(janela, image=icon, text='\u00A9 2022 - Fernando Cunha  ', font= ('Helvetica', 7), bg='Bisque', compound=LEFT)
copyr.pack(anchor=SE)


#manter janela ativa

janela.mainloop()


####################################################################################################
#                                   © 2022 - Fernando Cunha                                        #
####################################################################################################