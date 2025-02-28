import tkinter as tk
from tkinter import ttk, messagebox

from banco import insert

def main():
    a=Cadastro()
    a.mainloop()

class Cadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cadastro')

        self.titulo_lbl=ttk.Label(self,text='Cadastro de Usuário')
        self.titulo_lbl.grid(row=0,column=0,padx=5,pady=5)

        self.nome_lbl=ttk.Label(self,text='Nome:')
        self.nome_lbl.grid(row=1,column=0)
        self.nome_entry=ttk.Entry(self)
        self.nome_entry.grid(row=1,column=1)

        self.ra_lbl=ttk.Label(self,text='RA:')
        self.ra_lbl.grid(row=2,column=0)
        self.ra_entry=ttk.Entry(self)
        self.ra_entry.grid(row=2,column=1)

        self.curso_lbl=ttk.Label(self,text='Curso:')
        self.curso_lbl.grid(row=3,column=0)
        self.curso_entry=ttk.Entry(self)
        self.curso_entry.grid(row=3,column=1)

        self.confimar_btn=ttk.Button(self,text='Confirmar Cadastro', command=self.cadastrar)
        self.confimar_btn.grid(row=4,column=0)

        self.cancelar_btn=ttk.Button(self,text='Cancelar', command=self.destroy)
        self.cancelar_btn.grid(row=4,column=1)

    def cadastrar(self):
        dic={
            'nome':self.nome_entry.get(),
            'ra':self.ra_entry.get(),
            'curso':self.curso_entry.get()
        }
        try:
            insert(dic)
            messagebox.showinfo('Confirmação','Cadastro Realizado Com Sucesso')
            self.destroy()
        except:
            messagebox.showerror('Erro','RA já cadastrado')

if __name__=='__main__':
    main()