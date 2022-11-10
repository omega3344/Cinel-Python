



def nova():
     def sair():
          janela.attributes('-disabled', False) #torna clicável janela 1
          janela.deiconify()#volta  restaurar a janela nº1
          jan.destroy()#destroi 2º janela

     jan = Tk()
     jan.title("Janela 2")
     jan['bg'] = 'Lightblue'
     jan.geometry("400x300+300+500")
     jan.resizable(0,0)
     jan.focus_force() #ativa janela 2
     bsair = Button(jan, text = "Sair",
                    command = sair)
     
     janela.attributes('-disabled', True)
     janela.iconify()#oculta a janela nº1
     
     bsair.pack()
     
     jan.mainloop()



####
from tkinter import *

janela = Tk()
janela['bg'] = 'Orange'
janela.title("Nova janela")
fonte = ("Comic Sans Ms", 14, "bold")
janela.geometry("400x300+300+500")
janela.resizable(0,0)

botao = Button(janela, text = "Nova janela",
               command = nova)

######MOSTRAR
botao.pack()

janela.mainloop()





