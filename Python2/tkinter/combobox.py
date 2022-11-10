####FUNÇÕES
def escrever(evento): #reage ao BIND da combobox
     print(f'Foi escolhido o desporto {combo.get()}')


def inserir():
     novodesp = ent.get().title()

     if len(novodesp) == 0: #verifica se campo está vazio
          showinfo(title='Mensagem de alerta',
                   message='Precisa preencher o campo "Novo desporto"') 
     #tenta preencher
     elif novodesp not in desportos:
          desportos.append(novodesp) #anexa novo desporto à lista
          desportos.sort()
          combo['values'] = desportos #combo.configure(values=desportos)
          showinfo(title='Sucesso',
                   message=f"«{novodesp}» foi adicionado listagem corretamente")
     else:
          showinfo(title='Mensagem de alerta',
                   message=f'{novodesp} já existe na lista')
          
     ent.delete(0,END)
     ent.focus()

     
#######################
########JANELA
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import * #bib para apresentar janelas de mensagem

jan = Tk()
jan.geometry('350x200')

desportos = ['Futebol', 'Natação', 'Hóquei']
desportos.sort()

lab = Label(jan, text='Desporto favorito: ')
combo = ttk.Combobox(jan, values = desportos, width=20)
combo.set(desportos[2])#atribui valor pré-preenchido
#combo['state'] = 'readonly'
#combo['justify'] = 'center'
combo.configure(state='readonly', justify='center')


lab2 = Label(jan, text='Novo desporto:')
ent = Entry(jan, width=20)

botao = Button(jan, text='Inserir', command=inserir)

#####
#VER OS OBJETOS
lab.grid(row=0, column=0)
combo.grid(row=0, column=1)

lab2.grid(row=1, column=0)
ent.grid(row=1, column=1)
botao.grid(row=1, column=2)

##### BIND's
#combo.bind('< TAG >', funcao)
combo.bind('<<ComboboxSelected>>', escrever)

jan.mainloop()
