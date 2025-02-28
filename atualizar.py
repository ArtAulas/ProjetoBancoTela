import tkinter as tk
from tkinter import ttk, messagebox
from banco import get_one, update

def main():
    app=Atualizar(id=2)
    app.mainloop()

class Atualizar(tk.Tk):
    def __init__(self,id):
        super().__init__()
        self.title('Atualizar')
        self.id=id
        self.info=get_one(id)

        self.titulo=ttk.Label(self,text='Atualizar Registro')
        self.titulo.grid(row=0,column=0,padx=5,pady=5)

        self.nome_lbl=ttk.Label(self,text='Nome:')
        self.nome_lbl.grid(row=1,column=0)
        self.nome_entry=ttk.Entry(self)
        self.nome_entry.insert(0,self.info['nome'])
        self.nome_entry.grid(row=1,column=1)

        self.ra_lbl=ttk.Label(self,text='RA:')
        self.ra_lbl.grid(row=2,column=0)
        self.ra_entry=ttk.Label(self,text=self.info['ra'])
        self.ra_entry.grid(row=2,column=1)

        self.curso_lbl=ttk.Label(self,text='Curso:')
        self.curso_lbl.grid(row=3,column=0)
        self.curso_entry=ttk.Entry(self)
        self.curso_entry.insert(0,self.info['curso'])
        self.curso_entry.grid(row=3,column=1)

        self.confimar_btn=ttk.Button(self,text='Atualizar Informações',command=self.atualizar)
        self.confimar_btn.grid(row=4,column=0)

        self.cancelar_btn=ttk.Button(self,text='Cancelar', command=self.destroy)
        self.cancelar_btn.grid(row=4,column=1)

    def atualizar(self):
        dic={
            'id':self.info['id'],
            'nome':self.nome_entry.get(),
            'ra':self.info['ra'],
            'curso':self.curso_entry.get()
        }
        try:
            update(dic)
            messagebox.showinfo('Confirmação','Atualização Realizada com Sucesso')
            self.destroy()
        except:
            messagebox.showerror('Erro','Erro')

if __name__=='__main__':
    main()