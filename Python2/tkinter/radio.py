def escreve():
     opcao = genero.get()
     print(f'O valor associado ao click foi {opcao}')

def escreve2():
     opcao = cores.get()
     print(f'O valor associado à cor é {opcao}')
     r1['bg'] = 'SystemButtonFace'

     
#######################
from tkinter import *

jan = Tk()
jan.geometry('250x200')

genero = IntVar()
cores = IntVar()

r1 = Radiobutton(jan,text='Feminino',bg='Red',
                 value=5, variable=genero,
                 command=escreve)
r2 = Radiobutton(jan,text='Masculino',bg='Blue',
                 value=1, variable=genero,
                 command=escreve)
r3 = Radiobutton(jan,text='Binário',bg='Pink',
                 value=2, variable=genero,
                 command=escreve)
r4 = Radiobutton(jan,text='Não Binário',bg='Orange',
                 value=3, variable=genero,
                 command=escreve)

r5 = Radiobutton(jan,text='Branco',
                 value=5, variable=cores,
                 command=escreve2)
r6 = Radiobutton(jan,text='Preto',
                 value=1, variable=cores,
                 command=escreve2)

r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()

jan.mainloop()
