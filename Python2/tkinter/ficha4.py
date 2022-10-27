#ficha 4

from tkinter import *
'''
def sair():
    janela.destroy()

#1
janela = Tk()

#2
janela.title("Primeira janela em Tk")

#3
janela['bg'] = 'orange'

#4
x = 400
y = 330
janela.geometry(f'{x}x{y}')

#5
janela.resizable(0,0)

#6
fonte = ('Comic Sans MS', 14, 'bold')

#7
#janela.iconbitmap('lion.ico')

#8
posx = 300
posy = 500
janela.geometry(f'+{posx}+{posy}')

#9 #10
label = Label(janela, text='Olá Python', font = fonte)
label.pack()
#label.place()

#11
entrada = Entry(janela, width=50)
entrada.pack()

#12 #13 #14
bt = Button(janela, text='Sair', bg='navy',bd=10, command = sair)
bt.pack()

'''

#15
janela2 = Tk()

janela2.title('1ª janela')

janela2.geometry('300x300')

label1 = Label(janela2, text='Nome:')
entrada1 = Entry(janela2, width=30)
label2 = Label(janela2, text='Morada:')
entrada2 = Entry(janela2, width=30)

label1.grid(row=0, column=0)
entrada1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entrada2.grid(row=1, column=1)

bt1 = Button(janela2, text='Ler Dados')
bt2 = Button(janela2, text='Limpar')
bt3 = Button(janela2, text='Sair', bg='red')

bt1.grid(row=2, column=1)
bt2.grid(row=2, column=1)
bt3.grid(row=2, column=1)


#a












#janela.mainloop()
janela2.mainloop()



