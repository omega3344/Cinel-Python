###FUNÇÕES
def lerdados():
     nome = e1.get()
     morada = e2.get()
     frase = f'O nome é «{nome}» e a morada é «{morada}»'
     l4.configure(text=frase, relief='raised')     
     
def limpar():
     e1.delete(0, END)
     e2.delete(0, END)
     e1.focus()
     #l4.configure(text='', relief='flat')
     l4['text'] = ''
     


def sair():
     jan.destroy()
     
def relogio():
     hora = strftime('%H:%M:%S')
     lrelogio['text']= hora
     lrelogio.after(1000, relogio)
     
########################################
from tkinter import * #import tkinter
from time import strftime

fonte = ('Arial', 14)
fonte2 = ('Comic Sans Ms', 20, 'bold')
fonte3 = ('Times New Roman', 12, 'bold')

jan = Tk()

jan.title('Exercício 15 ficha 4')

#centrar janela
largecra = jan.winfo_screenwidth()
altecra = jan.winfo_screenheight()
larg=370   #larg/2
alt=250    #alt/2
posx = largecra//2 - larg//2
posy = altecra//2 - alt//2
jan.geometry(f"{larg}x{alt}+{posx}+{posy}")

l1 = Label(jan, text = 'Nome:',font = fonte)
l2 = Label(jan, text = 'Morada:',font = fonte)
e1 = Entry(jan, width = 20,font = fonte)
e2 = Entry(jan, width = 20,font = fonte)
b1 = Button(jan, text = 'Ler dados', width = 10,
            command = lerdados,font = fonte)
b2 = Button(jan, text = 'Limpar', width = 10,
            command = limpar,font = fonte)
b3 = Button(jan, text = 'Sair', bg='red',
            command = sair,font = fonte)

l3 = Label(jan, text = 'Os dados lidos são:', font = fonte)
l4 = Label(jan, font = fonte3, fg = 'blue', text = '')

#RELOGIO
lrelogio = Label(jan, font = fonte2,
                 fg='green',relief='ridge')
lrelogio.place(x=230, y=195) #posiciona relogio onde pretendemos...

##VER
l1.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1, columnspan = 2)
l2.grid(row = 1, column = 0)
e2.grid(row = 1, column = 1, columnspan = 2)
b1.grid(row = 2, column = 0,padx=5, pady=5) #pad's moldura do botão
b2.grid(row = 2, column = 1,padx=5, pady=5)
b3.grid(row = 2, column = 2,padx=5, pady=5)
l3.grid(row = 3, column = 0, columnspan=2, sticky=W) #sticky: encosta a Oeste(W)
l4.grid(row = 4, column = 0, columnspan=3)

e1.focus() #cursor posicionado na caixa E1


#Chama a função para criar relogio
relogio()

jan.mainloop()
