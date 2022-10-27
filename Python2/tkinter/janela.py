
from tkinter import *


def sair():
    print('Foi um gosto!\n Até uma próxima...')    
    #janela.destroy()
    e1.forget()
    
def mostrar():
    e1.pack()


janela = Tk()

x = 500
y = 300
posx = 0
posy = 0

janela.title('Primeira janela')
janela.geometry(f'{x}x{y}+{posx}+{posy}')

#janela['bg'] = 'orange'
janela['bg'] = '#00ABF6'

fonte = ('Comic Sans Ms',20,'italic')

label1 = Label(janela,text='Nome:', relief=GROOVE)
entry1 = Entry(janela,width=100)
b1 = Button(janela, text='bye-bye',font = fonte,
            bg='white',fg='red',bd=10,
            command = sair)

b2 = Button(janela, text='bye-bye',font = fonte,
            bg='red',fg='white',bd=10,
            command = mostrar)

e1 = Entry(janela,bg='pink',font = fonte, fg = 'blue')

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
e1.grid(row=1, column=0)
#e1.pack()

#blimpa = Button(janela, text='Limpar',command=limpar,bg='orange')

#janela.iconbitmap('snake.ico')

#janela.resizable(0,0)
#janela.maxsize(100,800)
#janela.minsize(50,50)

#janela.state('zoomed')
#janela.state('iconic')

janela.mainloop()

'''
root = Tk()

root.geometry('300x300')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
root.mainloop()
'''