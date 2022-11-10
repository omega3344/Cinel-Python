##FUNÇÕES
def remover(): 
     #pos = lb.get(0) #obtém texto do índice 0
     #print('POS=', pos)
     pos = lb.curselection()
     print('POSIÇÕES=', pos)
     #lb.delete(pos[0], pos[-1])

     for x in pos[::-1]: #(1,2) apaga a linha 1 e a linha 2
          resp = askyesnocancel(message=f'selecionou linha com nome {lb.get(x)}')
          #print(resp)

          if resp:
               print('Escolheu SIM')
               lb.delete(x)
          elif resp == False:
               print('Escolheu NÃO')
          else:
               print('Cancelou a escolha')
               break
          
###
from tkinter import *
from tkinter.messagebox import *


janela = Tk()
janela['bg'] = 'Orange'
janela.title("Listbox")
fonte = ("Comic Sans Ms", 14, "bold")
janela.geometry("400x300+300+500")

lista = ['Ana', 'Rui', 'Manuel', 'Xica']
lista.sort() #ordena a lista por ordem lexicográfica

lb = Listbox(janela, font = fonte,
             height = 5,
             selectmode=EXTENDED)

for elem in lista: #para cada elemento...
     lb.insert(0, elem)

botao = Button(janela, text = "Apagar",
               command = remover)

######MOSTRAR
lb.pack()
botao.pack()

janela.mainloop()
