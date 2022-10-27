##FUNÇÕES
def sair():
     jan.destroy()
     
#######
from tkinter import *

#1
jan = Tk() #inicia objeto do tipo janela
#2
jan.title('Primeira janela em Tk') #muda título
#3
jan['bg']='Orange' #coloca cor no fundo da janela
#4
x,y = 400,330 #largura e altura da janela
jan.geometry(f'{x}x{y}')
#5
jan.resizable(False,False) #não permite redimensionar
#6
fonte = ('Comic Sans Ms',14,'bold')#variável com formatações para usar nas fontes
#7
jan.iconbitmap('snake.ico')
#8
jan.geometry(f'{x}x{y}+300+500') #define tamanhos e posições

#9
lab = Label(jan, text='Olá Python')
lab.pack()
#lab.grid()
#lab.place(x=20, y=30)

#10
lab['font'] = fonte #definido na alinea 6
#lab.configure(font=fonte)

#11
ent = Entry(jan)
ent.pack()
#12
bsair = Button(jan, text = "Sair")
#13
bsair['command']=sair

#14
bsair.configure(bd=4, bg='pink', fg='blue')
#bsair['bd']=4
#bsair['bg']='pink'
#bsair['fg']='blue'
bsair.pack()

jan.mainloop()
