'''
Criar uma aplicação GUI que irá mostrar uma lista de dicionários na tela, exibindo todos os campos
Junto de cada registro, incluir dois botões, atualizar e apagar
Não é necessário ter a funcionalidade em um primeiro momento
'''
from banco import get_all,delete

import tkinter as tk
from tkinter import ttk, messagebox

def main():
    app=Consulta()
    app.mainloop()

class Consulta(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Consulta do Banco de Dados')
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)
        self.minsize(1000,500)

        self.lbl=ttk.Label(self,text='Registros\n',anchor='center')
        self.lbl.grid(row=0,column=0,sticky='ew')

        self.data_header=ttk.Label(self,text='Nome\t\tRA\t\tCurso')
        self.data_header.grid(row=1,column=0,sticky='ew')

        self.get_info()

        self.atualiza_btn=ttk.Button(self,text='Atualizar',command=self.atualizar)
        self.atualiza_btn.grid(row=1,column=1)
    
    def get_info(self):
        self.principal=MainFrame(self)
        self.principal.grid(row=2,column=0,sticky='nsew')

    def atualizar(self):
        self.principal.destroy()
        self.get_info()

class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.parent=parent

        l=get_all()
        for i in l:
            info=InfoDisplay(self,i['id'],i['nome'],i['ra'],i['curso'])
            info.grid(row=l.index(i),column=0,sticky='ew',padx=5,pady=5)

class InfoDisplay(ttk.Frame):
    def __init__(self,parent,id,nome,ra,curso):
        super().__init__(parent)
        self.parent=parent
        self.id=id
        self.nome=nome
        self.ra=ra
        self.curso=curso
        
        self.columnconfigure(0,weight=3)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        self.label1=ttk.Label(self, text=f'{nome}\t\t{ra}\t\t{curso}\t')
        self.label1.grid(row=0,column=0,sticky='ew')

        self.update_btn=ttk.Button(self,text='Atualizar',command=self.atualizar)
        self.update_btn.grid(row=0,column=1,sticky='ew')

        self.delete_btn=ttk.Button(self,text='Deletar',command=self.deletar)
        self.delete_btn.grid(row=0,column=2,sticky='ew')

    def atualizar(self):
        self.parent.parent.destroy()

    def deletar(self):
        a=messagebox.askquestion('Deletar','Confirmar Deleção?')
        if a=='yes':
            delete(self.id)
            self.destroy()

if __name__=='__main__':
    main()