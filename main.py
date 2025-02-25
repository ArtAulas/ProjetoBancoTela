'''
Criar uma aplicação GUI que irá mostrar uma lista de dicionários na tela, exibindo todos os campos
Junto de cada registro, incluir dois botões, atualizar e apagar
Não é necessário ter a funcionalidade em um primeiro momento
'''

l=[
    {
        'nome':'Arthur',
        'ra':'2302331',
        'curso':'SI'
    },
    {
        'nome':'Bárbara',
        'ra':'1873810',
        'curso':'ADS'
    },
    {
        'nome':'Camily',
        'ra':'1562037',
        'curso':'GTI'
    },
    {
        'nome':'Roberto',
        'ra':'1389021',
        'curso':'SI'
    },
    {
        'nome':'José',
        'ra':'2204781',
        'curso':'ADS'
    }
]

import tkinter as tk
from tkinter import ttk

def main():
    app=Aplication()
    app.mainloop()

class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Segunda Aplicação')
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)
        self.minsize(1000,500)

        self.lbl=ttk.Label(self,text='Registros\n',anchor='center')
        self.lbl.grid(row=0,column=0,sticky='ew')

        self.data_header=ttk.Label(self,text='Nome\t\tRA\t\tCurso')
        self.data_header.grid(row=1,column=0,sticky='ew')

        self.principal=MainFrame(self)
        self.principal.grid(row=2,column=0,sticky='nsew')

class MainFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)

        for i in l:
            info=InfoDisplay(self,i['nome'],i['ra'],i['curso'])
            info.grid(row=l.index(i),column=0,sticky='ew',padx=5,pady=5)

class InfoDisplay(ttk.Frame):
    def __init__(self,parent,nome,ra,curso):
        super().__init__(parent)
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
        print('TODO')

    def deletar(self):
        new=NameDisplay()
        new.mainloop()
        print('TODO')

class NameDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Confirmação')

        self.label=ttk.Label(self,text='Confirmar Deleção')
        self.label.grid(row=0,column=0, columnspan=2)

        self.btn=tk.Button(self,text='Confirmar',command=self.confirm)
        self.btn.grid(row=1,column=0)

        self.btn_canc=tk.Button(self,text='Cancelar',command=self.destroy)
        self.btn_canc.grid(row=1,column=1)
    
    def confirm(self):
        print('Confirmou deleção')
        self.destroy()


if __name__=='__main__':
    main()