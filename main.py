import tkinter as tk
from tkinter import ttk

from consulta import Consulta

def main():
    app=Aplication()
    app.mainloop()

class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Aplicação GUI Tkinter')
        self.minsize(360,375)

        self.consulta_btn=ttk.Button(self,text='Consultar Registros',command=self.cria_consulta)
        self.consulta_btn.grid(row=0,column=0,padx=5,pady=5)

        self.adicionar_btn=ttk.Button(self,text='Adicionar Registros')
        self.adicionar_btn.grid(row=1,column=0,padx=5,pady=5)

    def cria_consulta(self):
        app_consulta=Consulta()
        app_consulta.mainloop()

if __name__=='__main__':
    main()